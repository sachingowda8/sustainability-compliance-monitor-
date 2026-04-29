from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from services.cache import generate_key, get_cached_response, set_cached_response

# DEFINE blueprint BEFORE using it
describe_bp = Blueprint('describe', __name__)

@describe_bp.route('/describe', methods=['POST'])
def describe():
    data = request.json
    input_text = data.get("input_text")

    if not input_text:
        return jsonify({"error": "input_text required"}), 400

    key = generate_key(input_text)

    # Check cache
    cached = get_cached_response(key)
    if cached:
        cached["cached"] = True
        return jsonify(cached)

    # Call AI
    result = call_groq(input_text)

    # If AI failed → DO NOT cache
    if isinstance(result, dict) and result.get("is_fallback"):
        return jsonify({
            "description": result,
            "cached": False
        })

    response = {
        "description": result,
        "cached": False
    }

    # Only cache valid response
    set_cached_response(key, response)

    return jsonify(response)