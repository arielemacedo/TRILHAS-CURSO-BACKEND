# Desafio Nível 1 — PDV com Descontos (Python)

## O que o código faz

Este programa simula a lógica de um PDV (Ponto de Venda) que aplica descontos progressivos em compras. A cada compra, o usuário informa o valor, a idade do cliente, a quantidade de itens e um cupom (opcional). O sistema calcula o valor final aplicando as regras de desconto, guarda cada compra em uma lista e permite várias compras seguidas. Ao encerrar, mostra na tela um resumo do dia (quantidade de compras, total bruto, total de descontos e total final) e grava esse resumo, junto com o detalhe de cada compra, no arquivo `resumo.txt`.

## Como o código faz

1. O programa entra em um loop e pede o **valor da compra**.
2. Se o valor for `0`, o loop termina e o programa vai para o resumo final.
3. Se o valor for negativo, mostra um aviso e volta a pedir (`if` + `continue`).
4. Pede a **idade** do cliente. Se for negativa, mostra um aviso e volta a pedir (`if` + `continue`).
5. Pede a **quantidade de itens** e o **cupom de desconto** (o cupom é convertido para maiúsculas com `.upper()`).
6. **Regra 1 — desconto por idade:** se a idade for maior ou igual a 65, aplica 20% de desconto sobre o valor original.
7. **Regra 2 — desconto por valor:** se o valor *já com o desconto de idade* for maior que 100, aplica mais 10% sobre esse valor.
8. **Bônus 1 — desconto por quantidade:** se a quantidade de itens for maior que 3, aplica 5% de desconto extra sobre o valor atual.
9. **Bônus 2 — cupom de fidelidade:** se o cupom for `FIDELIDADE10`, aplica 10% de desconto extra sobre o valor atual.
10. Calcula o desconto total da compra (valor original − valor final) e exibe o valor final no formato `R$ 144.00`.
11. Guarda a compra (valor original, desconto total e valor final) em uma lista com `.append()`.
12. O loop recomeça, permitindo uma nova compra.
13. Ao digitar `0`, o programa percorre a lista com um `for`, soma os valores e monta o **resumo do dia**:
    - Quantidade de compras registradas
    - Total bruto (soma dos valores originais)
    - Total de descontos concedidos
    - Total final (soma dos valores com desconto)
14. **Bônus 3 — salvar histórico:** o resumo é gravado em `resumo.txt` com `open(..., "w")`, e um `for` na lista escreve no arquivo o detalhe de cada compra. O resumo também é exibido no console.

## Como rodar

Dentro da pasta `nivel_1`, execute:

```
python pdv.py
```

Ao rodar, o programa pergunta, nesta ordem: valor da compra, idade, quantidade de itens e cupom.
Para testar apenas as regras principais (valor e idade), responda **1** na quantidade de itens e deixe o cupom **vazio** (apenas Enter), assim nenhum desconto extra é aplicado.

## Tabela de exemplos (casos de teste)

Nestes casos, use quantidade de itens = 1 e cupom vazio.

| #  | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|----|-----------|-------|----------------|----------------|----------------------|
| 1  | 50.00     | 30    | 0%             | 0%             | R$ 50.00             |
| 2  | 100.00    | 30    | 0%             | 0%             | R$ 100.00            |
| 3  | 80.00     | 65    | 20%            | 0%             | R$ 64.00             |
| 4  | 100.00    | 70    | 20%            | 0%             | R$ 80.00             |
| 5  | 125.00    | 70    | 20%            | 0%             | R$ 100.00            |
| 6  | 200.00    | 30    | 0%             | 10%            | R$ 180.00            |
| 7  | 101.00    | 30    | 0%             | 10%            | R$ 90.90             |
| 8  | 200.00    | 65    | 20%            | 10%            | R$ 144.00            |
| 9  | 1000.00   | 80    | 20%            | 10%            | R$ 720.00            |
| 10 | 200.00    | 64    | 0%             | 10%            | R$ 180.00            |

### Casos-limite

- **Caso 2** (`100.00`, idade 30): o valor não é *maior* que 100, então não recebe os 10%.
- **Caso 5** (`125.00`, idade 70): `125 × 0.8 = 100`. Como não é maior que 100, os 10% não se aplicam. Resultado: R$ 100.00.
- **Caso 7** (`101.00`, idade 30): `101 × 0.9 = 90.90`. O valor é exibido com duas casas decimais.
- **Caso 10** (`200.00`, idade 64): a idade é 64, então não há desconto por idade, apenas o de valor (10%). Resultado: R$ 180.00.

## Bônus implementados

| Bônus | Regra |
|-------|-------|
| Desconto por quantidade | Mais de 3 itens: 5% de desconto extra |
| Cupom de fidelidade | Cupom `FIDELIDADE10`: 10% de desconto extra |
| Salvar histórico | Resumo e detalhe das compras gravados em `resumo.txt` |

Exemplo com bônus: compra de `200.00`, idade 65, 5 itens e cupom `FIDELIDADE10`
→ 200 × 0.8 = 160 → × 0.9 = 144 → × 0.95 = 136.80 → × 0.9 = **R$ 123.12**.