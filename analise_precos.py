precos = []

print("=== Analisador de Preços ===")
print("Digite os preços dos produtos. Digite '0' para encerrar.")

# Loop principal para entrada dos preços
while True:
    p = float(input("Preço: "))

    # Se o usuário digitar 0, encerra a entrada
    if p == 0:
        break

    # Adiciona o valor na lista
    precos.append(p)

# Verifica se existe algum preço informado
if precos:
    # Cálculos básicos sobre os preços informados
    maior = max(precos)
    menor = min(precos)
    media = sum(precos) / len(precos)

    # Exibe os resultados
    print("\n--- Resultado ---")
    print(f"Quantidade de preços: {len(precos)}")
    print(f"Maior preço: R$ {maior:.2f}")
    print(f"Menor preço: R$ {menor:.2f}")
    print(f"Média dos preços: R$ {media:.2f}")
else:
    print("Nenhum preço informado.")
