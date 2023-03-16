# 1. Escribir una función que calcule el máximo común divisor entre dos números

def max_divisor(n1,n2):
  
    while n1 >n2:
        if n1%n2 == 0:
            mcd = n2
            return mcd
        else:
            res = n1/n2
            n3 = int(res)*n2
            n4 = n1 - n3
            n1 = n2
            n2 = n4
    while n1 < n2:
        if n2%n1 == 0:
            mcd = n1
            return mcd
        else:
            res = n2/n1
            n3 = int(res)*n1
            n4 = n2 - n3
            n2 = n1
            n1 = n4
            
# print(max_divisor( 40, 120 ))

#2. Escribir una función que calcule el mínimo común múltiplo entre dos números

def min_multiplo(n1,n2):
    return n1*n2/max_divisor(n1,n2)
print(min_multiplo(40, 120))
