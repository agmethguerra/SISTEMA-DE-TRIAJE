# Clase para representar a cada paciente
class Paciente:
    def __init__(self, nombre, edad, sintomas, gravedad):
        self.nombre = nombre
        self.edad = edad
        self.sintomas = sintomas
        self.gravedad = gravedad
        self.prioridad_edad = self.calcular_prioridad_edad()

    def calcular_prioridad_edad(self):
        if self.edad < 12:
            return 1
        elif self.edad > 65:
            return 2
        else:
            return 3

    def obtener_clave_prioridad(self):
        return (self.gravedad, self.prioridad_edad)

# Nodo de la lista enlazada
class Nodo:
    def __init__(self, paciente):
        self.paciente = paciente
        self.siguiente = None

# Lista enlazada con inserción ordenada por prioridad
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_paciente(self, paciente):
        nuevo_nodo = Nodo(paciente)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            print("\nPaciente ingresado exitosamente. Posición en la cola: 1\n")
            return

        actual = self.cabeza
        anterior = None
        posicion = 1

        while actual:
            if paciente.obtener_clave_prioridad() < actual.paciente.obtener_clave_prioridad():
                break
            anterior = actual
            actual = actual.siguiente
            posicion += 1

        if anterior is None:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            anterior.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = actual

        print(f"\nPaciente ingresado exitosamente. Posición en la cola: {posicion}\n")

    def pasar_siguiente(self):
        if not self.cabeza:
            print("\nNo hay pacientes en la cola.\n")
            return

        paciente = self.cabeza.paciente
        self.cabeza = self.cabeza.siguiente

        print("\n--- SIGUIENTE PACIENTE EN SER ATENDIDO ---")
        print(f"Nombre    : {paciente.nombre}")
        print(f"Edad      : {paciente.edad}")
        print(f"Síntomas  : {paciente.sintomas}")
        print(f"Prioridad : Gravedad {paciente.gravedad}, Categoría Edad {paciente.prioridad_edad}")
        print("-------------------------------------------\n")

    def mostrar_cola(self):
        if not self.cabeza:
            print("\nNo hay pacientes en la cola.\n")
            return

        print("\n--- COLA DE PACIENTES ---")
        actual = self.cabeza
        posicion = 1
        while actual:
            paciente = actual.paciente
            print(f"{posicion}. {paciente.nombre} | Edad: {paciente.edad} | "
                  f"Síntomas: {paciente.sintomas} | Prioridad: G{paciente.gravedad}-E{paciente.prioridad_edad}")
            actual = actual.siguiente
            posicion += 1
        print("---------------------------\n")

# Funciones para desplegar el menu
def mostrar_menu():
    print("----- SERVICIO MÉDICO DOMICILIARIO X -----")
    print("1. Ingresar Paciente")
    print("2. Pasar siguiente paciente")
    print("3. Mostrar la cola")
    print("4. Salir")

def ejecutar_programa():
    lista = ListaEnlazada()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre completo del paciente: ")
            edad = int(input("Ingrese la edad del paciente: "))
            sintomas = input("Ingrese los síntomas o motivo de consulta: ")
            while True:
                gravedad = int(input("Ingrese la gravedad (1 a 5, donde 1 es la mayor gravedad): "))
                if 1 <= gravedad <= 5:
                    break
                print("Gravedad inválida. Debe estar entre 1 y 5.")
            paciente = Paciente(nombre, edad, sintomas, gravedad)
            lista.insertar_paciente(paciente)

        elif opcion == "2":
            lista.pasar_siguiente()

        elif opcion == "3":
            lista.mostrar_cola()

        elif opcion == "4":
            print("Saliendo del programa. ¡Gracias!")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")

ejecutar_programa()
