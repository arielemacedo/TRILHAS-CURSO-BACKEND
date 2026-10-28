lista = []
while True:

    valor_da_compra = float(input("Valor da Compra (0 para sair): "))

    if valor_da_compra == 0:
        break

    if valor_da_compra < 0:
        print("Aviso: o valor não pode ser negativo. Tente novamente.\n")
        continue

    idade = int(input("Idade: "))

    if idade < 0:
        print("Aviso: a idade não pode ser negativa. Tente novamente.\n")
        continue

    qtd_itens = int(input("Quantidade de Itens: "))

    cupom = input("Cupom de desconto: ").upper()

    valor_total = valor_da_compra

    if idade >= 65:
        valor_total = valor_total * 0.8

    if valor_total > 100:
        valor_total = valor_total * 0.9

    if qtd_itens > 3:
        valor_total = valor_total * 0.95

    if cupom == "FIDELIDADE10":
        valor_total = valor_total * 0.9

    desconto = valor_da_compra - valor_total

    lista.append(
        {
            "valor_original": valor_da_compra,
            "desconto_total": desconto,
            "valor_final": valor_total,
        }
    )

    print(f"Valor Total: R$ {valor_total:.2f}")

if len(lista) == 0:
    print("Nenhuma compra registrada")
else:
    total_bruto = 0
    desconto_geral = 0
    total_final = 0

    for compra in lista:
        total_bruto += compra["valor_original"]
        desconto_geral += compra["desconto_total"]
        total_final += compra["valor_final"]

    total_geral = f"""
          RELATÓRIO DE VENDAS - PDV 
    -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    Quantidade de compras registradas: {len(lista)}
    Total bruto (soma dos valores originais): {total_bruto:.2f}
    Total de descontos concedidos: {desconto_geral:.2f}
    Total final (soma dos valores com desconto):{total_final:.2f}
    -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
\n"""

    with open("resumo.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(total_geral)
        arquivo.write("Compras:\n")
        for i, compra in enumerate(lista, start=1):
            arquivo.write(f"""
    {i}. Original: R$ {compra['valor_original']:.2f} | "
    Desconto: R$ {compra['desconto_total']:.2f} | "
    Final: R$ {compra['valor_final']:.2f}\n""")

    print(total_geral)
