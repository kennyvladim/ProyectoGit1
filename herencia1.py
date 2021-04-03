# LA CLASE ANIMAL ES LA CLASE PADRE O SUPER CLASE

class Animal:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del animal: ")
        self.numero_patas = int(input("Ingrese el número de patas del animal: "))
        self.tamaño = input("Ingrese el tamaño del animal: ")
    
    def mostrarDatos(self):
        print("NOMBRE: ", self.nombre)
        print("NÚMERO DE PATAS: ", self.numero_patas)
        print("TAMAÑO: ", self.tamaño)

# CREANDO OBJETOS DE LA CLASE ANIMAL

perro1 = Animal()
perro1.mostrarDatos()

gato1 = Animal()
gato1.mostrarDatos()

conejo1 = Animal()
conejo1.mostrarDatos()
