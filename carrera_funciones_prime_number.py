import math
import time
from timeit import timeit

def prime_number(num):
	for i in range(2, math.floor(math.sqrt(num))):
		if(num % i == 0): return False
	return True
def prime_number_2(num):
	i = 2
	while(i <= math.floor(math.sqrt(num))):
		if(num % i == 0): return False
		i += 1
		while(not(prime_number(i))):
			i += 1
	return True
def prime_number_3_semirecursive_intento_fallido(num):
	prime_numbers = [2]
	i = prime_numbers[-1]
	while(i <= math.floor(math.sqrt(num))):
		for j in prime_numbers:
			if(num % j == 0): return False
		i += 1
		while(not(prime_number(i))):
			i += 1
		prime_numbers.append(i)
	return True
def is_divisible_by_this_list(num, list):
	for i in list:
		if(num % i == 0): return True
	return False
def prime_number_3_semirecursive(num):
	prime_numbers = [2]
	i = prime_numbers[-1]
	while(i <= math.floor(math.sqrt(num))):
		if(num % i == 0): return False
		i += 1
		while(is_divisible_by_this_list(i, prime_numbers)):
			i += 1
		prime_numbers.append(i)
	return True





def a_prime_number(num):
	time.sleep(tiempo_de_espera)
	for i in range(2, math.floor(math.sqrt(num))):
		time.sleep(tiempo_de_espera)
		if(num % i == 0):
			time.sleep(tiempo_de_espera)
			return False
		time.sleep(tiempo_de_espera)
	time.sleep(tiempo_de_espera)
	return True
def a_prime_number_2(num):
	time.sleep(tiempo_de_espera)
	i = 2
	time.sleep(tiempo_de_espera)
	while(i <= math.floor(math.sqrt(num))):
		time.sleep(tiempo_de_espera)
		if(num % i == 0):
			time.sleep(tiempo_de_espera)
			return False
		time.sleep(tiempo_de_espera)
		i += 1
		time.sleep(tiempo_de_espera)
		while(not(a_prime_number(i))):
			time.sleep(tiempo_de_espera)
			i += 1
			time.sleep(tiempo_de_espera)
		time.sleep(tiempo_de_espera)
	time.sleep(tiempo_de_espera)
	return True
def a_prime_number_3_semirecursive_intento_fallido(num):
	time.sleep(tiempo_de_espera)
	prime_numbers = [2]
	time.sleep(tiempo_de_espera)
	i = prime_numbers[-1]
	time.sleep(tiempo_de_espera)
	while(i <= math.floor(math.sqrt(num))):
		time.sleep(tiempo_de_espera)
		for j in prime_numbers:
			time.sleep(tiempo_de_espera)
			if(num % j == 0):
				time.sleep(tiempo_de_espera)
				return False
			time.sleep(tiempo_de_espera)
		time.sleep(tiempo_de_espera)
		i += 1
		time.sleep(tiempo_de_espera)
		while(not(a_prime_number(i))):
			time.sleep(tiempo_de_espera)
			i += 1
			time.sleep(tiempo_de_espera)
		time.sleep(tiempo_de_espera)
		prime_numbers.append(i)
		time.sleep(tiempo_de_espera)
	time.sleep(tiempo_de_espera)
	return True
def a_is_divisible_by_this_list(num, list):
	time.sleep(tiempo_de_espera)
	for i in list:
		time.sleep(tiempo_de_espera)
		if(num % i == 0):
			time.sleep(tiempo_de_espera)
			return True
		time.sleep(tiempo_de_espera)
	time.sleep(tiempo_de_espera)
	return False
def a_prime_number_3_semirecursive(num):
	time.sleep(tiempo_de_espera)
	prime_numbers = [2]
	time.sleep(tiempo_de_espera)
	i = prime_numbers[-1]
	time.sleep(tiempo_de_espera)
	while(i <= math.floor(math.sqrt(num))):
		time.sleep(tiempo_de_espera)
		if(num % i == 0):
			time.sleep(tiempo_de_espera)
			return False
		time.sleep(tiempo_de_espera)
		i += 1
		time.sleep(tiempo_de_espera)
		while(a_is_divisible_by_this_list(i, prime_numbers)):
			time.sleep(tiempo_de_espera)
			i += 1
			time.sleep(tiempo_de_espera)
		time.sleep(tiempo_de_espera)
		prime_numbers.append(i)
		time.sleep(tiempo_de_espera)
	time.sleep(tiempo_de_espera)
	return True

#_________________________________________
numero = 73 * 79 #6174 #73*79=5767

#0.03200173377990723
#0.7620589733123779
#0.959773063659668
#0.3420262336730957

inicio = time.time()
for i in range(0, 10000): prime_number(numero)
print(time.time() - inicio)
inicio = time.time()

for i in range(0, 10000): prime_number_2(numero)
print(time.time() - inicio)
inicio = time.time()

for i in range(0, 10000): prime_number_3_semirecursive_intento_fallido(numero)
print(time.time() - inicio)
inicio = time.time()

for i in range(0, 10000): prime_number_3_semirecursive(numero)
print(time.time() - inicio)

#_________________________________________
#He hecho el tonto metiendo time.sleep() por todas partes, con un simple for es mejor
tiempo_de_espera = 0.0005

# 2.2490310668945312
# 8.872374773025513
# 22.907182216644287
# 13.477222681045532

inicio = time.time()
a_prime_number(numero)
print(time.time() - inicio)

inicio = time.time()
a_prime_number_2(numero)
print(time.time() - inicio)

inicio = time.time()
a_prime_number_3_semirecursive_intento_fallido(numero)
print(time.time() - inicio)

inicio = time.time()
a_prime_number_3_semirecursive(numero)
print(time.time() - inicio)