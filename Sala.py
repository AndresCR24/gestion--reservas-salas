class Sala:
    id_counter = 0
    tipo_sala = ["Pequeña", "Mediana", "Grande"]
    capacidad_maxima = [5, 10, 15]
    tarifa_por_hora = [100, 200, 300]  # Ejemplo de tarifas por hora

    def __init__(self):
        self.id = Sala.id_counter
        Sala.id_counter += 1
        self.nombre_sala = Sala.tipo_sala[self.id % len(Sala.tipo_sala)]
        self.capacidad_maxima = Sala.capacidad_maxima[self.id % len(Sala.capacidad_maxima)]
        self.tarifa_por_hora = Sala.tarifa_por_hora[self.id % len(Sala.tarifa_por_hora)]
        self.estado = "Disponible"

    def __str__(self):
        return f"Sala {self.nombre_sala} con capacidad para {self.capacidad_maxima} personas"

    def reservar(self):
        self.estado = "Reservada"

    def liberar(self):
        self.estado = "Disponible"