from operaciones import Operaciones
from menu import Menu
if __name__ == "__main__":
    menu = Menu()
    menu.ejecutar()
    """"
    # Crear una instancia de Operaciones
    operaciones = Operaciones()

    # Agregar algunas salas
    operaciones.agregar_sala("Sala A", "Pequeña")
    operaciones.agregar_sala("Sala B", "Mediana")
    operaciones.agregar_sala("Sala C", "Grande")
    operaciones.agregar_sala("Sala D", "Pequeña")
    operaciones.agregar_sala("Sala E", "Grande")
    operaciones.agregar_sala("Sala F", "Mediana")
    #operaciones.agregar_sala("Sala G", "Grande")

    # Imprimir la lista de salas para verificar
    print("Lista de salas después de agregar:")
    operaciones.listar_salas()

    # Reservar una sala
    operaciones.reservar(1, horas=5)
    print("Estado de la sala 1 después de reservar por 5 horas:")
    for sala in operaciones.lista_salas:
        if sala.value.id == 1:
            print(sala.value.estado)

    # Reservar una sala por más de 8 horas para aplicar descuento
    operaciones.reservar(2, horas=10)
    print("Estado de la sala 2 después de reservar por 10 horas:")
    for sala in operaciones.lista_salas:
        if sala.value.id == 2:
            print(sala.value.estado)

    # Liberar una sala
    operaciones.liberar(1)
    print("Estado de la sala 1 después de liberar:")
    for sala in operaciones.lista_salas:
        if sala.value.id == 1:
            print(sala.value.estado)

    # Buscar salas por capacidad
    capacidad = 10
    print(f"Buscando salas con capacidad para {capacidad} personas:")
    operaciones.buscar_salas_por_capacidad(capacidad)

    # Eliminar una sala
    operaciones.eliminar_sala(1)
    print("Lista de salas después de eliminar la sala con ID 1:")
    operaciones.listar_salas()

    # Reservar una sala por tipo
    operaciones.reservar_por_tipo("Pequeña", horas=3)
    print("Lista de salas después de reservar una sala de tipo 'Pequeña':")
    operaciones.listar_salas()

    # Modificar una reserva
    operaciones.modificar_reserva(2, nuevo_tipo_sala="Grande", horas=4)
    print("Lista de salas después de modificar la reserva de la sala con ID 2:")
    operaciones.listar_salas()

    # Cancelar una reserva
    operaciones.cancelar_reserva(2)
    print("Lista de salas después de cancelar la reserva de la sala con ID 2:")
    operaciones.listar_salas()

    # Calcular ingresos por reservas
    print("Ingresos totales por reservas:")
    operaciones.calcular_ingresos()

    # Intercambiar salas en mantenimiento
    print("---------------------------")
    print("Salas antes del cambio: ")
    operaciones.listar_salas()
    operaciones.mantenimiento(3)
    operaciones.intercambiar_salas_mantenimiento(3)
    print("Lista de salas después de intentar intercambiar la sala con ID 3:")
    operaciones.listar_salas()

    # Reorganizar las salas por capacidad
    operaciones.reorganizar_salas_por_capacidad()
    print("Lista de salas después de reorganizar por capacidad:")
    operaciones.listar_salas()

    # Listar salas reservadas por tipo
    print("Listar salas reservadas de tipo 'Grande':")
    operaciones.listar_salas_reservadas_por_tipo("Grande")
    """