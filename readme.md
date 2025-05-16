# ✅ Projeto CrewAI

Este projeto usa CrewAI, totalmente compatível com a versão atual da biblioteca.
gera um arquivo no estilo relatório que apresenta informações de um IP, telefone e ação espécífica

## APIs usadas

- NumVerify: Validação de número
- IpStack: Localização de IP
- MarketStack: Dados de ações

`Obs: Deixar KEY do Groq dentro do arquivo .env`

## Como executar

```bash
python -m venv venv `Utilizar python 3.12`
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Resultado final salvo em: `output/resultado_final.txt`
