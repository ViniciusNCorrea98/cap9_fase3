print("Insira as toneladas colhidas por mês:")

producao_total = 0
perda_manual_total = 0
perda_maquina_total = 0

for i in range(1, 13, 1):
    producao = int(input(f'Mês {i}....:'))

    if producao < 0:
        producao = int(input(f'Mês {i}....:'))

    perda_manual = producao*0.05
    perda_maquina = producao*0.15

    producao_total += producao
    perda_manual_total += perda_manual
    perda_maquina_total += perda_maquina

    print(f"Perda manual.....: {perda_manual}")
    print(f"Perda maquina.....: {perda_maquina}")

print("RELATÓRIO CONSOLIDADO:")
print(f"Colheita do ano......: {producao_total}")
print("Projeção de desperdicio:")
print(f"Manual.................: {perda_manual_total}")
print(f"Com máquina.............: {perda_maquina_total}")
