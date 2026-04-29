from flask import Blueprint, jsonify
import time
from services.metrics import app_start_time, response_times
health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health():
    uptime = int(time.time() - app_start_time)

    avg_response = (
        sum(response_times) / len(response_times)
        if response_times else 0
    )

    return jsonify({
        "status": "ok",
        "model": "llama3-70b",
        "avg_response_time_ms": round(avg_response, 2),
        "uptime_seconds": uptime
    })