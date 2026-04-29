import hashlib
import json
from services.redis_client import redis_client

TTL = 900  # 15 minutes

def generate_key(input_text):
    return hashlib.sha256(input_text.encode()).hexdigest()

def get_cached_response(key):
    data = redis_client.get(key)
    return json.loads(data) if data else None

def set_cached_response(key, value):
    redis_client.setex(key, TTL, json.dumps(value))