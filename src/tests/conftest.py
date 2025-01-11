# from base64 import b64encode
import pytest
import os
from dotenv import load_dotenv 
from ..utils.request_gen import APICaller



load_dotenv()


@pytest.fixture(scope="module", autouse=True)
def get_api_obj():
    BASE_URL = os.getenv("BASE_URL")
    # API_ID = os.getenv("API_ID")
    # API_TOKEN = os.getenv("API_TOKEN")
    # token = b64encode(f"{API_ID}:{API_TOKEN}".encode('utf-8')).decode("ascii")
    headers = {"Connection": f"keep-alive"}
    api_obj = APICaller(BASE_URL,headers)
    return api_obj
