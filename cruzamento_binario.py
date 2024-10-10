import random

def cruzamento_binario(pai1, pai2):
    if len(pai1) != 8 or len(pai2) != 8:
        raise ValueError("Os números binários devem ter exatamente 8 caracteres.")

    ponto_cruzamento = random.randint(1, 7)

    filho = pai1[:ponto_cruzamento] + pai2[ponto_cruzamento:]

    return filho

pai1 = "10101010"
pai2 = "01100110"
filho = cruzamento_binario(pai1, pai2)

print(f"Pai 1: {pai1}")
print(f"Pai 2: {pai2}")
print(f"Filho gerado: {filho}")
