from lista_enlazada import LinkedList
from Sala import Sala

class Operaciones:
    def __init__(self):
        self.lista_salas = LinkedList()

    def agregar_sala(self):
        nueva_sala = Sala()
        self.lista_salas.append(nueva_sala)
        print(f"Sala agregada: {nueva_sala.nombre_sala}, ID: {nueva_sala.id}")

    def reservar(self, sala_id):
        for sala in self.lista_salas:
            if sala.value.id == sala_id:
                sala.value.reservar()
                print(f"Sala {sala_id} reservada.")
                return
        print(f"Sala {sala_id} no encontrada.")

    def liberar(self, sala_id):
        for sala in self.lista_salas:
            if sala.value.id == sala_id:
                sala.value.liberar()
                print(f"Sala {sala_id} liberada.")
                return
        print(f"Sala {sala_id} no encontrada.")

    def eliminar_sala(self, sala_id):
        index = 0
        for sala in self.lista_salas:
            if sala.value.id == sala_id:
                self.lista_salas.remove(index)
                print(f"Sala {sala_id} eliminada.")
                return
            index += 1
        print(f"Sala {sala_id} no encontrada.")

    def buscar_salas_por_capacidad(self, capacidad):
        salas_encontradas = []
        for sala in self.lista_salas:
            if sala.value.capacidad_maxima == capacidad:
                salas_encontradas.append(sala.value)
        if salas_encontradas:
            print(f"Salas encontradas con capacidad para {capacidad} personas:")
            for sala in salas_encontradas:
                print(sala)
        else:
            print(f"No se encontraron salas con capacidad para {capacidad} personas.")
        return salas_encontradas

    def listar_salas(self):
        print("Lista de todas las salas:")
        for sala in self.lista_salas:
            print(sala.value)