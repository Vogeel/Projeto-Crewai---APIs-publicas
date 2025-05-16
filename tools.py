from crewai.tools import BaseTool
import requests
import time

class NumVerifyTool(BaseTool):
    name: str = "Validador de Número"
    description: str = "Valida números de telefone e retorna informações como país e operadora."

    def _run(self, number: str = "+5511987654321") -> str:
        response = requests.get(
            f"http://apilayer.net/api/validate?access_key=5a88cad60f9af373b7956c75bf2edcc1&number={number}&country_code=&format=1"
        )
        time.sleep(8)
        return str(response.json())

class IpStackTool(BaseTool):
    name: str = "Localizador de IP"
    description: str = "Retorna informações sobre um endereço IP, como país e cidade."

    def _run(self, ip: str = "187.75.194.108") -> str:
        response = requests.get(
            f"http://api.ipstack.com/{ip}?access_key=a0545fb3d3ff99ba311868fbe42b1a8b"
        )
        time.sleep(8)
        return str(response.json())

class MarketStackTool(BaseTool):
    name: str = "Consulta de Ações"
    description: str = "Retorna dados de mercado de ações para uma empresa específica."

    def _run(self, symbol: str = "AAPL") -> str:
        response = requests.get(
            f"http://api.marketstack.com/v1/eod?access_key=a2dd96156ae00e4e779c77c4f0f95d31&symbols={symbol}"
        )
        time.sleep(8)
        return str(response.json())
