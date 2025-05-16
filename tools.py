import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

class NumVerifyTool:
    def _run(self, number: str = "+5511987654321") -> str:
        api_key = os.getenv("NUMVERIFY_KEY")
        response = requests.get(
            f"http://apilayer.net/api/validate?access_key={api_key}&number={number}&format=1"
        )
        return json.dumps(response.json(), indent=2, ensure_ascii=False)

class IpStackTool:
    def _run(self, ip: str = "187.75.194.108") -> str:
        api_key = os.getenv("IPSTACK_KEY")
        response = requests.get(
            f"http://api.ipstack.com/{ip}?access_key={api_key}"
        )
        return json.dumps(response.json(), indent=2, ensure_ascii=False)

class MarketStackTool:
    def _run(self, symbol: str = "AAPL") -> str:
        api_key = os.getenv("MARKETSTACK_KEY")
        response = requests.get(
            f"http://api.marketstack.com/v1/eod?access_key={api_key}&symbols={symbol}"
        )
        return json.dumps(response.json(), indent=2, ensure_ascii=False)
