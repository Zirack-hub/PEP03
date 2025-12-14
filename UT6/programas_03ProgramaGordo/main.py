from personaje import *

def combate(p1, p2):
    turno = 1
    while p1.vivo and p2.vivo:
        print(f"\n--- Turno {turno} ---")

        p1.atacar(p2)
        print(f"{p2.nombre} queda con {p2.vida}")    
        if not p2.vivo:
            break

        p2.atacar(p1)
        print(f"{p1.nombre} queda con {p1.vida}")
        turno += 1
    print("\n--- FIN DEL COMBATE ---\n")
    vencedor = p1 if p1.vivo else p2
    print(f"🏆 {vencedor.nombre} gana con {vencedor.vida} de vida restante.")

        

diccionario_hechizos = {
                        "Bola de fuego": (18, 5),
                        "Rayo": (32 , 7),
                        "Descarga de pirofrio": (100, 50)
                        }

mago = Mago("Merlin", 80, diccionario_hechizos)

espada = Arma("Espada larga", 20)
pistola = Arma("UNA FUCKING PISTOLA", 50)
bazoka = Arma("UN FUCKING BAZOKA", 200)
listaArmas = [espada, pistola, bazoka]
guerrero = Guerrero("TINA CHIKITNA", 100, listaArmas)


combate(mago, guerrero)

