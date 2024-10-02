import sys
from operaciones import Operaciones

class Menu:
    def __init__(self):
        self.operaciones = Operaciones()

    def mostrar_menu(self):
        print("\n--- Menú de Operaciones ---")
        print("1. Agregar sala")
        print("2. Reservar sala")
        print("3. Liberar sala")
        print("4. Buscar salas por capacidad")
        print("5. Eliminar sala")
        print("6. Reservar sala por tipo")
        print("7. Modificar reserva")
        print("8. Cancelar reserva")
        print("9. Calcular ingresos por reservas")
        print("10. Intercambiar salas en mantenimiento")
        print("11. Reorganizar salas por capacidad")
        print("12. Listar salas reservadas por tipo")
        print("13. Listar todas las salas")
        print("14. Poner sala en mantenimiento")
        print("15. Cargar salas desde archivo CSV")
        print("0. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre = input("Ingrese el nombre de la sala: ")
                tipo = input("Ingrese el tipo de sala (Pequeña, Mediana, Grande): ")
                self.operaciones.agregar_sala(nombre, tipo)
            elif opcion == "2":
                sala_id = int(input("Ingrese el ID de la sala a reservar: "))
                horas = int(input("Ingrese la cantidad de horas: "))
                self.operaciones.reservar(sala_id, horas)
            elif opcion == "3":
                sala_id = int(input("Ingrese el ID de la sala a liberar: "))
                self.operaciones.liberar(sala_id)
            elif opcion == "4":
                capacidad = int(input("Ingrese la capacidad mínima: "))
                self.operaciones.buscar_salas_por_capacidad(capacidad)
            elif opcion == "5":
                sala_id = int(input("Ingrese el ID de la sala a eliminar: "))
                self.operaciones.eliminar_sala(sala_id)
            elif opcion == "6":
                tipo = input("Ingrese el tipo de sala a reservar (Pequeña, Mediana, Grande): ")
                horas = int(input("Ingrese la cantidad de horas: "))
                self.operaciones.reservar_por_tipo(tipo, horas)
            elif opcion == "7":
                sala_id = int(input("Ingrese el ID de la sala a modificar: "))
                nuevo_tipo = input("Ingrese el nuevo tipo de sala (Pequeña, Mediana, Grande): ")
                horas = int(input("Ingrese la cantidad de horas: "))
                self.operaciones.modificar_reserva(sala_id, nuevo_tipo, horas)
            elif opcion == "8":
                sala_id = int(input("Ingrese el ID de la sala a cancelar: "))
                self.operaciones.cancelar_reserva(sala_id)
            elif opcion == "9":
                self.operaciones.calcular_ingresos()
            elif opcion == "10":
                sala_id = int(input("Ingrese el ID de la sala en mantenimiento: "))
                self.operaciones.intercambiar_salas_mantenimiento(sala_id)
            elif opcion == "11":
                self.operaciones.reorganizar_salas_por_capacidad()
            elif opcion == "12":
                tipo = input("Ingrese el tipo de sala a listar (Pequeña, Mediana, Grande): ")
                self.operaciones.listar_salas_reservadas_por_tipo(tipo)
            elif opcion == "13":
                self.operaciones.listar_salas()
            elif opcion == "14":
                sala_id = int(input("Ingrese el ID de la sala a poner en mantenimiento: "))
                self.operaciones.mantenimiento(sala_id)
            elif opcion == "15":
                archivo_csv = input("Ingrese el nombre del archivo CSV: ")
                self.operaciones.cargar_salas_desde_csv(archivo_csv)

            elif opcion == "0":
                print("Saliendo...")
                sys.exit()
            else:
                print("Opción no válida. Intente de nuevo.")
