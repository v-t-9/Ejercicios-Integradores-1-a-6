# Sabiendo que ValueError es la excepción que se lanza cuando no podemos 
# convertir una cadena de texto en su valor numérico, escriba una función get_int() 
# que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto.
# Intente resolver el ejercicio tanto de manera iterativa como recursiva.

def get_int():
        try:
            n = int(input("Ingrese un numero entero: "))
            print("El valor es: ", n)
        except ValueError as ve:
            print(str(ve) , ", No es valido. Intente de nuevo. ")
            n = get_int()
       
      
             

       
get_int()

