from lista_enlazada import LinkedList
from Sala import Sala

class Operaciones:
    def __init__(self):
        self.lista_salas = LinkedList()
        self.ingresos_totales = 0

    def agregar_sala(self, nombre_sala, tipo_sala):
        nueva_sala = Sala(nombre_sala, tipo_sala)
        self.lista_salas.append(nueva_sala)
        print(f"Sala agregada: {nueva_sala.nombre_sala}, ID: {nueva_sala.id}")

    """
    def reservar(self, sala_id):
        for sala in self.lista_salas:
            if sala.value.id == sala_id:
                sala.value.reservar()
                print(f"Sala {sala_id} reservada.")
                return
        print(f"Sala {sala_id} no encontrada.")
    """
    def reservar(self, sala_id, horas=1):
        for sala in self.lista_salas:
            if sala.value.id == sala_id:
                sala.value.reservar()
                tarifa = sala.value.tarifa_por_hora * horas
                if horas > 8:
                    tarifa *= 0.85  # Aplicar 15% de descuento
                self.ingresos_totales += tarifa
                print(f"Sala {sala_id} reservada por {horas} horas. Tarifa: {tarifa}")
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
            if sala.value.capacidad_maxima >= capacidad:
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
            print(sala.value, "Numero de la sala: ", sala.value.id)

    def listar_salas_disponibles(self):
        print("Salas disponibles para reserva:")
        for sala in self.lista_salas:
            if sala.value.estado == "Disponible":
                print(sala.value, f"Tarifa por hora: {sala.value.tarifa_por_hora}")

    def listar_salas_reservadas(self):
        print("Salas reservadas:")
        for sala in self.lista_salas:
            if sala.value.estado == "Reservada":
                print(sala.value)

    def reservar_por_tipo(self, tipo_sala):
        for sala in self.lista_salas:
            if sala.value.tipo_sala == tipo_sala and sala.value.estado == "Disponible":
                sala.value.reservar()
                print(f"Sala {sala.value.id} de tipo {tipo_sala} reservada.")
                return
        print(f"No hay salas disponibles de tipo {tipo_sala}.")

    def modificar_reserva(self, sala_id, nuevo_tipo_sala=None):
        for sala in self.lista_salas:
            if sala.value.id == sala_id:
                if nuevo_tipo_sala:
                    self.liberar(sala_id)
                    self.reservar_por_tipo(nuevo_tipo_sala)
                else:
                    print(f"No se especificó un nuevo tipo de sala para la reserva {sala_id}.")
                return
        print(f"Sala {sala_id} no encontrada.")

    def cancelar_reserva(self, sala_id):
        for sala in self.lista_salas:
            if sala.value.id == sala_id:
                sala.value.liberar()
                print(f"Reserva de la sala {sala_id} cancelada.")
                return
        print(f"Sala {sala_id} no encontrada.")

    def calcular_ingresos(self):
        print(f"Ingresos totales por reservas: {self.ingresos_totales}")
        return self.ingresos_totales