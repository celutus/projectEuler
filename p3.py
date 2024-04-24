"""
Largest Prime Factor

The prime factor of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import math
from functions_file import prime_factors, prime_number

# What is the largest prime factor of the number 600651475143
# Yo he hecho una función que calcula todos los prime_factors, pero lo más fácil es simplemente buscar ese más alto
#Sobre todo porque para números de 7 cifras se queda pensando y no da resultado

#he puesto if(num == 1): final = True en la función prime_factos pero aún así sigue sin salir respuesta, debería salir, son pocos cálculos
#también se me ocurrió que la lista prime_numbers dentro de la función prime_factors la podría reducir a los números de la lista
#menores iguales a 1 + la raiz del número, pero con lo de final = True cortaría antes que ocurra lo de la raiz

# print(prime_factors(600851475143))
num = 600851475143
for i in range(math.floor(math.sqrt(num)) + 1, 2, -1):
	if(num % i == 0): #
		if(prime_number(i)):
			print(i)

#486847 multiplo de 6857 y 71
#104441 multiplo también
#59569 multiplo
#6857 prime number -> Este es el más alto
#1471 prime number
#839 prime number
#71 prime number