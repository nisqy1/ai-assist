import re

def simulacao(texto):
    """
    Exemplo:
    '1000 10 12' = valor, juros %, meses
    """

    match = re.search(r"(\d+)\s+(\d+)\s+(\d+)", texto)

    if not match:
        return None

    valor = float(match.group(1))
    juros = float(match.group(2)) / 100
    meses = int(match.group(3))

    resultado = valor * (1 + juros) ** meses

    return f"📊 Simulação: R$ {resultado:.2f} após {meses} meses."