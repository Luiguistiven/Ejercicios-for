#Práctica Loop For 3


lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4] 
suma_pares = 0
suma_impares = 0

for num in lista_numeros:
    if num % 2 == 0:
        suma_pares += num
    else:
        suma_impares += num

print("suma de numero pares:", suma_pares)
print("suma de numero impares:", suma_impares)