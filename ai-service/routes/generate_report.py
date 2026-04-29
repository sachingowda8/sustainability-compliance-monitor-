from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from services.cache import generate_key, get_cached_response, set_cached_response

report_bp = Blueprint('report', __name__)

@report_bp.route('/generate-report', methods=['POST'])
def generate_report():
    data = request.json
    input_text = data.get("input_text")

    if not input_text:
        return jsonify({"error": "input_text required"}), 400

    # Unique key
    key = generate_key("report:" + input_text)

    # Check cache
    cached = get_cached_response(key)
    if cached:
        cached["cached"] = True
        return jsonify(cached)

    # Call AI
    result = call_groq(f"Generate a sustainability report for: {input_text}")

    # DO NOT cache fallback
    if isinstance(result, dict) and result.get("is_fallback"):
        return jsonify({
            "report": result,
            "cached": False
        })

    response = {
        "report": result,
        "cached": False
    }

    # Store valid response
    set_cached_response(key, response)

    return jsonify(response)