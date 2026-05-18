import json

with open("data/faq.json", "r", encoding="utf-8") as f:
    FAQ = json.load(f)

def buscar_faq(msg):
    msg = msg.lower()

    for item in FAQ:
        if item["pergunta"] in msg:
            return item["resposta"]

    return None