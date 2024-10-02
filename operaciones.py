from lista_enlazada import LinkedList
from Sala import Sala

import csv

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
    """
    # Se trato de corregir que se restara el dinero si se cancelaba la reserva
    def reservar(self, sala_id, horas):
        for sala in self.lista_salas:
            if sala.value.id == sala_id:
                if sala.value.estado == "Disponible":
                    sala.value.reservar(horas)
                    print(f"Sala {sala_id} reservada por {horas} horas.")
                    return
                else:
                    print(f"La sala {sala_id} no está disponible.")
                    return
        print(f"Sala {sala_id} no encontrada.")
    """
    def liberar(self, sala_id):
        for sala in self.lista_salas:
            if sala.value.id == sala_id:
                sala.value.liberar()
                print(f"Sala {sala_id} liberada.")
                return
        print(f"Sala {sala_id} no encontrada.")

    def mantenimiento(self, sala_id):
        for sala in self.lista_salas:
            if sala.value.id == sala_id:
                sala.value.mantenimento()
                print(f"Sala {sala_id} en mantenimiento.")
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

    def reservar_por_tipo(self, tipo_sala, horas=1):
        for sala in self.lista_salas:
            if sala.value.tipo_sala == tipo_sala and sala.value.estado == "Disponible":
                sala.value.reservar()
                tarifa = sala.value.tarifa_por_hora * horas
                if horas > 8:
                    tarifa *= 0.85  # Aplicar 15% de descuento
                self.ingresos_totales += tarifa
                print(f"Sala {sala.value.id} de tipo {tipo_sala} reservada por {horas} horas. Tarifa: {tarifa}")
                return
        print(f"No hay salas disponibles de tipo {tipo_sala}.")

    def modificar_reserva(self, sala_id, nuevo_tipo_sala=None, horas=1):
        for sala in self.lista_salas:
            if sala.value.id == sala_id:
                if nuevo_tipo_sala:
                    self.liberar(sala_id)
                    self.reservar_por_tipo(nuevo_tipo_sala, horas)
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


    """
    def intercambiar_salas_mantenimiento(self, sala_id):
        sala_mantenimiento = None
        for sala in self.lista_salas:
            if sala.value.id == sala_id and sala.value.estado == "Mantenimiento":
                sala_mantenimiento = sala
                break

        if not sala_mantenimiento:
            print(f"Sala {sala_id} no está en mantenimiento o no existe.")
            return

        for sala in self.lista_salas:
            if (sala.value.capacidad_maxima == sala_mantenimiento.value.capacidad_maxima and
                    sala.value.tipo_sala == sala_mantenimiento.value.tipo_sala and
                    sala.value.estado != "Mantenimiento"):
                # Intercambiar los nodos
                sala_mantenimiento.value, sala.value = sala.value, sala_mantenimiento.value
                print(f"Sala {sala_id} intercambiada con sala {sala.value.id}.")
                return

    """

    def intercambiar_salas_mantenimiento(self, sala_id):
        # Encontrar la sala en mantenimiento
        nodo_anterior_mantenimiento = None
        nodo_mantenimiento = None

        anterior = None
        for sala in self.lista_salas:
            if sala.value.id == sala_id and sala.value.estado == "Mantenimiento":
                nodo_anterior_mantenimiento = anterior
                nodo_mantenimiento = sala
                break
            anterior = sala

        if not nodo_mantenimiento:
            print(f"Sala {sala_id} no está en mantenimiento o no existe.")
            return

        # Buscar una sala con las mismas características para intercambiar
        nodo_anterior_candidato = None
        nodo_candidato = None
        anterior = None
        for sala in self.lista_salas:
            if (sala.value.capacidad_maxima == nodo_mantenimiento.value.capacidad_maxima and
                    sala.value.tipo_sala == nodo_mantenimiento.value.tipo_sala and
                    sala.value.estado != "Mantenimiento"):
                nodo_anterior_candidato = anterior
                nodo_candidato = sala
                break
            anterior = sala

        if not nodo_candidato:
            print("No se encontró una sala con las mismas características para intercambiar.")
            return

        # Intercambiar los nodos en la lista enlazada
        if nodo_anterior_mantenimiento:
            nodo_anterior_mantenimiento.next = nodo_candidato
        else:
            self.lista_salas.head = nodo_candidato  # Si es la primera sala en la lista

        if nodo_anterior_candidato:
            nodo_anterior_candidato.next = nodo_mantenimiento
        else:
            self.lista_salas.head = nodo_mantenimiento  # Si es la primera sala en la lista

        # Intercambiar las referencias next
        nodo_mantenimiento.next, nodo_candidato.next = nodo_candidato.next, nodo_mantenimiento.next

        print(f"Sala {nodo_mantenimiento.value.id} intercambiada con sala {nodo_candidato.value.id}.")

    """
    def reorganizar_salas_por_capacidad(self):
        if self.lista_salas.length < 2:
            print("No hay suficientes salas para reorganizar.")
            return

        # Convertir la lista enlazada a una lista de Python para facilitar la ordenación
        salas = []
        for sala in self.lista_salas:
            salas.append(sala.value)

        # Ordenar las salas por capacidad máxima de mayor a menor
        salas.sort(key=lambda x: x.capacidad_maxima, reverse=True)

        # Reconstruir la lista enlazada con las salas ordenadas
        self.lista_salas.delete()
        for sala in salas:
            self.lista_salas.append(sala)

        print("Salas reorganizadas por capacidad máxima.") 
    """
    def reorganizar_salas_por_capacidad(self):
        if self.lista_salas.length < 2:
            print("No hay suficientes salas para reorganizar.")
            return

        for i in range(self.lista_salas.length - 1):
            current = self.lista_salas.head
            next_node = current.next
            for j in range(self.lista_salas.length - 1 - i):
                if current.value.capacidad_maxima < next_node.value.capacidad_maxima:
                    current.value, next_node.value = next_node.value, current.value
                current = next_node
                next_node = next_node.next

        print("Salas reorganizadas por capacidad máxima.")

    def listar_salas_reservadas_por_tipo(self, tipo_sala):
        print(f"Salas reservadas de tipo {tipo_sala}:")
        for sala in self.lista_salas:
            if sala.value.tipo_sala == tipo_sala and sala.value.estado == "Reservada":
                print(sala.value)
    """
    guia rapida para implementacion del codigo
    def reservar_varias_salas(self, tipo_sala = "Grande", horas=1, cantidad = 1):
        for sala in self.lista_salas:
            if sala.value.tipo_sala == tipo_sala:
                sala.value.reservar()
                tarifa = sala.value.tarifa_por_hora * horas
                if horas > 8:
                    tarifa *= 0.85  # Aplicar 15% de descuento
                self.ingresos_totales += tarifa
                print(f"Sala {sala.value.id} reservada por {horas} horas. Tarifa: {tarifa}")

                if cantidad == 2:
                    tarifa *= 0.90
                    self.ingresos_totales += tarifa
                    print(f"Nuevo valor de reserva al reservar 2 salas: {tarifa}")
                elif cantidad == 3:
                    tarifa *= 0.85
                    self.ingresos_totales += tarifa
                    print(f"Nuevo valor de reserva al reservar 3 salas: {tarifa}")
                elif cantidad > 3:
                    tarifa *= 0.80
                    self.ingresos_totales += tarifa
                    print(f"Nuevo valor de reserva al reservar más de 3 salas: {tarifa}")
                return

        print("No hay suficientes salas de tipo 'Grande' para reservar")
    """
    def reservar_varias_salas(self, horas=1, cantidad=1):
        salas_reservadas = 0
        tipo_sala = "Grande"

        for sala in self.lista_salas:
            if sala.value.tipo_sala == tipo_sala and sala.value.estado == "Disponible":
                sala.value.reservar()
                tarifa = sala.value.tarifa_por_hora * horas
                if horas > 8:
                    tarifa *= 0.85

                if cantidad == 2:
                    tarifa *= 0.90
                elif cantidad == 3:
                    tarifa *= 0.85
                elif cantidad > 3:
                    tarifa *= 0.80

                self.ingresos_totales += tarifa
                salas_reservadas += 1
                print(f"Sala {sala.value.id} reservada por {horas} horas. Tarifa: {tarifa}")

                if salas_reservadas == cantidad:
                    return

        if salas_reservadas < cantidad:
            print(f"No hay suficientes salas de tipo '{tipo_sala}' disponibles para reservar {cantidad} salas.")

    # DE chat GPT
    def cargar_salas_desde_csv(self, archivo_csv):
        with open(archivo_csv, mode='r') as file:
            reader = csv.reader(file)
            for fila in reader:
                nombre_sala = fila[0]
                tipo_sala = fila[1]
                self.agregar_sala(nombre_sala, tipo_sala)
        print("Salas cargadas desde el archivo CSV.")