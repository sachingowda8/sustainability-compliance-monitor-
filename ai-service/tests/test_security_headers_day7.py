import pytest
import os
import sys

# Add parent dir to path to import app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_security_headers_present(client):
    """Day 7: Verify all critical OWASP security headers are present in the response"""
    response = client.get('/health')
    
    assert response.status_code == 200
    headers = response.headers
    
    assert headers.get('X-Content-Type-Options') == 'nosniff'
    assert headers.get('X-Frame-Options') == 'DENY'
    assert 'max-age=31536000' in headers.get('Strict-Transport-Security', '')
    assert "default-src 'self'" in headers.get('Content-Security-Policy', '')
