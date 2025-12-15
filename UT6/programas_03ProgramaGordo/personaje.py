from abc import ABC, abstractmethod
import random

# Clase base
class Personaje(ABC):
    def __init__(self, nombre, vida):
        self._nombre = nombre
        self._vida = vida
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, nueva_vida):
        self._vida = max(0, nueva_vida)
    
    @property
    def vivo(self):
        return self._vida > 0
    
    @abstractmethod
    def atacar(self, objetivo):
        raise NotImplementedError
    
    #def to_dict(self):
    #    result = {"tipo": self.__class__.__name__, "nombre": self.nombre, "vida": self.vida}
    #    
    #    # Guerrero: serializa arsenal y arma actual
    #    if isinstance(self, Guerrero):
    #        result["arma_actual"] = {"nombre": self.arma.nombre, "danio": self.arma.danio}
    #        result["arsenal"] = [{"nombre": arma.nombre, "danio": arma.danio} for arma in self.arsenal]
    #    
    #    # Mago: serializa maná y hechizos
    #    elif isinstance(self, Mago):
    #        result["mana"] = self.mana
    #        # Convertimos los hechizos a lista de diccionarios
    #        result["hechizos"] = [{"nombre": h, "danio": v[0], "coste_mana": v[1]} for h, v in self.diccionario_hechizos.items()]
    #    
    #    # Arquero: serializa puntería
    #    elif isinstance(self, Arquero):
    #        result["punteria"] = self.punteria
    #    
    #    elif isinstance(self, Arma):
    #    
    #    return result
    #    

    
    

# Clase Arma
class Arma:
    def __init__(self, nombre, danio):
        self._nombre = nombre
        self._danio = danio
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def danio(self):
        return self._danio

# Guerrero
class Guerrero(Personaje):
    def __init__(self, nombre, vida, arsenal):
        super().__init__(nombre, vida)
        self.arsenal = arsenal
        self._arma = random.choice(self.arsenal)
    
    @property
    def arma(self):
        return self._arma
    @arma.setter
    def arma(self, nueva_arma):
        self._arma = nueva_arma
    
    def atacar(self, objetivo):
        danio = self.arma.danio + random.randint(0, 3)
        objetivo.vida -= danio  # ⚠️ usamos la propiedad, no _vida
        print(f"{self.nombre} golpea con {self.arma.nombre} y causa {danio} de daño.")
        self.cambiar_arma()
    
    def cambiar_arma(self):
        armas = [arma for arma in self.arsenal]
        self.arma = random.choice(armas)
        print(f"{self.nombre} ha cambiado de arma y ahora va a pegarte con: {self.arma.nombre}")

    def to_dict(self):
        return{
            "tipo": self.__class__.__name___,
            "nombre": self.nombre,
            "vida": self.vida
        }

# Mago
class Mago(Personaje):
    def __init__(self, nombre, vida, diccionario_hechizos, mana=100):
        super().__init__(nombre, vida)
        self._mana = mana
        self._diccionario_hechizos = diccionario_hechizos
    
    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, nuevo_mana):
        self._mana = nuevo_mana
    
    @property
    def diccionario_hechizos(self):
        return self._diccionario_hechizos
    
    def atacar(self, objetivo):
        hechizo = random.choice(list(self.diccionario_hechizos.keys()))
        danio, coste_mana = self.diccionario_hechizos[hechizo]

        if self.mana < coste_mana:
            print(f"{self.nombre} no tiene suficiente maná para lanzar {hechizo}.")
            return
        
        objetivo.vida -= danio  # ⚠️ usamos la propiedad, no _vida
        self.mana -= coste_mana  # ⚠️ usamos la propiedad, no _mana
        
        print(f"{self.nombre} lanza {hechizo} y causa {danio} de daño.")
        print(f"Le quedan {self.mana} de maná")

class Arquero(Personaje):
    def __init__(self, nombre, vida, punteria=10,):
        super().__init__(nombre, vida)
        self._punteria = punteria

    @property
    def punteria(self):
        return self._punteria
    
    @punteria.setter
    def punteria(self, nueva_punteria):
        self._punteria = nueva_punteria
    
    def atacar(self, objetivo):
        danio = self._punteria + random.randint(0, 3)
        objetivo.vida -= danio  # ⚠️ usamos la propiedad, no _vida
        print(f"{self.nombre} apunta con su arco y causa {danio} de daño.")
        self.punteria += 10
