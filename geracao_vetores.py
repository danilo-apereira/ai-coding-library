import numpy as np

def gerar_vetor_aleatorio(tamanho=50, limite_inferior=-100, limite_superior=100):
    return np.random.randint(limite_inferior, limite_superior, size=tamanho)

def calcular_funcao(x):
    return abs(x * np.sin(np.sqrt(abs(x))))

vetor_inicial = gerar_vetor_aleatorio()
vetor_resultado = np.array([calcular_funcao(x) for x in vetor_inicial])

def exibir_vetores(vetor, nome_vetor):
    print(f"{nome_vetor}:")
    for i, valor in enumerate(vetor):
        print(f"Índice {i}: {valor}")

exibir_vetores(vetor_inicial, "Vetor inicial")
exibir_vetores(vetor_resultado, "Vetor resultado")
