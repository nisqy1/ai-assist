from google import genai

client = genai.Client(api_key="Your_API_Key")

response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents="Explique juros em uma frase simples"
)

print(response.text)
