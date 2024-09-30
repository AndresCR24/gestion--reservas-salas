from operaciones import Operaciones

if __name__ == "__main__":
    # Crear una instancia de Operaciones
    operaciones = Operaciones()

    # Agregar algunas salas
    operaciones.agregar_sala()
    operaciones.agregar_sala()
    operaciones.agregar_sala()

    # Imprimir la lista de salas para verificar
    print("Lista de salas después de agregar:")
    print(operaciones.lista_salas)

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