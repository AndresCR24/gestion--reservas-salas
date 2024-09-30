
class Sala:
    id_counter = 0
    tipo_sala = ["Pequeña", "Mediana", "Grande"]
    nombre_sala = ""
    capacidad_maxima = [5, 10, 15]
    tarifa_por_hora = [100, 200, 300]  # Ejemplos de tarifas por hora

    def __init__(self, nombre_sala, tipo_sala):
        self.id = Sala.id_counter
        Sala.id_counter += 1
        self.nombre_sala = nombre_sala
        if tipo_sala in Sala.tipo_sala:
            self.tipo_sala = tipo_sala  # Asignar tipo_sala a la instancia
            index = Sala.tipo_sala.index(tipo_sala)
            self.capacidad_maxima = Sala.capacidad_maxima[index]
            self.tarifa_por_hora = Sala.tarifa_por_hora[index]
            self.tarifa_acumulada = 0
        else:
            raise ValueError(f"Tipo de sala '{tipo_sala}' no válido. Debe ser uno de {Sala.tipo_sala}.")
        self.estado = "Disponible"

    def __str__(self):
        return (f"Sala {self.nombre_sala} ({self.tipo_sala}) con capacidad para "
                f"{self.capacidad_maxima} personas. Estado: {self.estado}")

    def reservar(self):
        self.estado = "Reservada"

    def liberar(self):
        self.estado = "Disponible"

    def mantenimento(self):
        self.estado = "Mantenimiento"
"""
# Modificacion de la clase para restar dinero al quitar una reserva
class Sala:
    id_counter = 0
    tipos_sala = ["Pequeña", "Mediana", "Grande"]
    capacidades_maximas = [5, 10, 15]
    tarifas_por_hora = [100, 200, 300]  # Ejemplos de tarifas por hora

    def __init__(self, nombre_sala, tipo_sala):
        self.id = Sala.id_counter
        Sala.id_counter += 1
        self.nombre_sala = nombre_sala

        if tipo_sala in Sala.tipos_sala:
            self.tipo_sala = tipo_sala  # Asignar tipo_sala a la instancia
            index = Sala.tipos_sala.index(tipo_sala)
            self.capacidad_maxima = Sala.capacidades_maximas[index]
            self.tarifa_por_hora = Sala.tarifas_por_hora[index]
            self.tarifa_actual = 0  # Nuevo atributo para almacenar la tarifa de la reserva
        else:
            raise ValueError(f"Tipo de sala '{tipo_sala}' no válido. Debe ser uno de {Sala.tipos_sala}.")

        self.estado = "Disponible"

    def __str__(self):
        return (f"Sala {self.nombre_sala} ({self.tipo_sala}) con capacidad para "
                f"{self.capacidad_maxima} personas. Estado: {self.estado}")

    def reservar(self, horas):
        self.estado = "Reservada"
        self.tarifa_actual = self.tarifa_por_hora * horas  # Almacena la tarifa de la reserva
        return self.tarifa_actual

    def liberar(self):
        self.estado = "Disponible"
        self.tarifa_actual = 0  # Reinicia la tarifa cuando se libera

    def mantenimiento(self):
        self.estado = "Mantenimiento"
"""
