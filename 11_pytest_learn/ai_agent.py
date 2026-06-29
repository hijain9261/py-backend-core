import requests
def ask_ai_agent(prompt: str, api_key: str) -> str:
    url = f"https://api.example.com/v1/generate?key={api_key}"
    response = requests.post(url, json={"prompt": prompt})
    return response.json()["text"]

    