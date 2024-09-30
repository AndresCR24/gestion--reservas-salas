from operaciones import Operaciones

if __name__ == "__main__":
    # Crear una instancia de Operaciones
    operaciones = Operaciones()

    # Agregar algunas salas
    operaciones.agregar_sala("Sala A", "Pequeña")
    operaciones.agregar_sala("Sala B", "Mediana")
    operaciones.agregar_sala("Sala C", "Grande")
    operaciones.agregar_sala("Sala D", "Pequeña")
    operaciones.agregar_sala("Sala E", "Grande")

    # Imprimir la lista de salas para verificar
    print("Lista de salas después de agregar:")
    operaciones.listar_salas()

    # Reservar una sala
    operaciones.reservar(1)
    print("Estado de la sala 1 después de reservar:")
    for sala in operaciones.lista_salas:
        if sala.value.id == 1:
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