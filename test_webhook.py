import requests

url = "http://localhost:5000/webhook"
payload = {"mensagem": "teste"}

res = requests.post(url, json=payload)
print(res.status_code)
print(res.json())