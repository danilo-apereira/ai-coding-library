import random
import math

def gerar_populacao(tamanho_populacao=50):
    return [random.randint(-100, 100) for _ in range(tamanho_populacao)]

def calcular_fitness(valor):
    return abs(valor * math.sin(math.sqrt(abs(valor))))

def inteiro_para_binario(numero):
    return format(numero if numero >= 0 else (1 << 8) + numero, '08b')

def binario_para_inteiro(binario):
    numero = int(binario, 2)
    return numero if numero < 128 else numero - (1 << 8)

def cruzar_individuos(bin1, bin2):
    ponto_cruzamento = random.randint(1, len(bin1) - 1)
    novo_individuo = bin1[:ponto_cruzamento] + bin2[ponto_cruzamento:]
    return novo_individuo

def competicao_para_reproducao(populacao, fitness):
    def selecionar_mais_apto():
        indice1, indice2 = random.sample(range(len(populacao)), 2)
        return indice1 if fitness[indice1] >= fitness[indice2] else indice2

    vencedor1 = selecionar_mais_apto()
    vencedor2 = selecionar_mais_apto()

    binario_vencedor1 = inteiro_para_binario(populacao[vencedor1])
    binario_vencedor2 = inteiro_para_binario(populacao[vencedor2])

    novo_individuo_binario = cruzar_individuos(binario_vencedor1, binario_vencedor2)

    novo_individuo_decimal = binario_para_inteiro(novo_individuo_binario)
    novo_fitness = calcular_fitness(novo_individuo_decimal)

    print(f"\nIndivíduos selecionados para cruzamento:")
    print(f"Vencedor 1: Índice {vencedor1} - Valor {populacao[vencedor1]} - Binário {binario_vencedor1}")
    print(f"Vencedor 2: Índice {vencedor2} - Valor {populacao[vencedor2]} - Binário {binario_vencedor2}")

    return novo_individuo_decimal, novo_fitness

populacao = gerar_populacao()
valores_fitness = [calcular_fitness(x) for x in populacao]

print(f"{'Índice':<10}{'Indivíduo (Decimal)':<20}{'Fitness':<20}")
print("-" * 50)
for i, (individuo, fitness) in enumerate(zip(populacao, valores_fitness)):
    print(f"{i:<10}{individuo:<20}{fitness:<20.5f}")

novo_individuo, fitness_novo_individuo = competicao_para_reproducao(populacao, valores_fitness)

print(f"\nNovo indivíduo gerado: {novo_individuo}")
print(f"Fitness do novo indivíduo: {fitness_novo_individuo:.5f}")
