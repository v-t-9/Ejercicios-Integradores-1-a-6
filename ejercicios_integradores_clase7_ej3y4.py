# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
# Los diccionarios no permiten claves repetidas.
def string_to_dic(str):
    list1 = str.split(" ")
    dic = dict()
    for i in list1:    
            dic[i] =  list1.count(i) 

    return dic
str1 = "manzana pera manzana frutilla pera pera"
# print(string_to_dic(str1))

# Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). 
# Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

# def dic_to_tup():
#       max = 0 
#       dict = string_to_dic(str1)
#       for i in dict.values():
#         if i>max:
#          max = i
#       lista_values = list(dict.values())
#       lista_keys = list(dict.keys())
#       pos = lista_values.index(max)
#       tup = (lista_keys[pos], max)
#       print(tup)

# dic_to_tup()


def dic_to_tup(func):
      max = 0 
      dict = func
      for i in dict.values():
        if i>max:
         max = i
      lista_values = list(dict.values())
      lista_keys = list(dict.keys())
      pos = lista_values.index(max)
      tup = (lista_keys[pos], max)
      print(tup)

dic_to_tup(string_to_dic(str1))
      