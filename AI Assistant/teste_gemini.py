from google import genai

client = genai.Client(api_key="AIzaSyBxd7dfY141AoRGPyuT8c8uyODAe9TMwnY")

response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents="Explique juros em uma frase simples"
)

print(response.text)