#Crea dos conjuntos A y B con números.
#Muestra la unión (A | B), la intersección (A & B), la diferencia (A - B) y la
#diferencia simétrica (A ^ B).
#Repite las operaciones usando los métodos union(), intersection(),
#difference() y symmetric_difference()
conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}
print("Union (A | B):", conjunto_A | conjunto_B)
print("Intersección (A & B):", conjunto_A & conjunto_B)
print("Diferencia (A - B):", conjunto_A - conjunto_B)
print("Diferencia simétrica (A ^ B):", conjunto_A ^ conjunto_B)
print("Union (A.union(B)):", conjunto_A.union(conjunto_B))
print("Intersección (A.intersection(B)):", conjunto_A.intersection(conjunto_B))
print("Diferencia (A.difference(B)):", conjunto_A.difference(conjunto_B))
print("Diferencia simétrica (A.symmetric_difference(B)):", conjunto_A.symmetric_difference(conjunto_B))
