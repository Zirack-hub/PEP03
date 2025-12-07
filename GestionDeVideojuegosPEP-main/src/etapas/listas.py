listajuegos=["Expedition 33", "Silksong", "Monster Hunter World", "Elden Ring", "World of Warcraft"]
listajuegos.append("Hogwarts Legacy")
listajuegos.insert(2, "God of War Ragnarok")
listajuegos.remove("Monster Hunter World")

for i in range(len(listajuegos)):
    print(f"Juego {i+1}: {listajuegos[i]}")

listajuegos.sort()

print("Lista de juegos ordenada:")
for juego in listajuegos:
    print(juego)




