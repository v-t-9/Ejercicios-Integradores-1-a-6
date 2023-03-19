# Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.
# Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

# Los getters y setters en general no tienen lógica adicional.
class Persona:
    def __init__(self, nombre = "", edad = "", DNI = ""):
        self.__nom = nombre
        self.__edad = edad
        self.__DNI = DNI
        
    @property
    def nombre(self):
        return self.__nom
    
    @nombre.setter
    def nombre(self, value):
        if len(value) > 20:
            raise ValueError("El nombre no es valido.")
        self.__nom = value

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, value):
        if type(value) is str:
             raise TypeError("La edad debe ser numerica.")
        self.__edad = value
    
    @property
    def DNI(self):
        return self.__DNI
    
    @DNI.setter
    def DNI(self, value):
        if value <100000:
            raise ValueError("Numero de DNI no valido")
        self._DNI = value
    
    def mostrar(self):
        print("Nombre: " , self.__nom , "\nEdad: ", self.__edad, "\nDNI: ", self._DNI )
    
    def es_mayor_de_edad(self):
        if self.__edad >=18:
            return print(True)
        else:
            return print(False)

persona1 = Persona()
persona1.nombre = "Juana"
persona1.edad = 20
persona1.DNI = 30123456
persona1.mostrar()
persona1.es_mayor_de_edad()
persona2 = Persona()
persona2.nombre = ""
persona2.edad = 16
persona2.DNI = 31987654
persona2.mostrar()
persona2.es_mayor_de_edad()