import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.main import create_app
from app.limiter import reset_limiter 

@pytest.fixture(autouse=True)
def client():
    app = create_app()
    app.config['TESTING'] = True
    reset_limiter() 
    return app.test_client()
