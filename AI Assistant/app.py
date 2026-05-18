from flask import Flask, request, jsonify
from core.faq import buscar_faq
from core.calc import simulacao
from core.ai import responder_ia

app = Flask(__name__)

contexto_usuario = []

@app.route("/")
def home():
    return "🚀 Finance AI com Gemini rodando com sucesso!"

@app.route("/chat", methods=["POST"])
def chat():
    global contexto_usuario

    try:
        data = request.json
        msg = data.get("message")

        if not msg:
            return jsonify({"response": "Mensagem vazia."})

        # FAQ primeiro
        faq = buscar_faq(msg)
        if faq:
            resposta = faq

        else:
            # Simulação financeira
            sim = simulacao(msg)
            if sim:
                resposta = sim

            else:
                # IA Gemini
                try:
                    resposta = responder_ia(msg, contexto_usuario)

                except Exception as erro:
                    print("ERRO GEMINI:", erro)

                    resposta = (
                        "⚠️ IA temporariamente indisponível no momento.\n"
                        "Limite da API atingido ou erro externo.\n"
                        "Tente novamente em instantes."
                    )

        contexto_usuario.append(f"Usuário: {msg}")
        contexto_usuario.append(f"IA: {resposta}")

        return jsonify({"response": resposta})

    except Exception as erro:
        print("ERRO GERAL:", erro)

        return jsonify({
            "response": "Erro interno no servidor."
        })


if __name__ == "__main__":
    app.run(debug=True)