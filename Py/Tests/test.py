import requests
import json

def call_gpt3(prompt, max_tokens=100):
    url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer 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",
    }
    data = {
        "prompt": prompt,
        "max_tokens": max_tokens,
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

    if response.status_code == 200:
        return response_json["choices"][0]["text"]
    else:
        return f"Error: {response.status_code}, {response_json}"


# Exemplo de uso
banco = input("Digite um banco:")
perfil = input("Digite seu perfil de investidor:")
investimento = input("Qual o valor do investimento:")
rendimento = input("Digite até quanto deseja de rendimento:")
risco = input("Digite a margem de risco:")
texto = f"""
No banco{banco}, com perfil de investidor{perfil}, R${investimento} e rendimento min{rendimento} com risco{risco}, indique três tipos de investimento. Do seguinte modo: Investimento, Rendimento, Margem de risco, breve explicação (até 10 palavras) 
"""


result = call_gpt3(texto, 4000)
print(result)
