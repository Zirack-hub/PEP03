from personaje import *
import json, os, traceback



def main ():
    diccionario_hechizos = {
                            "Bola de fuego": (18, 5),
                            "Rayo": (32 , 7),
                            }
    espada = Arma("Espada larga", 20)
    alabarda = Arma("Alabarda", 25)
    mandoble = Arma("Mandoble", 30)
    listaArmas = [espada, alabarda, mandoble]

    mago = Mago("Merlin", 80, diccionario_hechizos)
    guerrero = Guerrero("TINA CHIKITNA", 100, listaArmas)
    arquero = Arquero("Legolas", 90)
    personajes = [mago, guerrero, arquero]

    while True:
        print("---MENU----")
        print("1-Crear Personaje")
        print("2-Realizar Batalla")
        print("3-Empezar TCT")
        print("4-Salir")
        print("5-Mostrar Personajes")   
        print("----------------")
        
        opcion = input("Introduce el numero de tu seleccion: ").strip()
        
        if opcion == "1":
            print("Crear Personaje")
            nuevo_personaje = creacion_personaje()
            if nuevo_personaje:
                personajes.append(nuevo_personaje)
        elif opcion == "2":
            print("Realizar Batalla")
            batalla(personajes)
            break
        elif opcion == "3":
            print("Empezar TCT")
            participantes = seleccionar_aleatorios(personajes)
            tct(*participantes)
            
            break
        elif opcion == "4":
            crear_Json(personajes)
        elif opcion == "5":  # Mostrar personajes
            mostrar_personajes(personajes)
        else:
            print("Opción no válida")


def seleccionar_aleatorios(personajes, cantidad=3):
    if cantidad > len(personajes):
        raise ValueError("No hay suficientes personajes en la lista")
    return random.sample(personajes, cantidad)

def batalla(personajes):
    print("selecciona 2 personajes")
    mostrar_personajes(personajes)
    p1 = input("Introduce el primer personaje: ")
    p2 = input("Introduce el primer personaje: ")
    combatiente1 = pj_nombre(personajes, p1)
    combatiente2 = pj_nombre(personajes, p2)

    combate(combatiente1, combatiente2)

def pj_nombre(personajes, nombre):
    for personaje in personajes:
        if personaje.nombre.lower() == nombre.lower():
            return personaje


def crear_Json(personajes):
    try:
        with open("./ficheros/personajesCopia.json", "w", encoding="utf-8") as f:
            hola = json.dump(personajes, f, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)

        print("escrito en:", os.path.abspath("./ficheros/personajesCopia.json"))
        print("tamaño bytes:", os.path.getsize("./ficheros/personajesCopia.json"))
        print(hola)
        f.close()
    except Exception:
        traceback.print_exc()

   
def creacion_personaje():
    diccionario_hechizos = {
                            "Bola de fuego": (18, 5),
                            "Rayo": (32 , 7),
                            }
    espada = Arma("Espada larga", 20)
    alabarda = Arma("Alabarda", 25)
    mandoble = Arma("Mandoble", 30)
    listaArmas = [espada, alabarda, mandoble]
    print("---MENU----")
    print("1-Guerrero")
    print("2-Mago")
    print("3-Arquero")
    opcion = input("Introduce el numero de tu seleccion: ")
    if opcion == "1":
        print("Has elegido Guerrero")
        nombre = input("Introduce el nombre de tu personaje: ").strip()
        guerrero_creacion = Guerrero(nombre, 100, listaArmas)
        return guerrero_creacion
    elif opcion == "2":
        print("Has elegido Mago")
        nombre = input("Introduce el nombre de tu personaje: ").strip()
        mago_creacion = Mago(nombre, 80, diccionario_hechizos)
        return mago_creacion
    elif opcion == "3":
        print("Has elegido Arquero")
        nombre = input("Introduce el nombre de tu personaje: ").strip()
        arquero_creacion = Arquero(nombre, 90)
        return arquero_creacion
    else:
        print("Opción no válida")
        return None
    



def mostrar_personajes(personajes):
    if not personajes:
        print("No hay personajes creados.")
        return

    print("---LISTA DE PERSONAJES---")
    for i, p in enumerate(personajes, start=1):
        # Información básica
        info = f"{i}- {p.nombre} ({p.__class__.__name__}) | Vida: {p.vida} | Estado: {'Vivo' if p.vivo else 'Muerto'}"

        # Información específica según tipo
        if isinstance(p, Guerrero):
            try:
                info += f" | Arma actual: {p.arma.nombre}"
            except AttributeError:
                info += " | Arma actual: Sin arma"

        elif isinstance(p, Mago):
            # Mostrar hechizos de manera segura
            hechizos_list = []
            if p.diccionario_hechizos:
                for k, v in p.diccionario_hechizos.items():
                    try:
                        danio = v[0]
                        mana = v[1]
                        hechizos_list.append(f"{k}({danio} dmg, {mana} mana)")
                    except (TypeError, IndexError):
                        hechizos_list.append(f"{k}(datos inválidos)")
                hechizos = ', '.join(hechizos_list)
            else:
                hechizos = "Sin hechizos"
            info += f" | Hechizos: {hechizos} | Mana: {getattr(p, 'mana', 'N/A')}"

        elif isinstance(p, Arquero):
            info += f" | Puntería: {getattr(p, 'punteria', 'N/A')}"

        print(info)
    print("-------------------------")





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



def tct(p1, p2, p3):
    turno = 1

    while sum(p.vivo for p in (p1, p2, p3)) >= 2:
        print(f"\n--- Turno {turno} ---")

        if p1.vivo:
            objetivos = [p for p in (p2, p3) if p.vivo]
            if objetivos:
                objetivo = random.choice(objetivos)
                p1.atacar(objetivo)
                print(f"{objetivo.nombre} queda con {objetivo.vida}\n")

        if p2.vivo:
            objetivos = [p for p in (p1, p3) if p.vivo]
            if objetivos:
                objetivo = random.choice(objetivos)
                p2.atacar(objetivo)
                print(f"{objetivo.nombre} queda con {objetivo.vida}\n")

        if p3.vivo:
            objetivos = [p for p in (p1, p2) if p.vivo]
            if objetivos:
                objetivo = random.choice(objetivos)
                p3.atacar(objetivo)
                print(f"{objetivo.nombre} queda con {objetivo.vida}\n")

        turno += 1

    print("\n--- FIN DEL COMBATE ---\n")
    vivos = [p for p in (p1, p2, p3) if p.vivo]
    vencedor = vivos[0] if vivos else None

    if vencedor:
        print(f"🏆 {vencedor.nombre} gana con {vencedor.vida} de vida restante.")


#mago = Mago("Merlin", 80, diccionario_hechizos)
#guerrero = Guerrero("TINA CHIKITNA", 100, listaArmas)
#arquero = Arquero("Legolas", 90)
#
#
#
#tct(mago, guerrero, arquero)

if __name__ == "__main__":
    main()