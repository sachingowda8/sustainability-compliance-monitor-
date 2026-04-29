import os
import re
import logging
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from services.groq_client import GroqClient

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Day 3: Security - Rate Limiting (30 requests per minute)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"],
    storage_uri="memory://"
)

# Day 7: OWASP Critical Fix - Add Security Headers
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response

# Initialize AI Client
client = GroqClient()

def sanitize_input(text):
    """
    Clean input to prevent HTML injection and detect prompt injection.
    Returns (cleaned_text, is_valid, error_message)
    """
    if not text or not isinstance(text, str):
        return None, False, "Invalid input format"

    # 1. Strip HTML tags
    clean_text = re.sub(r'<[^>]*?>', '', text)
    
    # 2. Detect Prompt Injection
    # Look for common injection keywords/patterns
    injection_patterns = [
        r"ignore (all )?previous instructions",
        r"system prompt",
        r"instead of",
        r"you are now",
        r"forget (your|what|all)",
        r"no longer an AI",
        r"act as",
        r"sudo mode"
    ]
    
    for pattern in injection_patterns:
        if re.search(pattern, clean_text, re.IGNORECASE):
            logger.warning(f"🚨 Potential Prompt Injection Detected: {clean_text}")
            return None, False, "Security check failed: Prompt injection detected."

    return clean_text.strip(), True, None

@app.route('/api/analyze', methods=['POST'])
@limiter.limit("10 per minute")  # Stricter limit for the AI processing route
def analyze_compliance():
    try:
        data = request.get_json(silent=True)
        if not data or 'query' not in data:
            return jsonify({"error": "Missing 'query' in request body"}), 400

        user_query = data['query']
        
        # Security: Input Sanitization & Injection Detection
        clean_query, is_valid, error_msg = sanitize_input(user_query)
        
        if not is_valid:
            return jsonify({"error": error_msg}), 400
            
        if not clean_query:
            return jsonify({"error": "Invalid or empty query after sanitization"}), 400

        # Day 6: Prompt Tuning - Load prompt from file
        prompt_path = os.path.join(os.path.dirname(__file__), 'prompts', 'sustainability_expert.txt')
        with open(prompt_path, 'r') as f:
            system_prompt = f.read().strip()
            
        ai_response = client.get_completion(clean_query, system_prompt=system_prompt)
        
        # Security: Escape AI response to prevent XSS if rendered in a browser
        # (Basic escaping for demonstration)
        escaped_response = re.sub(r'[<>]', '', ai_response)
        
        return jsonify({
            "status": "success",
            "data": {
                "original_query": user_query,
                "sanitized_query": clean_query,
                "analysis": escaped_response
            }
        })

    except Exception as e:
        logger.error(f"Error in analyze_compliance: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Security Test: Basic health check endpoint"""
    return jsonify({"status": "healthy", "version": "1.0.0"}), 200

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({"error": "Rate limit exceeded. Please try again later."}), 429

if __name__ == '__main__':
    # Day 7: OWASP Critical Fix - Disable debug mode by default in production
    is_debug = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')
    app.run(port=5001, debug=is_debug)
