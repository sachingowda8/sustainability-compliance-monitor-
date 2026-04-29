from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from services.cache import generate_key, get_cached_response, set_cached_response

recommend_bp = Blueprint('recommend', __name__)

@recommend_bp.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    input_text = data.get("input_text")

    if not input_text:
        return jsonify({"error": "input_text required"}), 400

    # Unique key
    key = generate_key("recommend:" + input_text)

    # Check cache
    cached = get_cached_response(key)
    if cached:
        cached["cached"] = True
        return jsonify(cached)

    # Call AI
    result = call_groq(f"Give 3 sustainability recommendations for: {input_text}")

    # DO NOT cache fallback
    if isinstance(result, dict) and result.get("is_fallback"):
        return jsonify({
            "recommendations": result,
            "cached": False
        })

    response = {
        "recommendations": result,
        "cached": False
    }

    # Store valid response
    set_cached_response(key, response)

    return jsonify(response)