# La palabra "continue" se usa para ejecutar la siguiente acción a la que se le ha dado al ciclo
for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')