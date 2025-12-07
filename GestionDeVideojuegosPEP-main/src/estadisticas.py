
# Cáculo de Estadísticas

# -------- CÁCULO DE ESTADÍSTICAS --------------------------------
def estadisticas(catalogo):
    print("\n=== Estadísticas ===")
    print("Número total de juegos:", len(catalogo))
    conteo_generos = {}
    for datos in catalogo.values():
        for g in datos["genero"]:
            if g not in conteo_generos:
                conteo_generos[g] = 1
            else:
                conteo_generos[g] += 1
    print("Conteo por género:")
    for g, cantidad in conteo_generos.items():
        print("-", g, ":", cantidad)