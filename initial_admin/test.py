import requests

# Change this URL to match where your FastAPI is running
url = "http://localhost:8000/predictor/"

# Example payload matching your PredictMLInput model
payload = {
    "segment": "esports",
    "game": "valorant",
    "total_rounds": 569,
    "kd": 1.2
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print("Status code:", response.status_code)
print("Response JSON:", response.json())
