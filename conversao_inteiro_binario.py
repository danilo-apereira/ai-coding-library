def inteiro_para_binario(numero):
    return f"{numero & 0xFF:08b}"

def binario_para_inteiro(binario):
    return int(binario, 2)

numero_teste = 45
binario = inteiro_para_binario(numero_teste)
decimal = binario_para_inteiro(binario)

print(f"Número inteiro: {numero_teste}")
print(f"Número binário: {binario}")
print(f"Número decimal a partir do binário: {decimal}")
