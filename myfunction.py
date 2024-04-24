import math



#///_._1_._///________________________________________________________________________________________________________
# es a multiplo de b?
def multiple(a, b):
	if(a % b == 0): return True
	return False
#///_._2_._///________________________________________________________________________________________________________

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# devuelve el iésimo (por eso no pongo num de argumento) número de fibonacci
# la sucesión de fibonacci es 1, 1, 2, 3, 5...
# pero en projecto euler han puesto 1, 2, 3, 5...
def fibonacci(i):
	one = 1
	two = 1
	three = 1
	for j in range(0, i - 2):
		three = one + two
		one = two
		two = three
	return three

#sería igual que el código de fibonacci(i) pero con range(0, i - 1)
def projecteuler_fibonacci(i):
	return fibonacci(i + 1)

#es par?
def even_valued_term(num):
	if(num % 2 == 0): return True
	return False

#///_._3_._///________________________________________________________________________________________________________
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#yo me acuerdo en 42 madrid cuando calculábamos números primos, que ponía range(2, num/2), hasta la mitad porque
#no sabía muy bien donde estaba el límite hasta donde podías bajar, pero ahora si lo sé,
#el límite es num = sqrt(num) * sqrt(num). Gracias a la ingeniería que estoy haciendo estas cosas de matemáticas
#se me ocurren. num = a * b, si a es mayor a sqrt(num), b es menor a sqrt(num) y si a es menor, b es mayor.
#cuando encuentra un divisor te da igual porque hace return, y rompe el bucle, pero cuando es primo y no encuentra divisores,
#que tranque en sqrt(num) está de puta madre.
#En 42 no estaba bien el código porque excedía en tiempo, pero creo que solamente esto de sqrt no lo hubiese arreglado,
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#creo que si hubiese servido lo de hacer lista de numeros primos, voy a medir el tiempo que dura cada funcion prime_number

#esta es una forma sencilla de saber si es primo
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#usando math.floor te da como primos el 4, 6, 8, 9. El nueve por ejemplo porque hace range(2,3) no llega al 3 y no divide.
#yo pensaba que tenía que poner math.ceil, pero no, ahora que he visto el ejemplo del 9, es math.floor + 1
#esto no varía prácticamente en la velocidad de las funciones, sólo en los resultados (de números pequeños, por ejemplo en los
# cien primeros números los afectados son 4, 6, 8, 9, 15, 25, 35, 49)
def prime_number(num):
	for i in range(2, math.floor(math.sqrt(num)) + 1):
		if(num % i == 0): return False
	return True

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#con esta forma te ahorras dividir entre los no primos, por ejemplo dividir entre 4, pero no compensa el código extra
#calculas si 4 es primo y te ahorras 700 / 4, merece la pena porque 4/2 es más rápido
#calculas si 300 es primo y te ahorras 700 / 300, no merece la pena
def prime_number_2(num):
	i = 2
	while(i <= math.floor(math.sqrt(num)) + 1):
		if(num % i == 0): return False
		i += 1
		while(not(prime_number(i))):
			i += 1
	return True
#usando una lista que guarda los números primos anteriores
#el problema de este intento es que es la misma función que prime_number_2, sólo que guarda una lista, pero no hago nada con la lista
#porque donde hago for(j) no sirve para nada porque ya lo has hecho en otras iteraciones de (i)
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#lo de la lista está bien, pero lo tienes que usar en otra función para no tener que usar prime_number (el original) dentro de tu función prime_number_3
#le he puesto el nombre de intento fallido sin ni siquiera ejecutarlo
def prime_number_3_semirecursive_intento_fallido(num):
	prime_numbers = [2]
	i = prime_numbers[-1]
	while(i <= math.floor(math.sqrt(num)) + 1):
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
			#aqui hay un problema y es que puedes estar llevando (i) más allá de sqrt(num) mientras no sea primo, es derroche de calculo
			#el problema es que tienes en dos sitios i+=1 y eso genera conflictos matemáticos. El código está bien pero no optimizado del todo
			#esto no es el motivo de que sea más lento que la forma bruta prime_number
			i += 1
		prime_numbers.append(i)
	return True

# queria hacer las funciones prime_numbers_below y prime_factors con listas como en prime_number_3_semirecursive, pero
#no iba a ser eficaz, por eso lo hice en lo más básica: saber si un número es primo. Y está comprobado que es más lento
#que el método más bruto.
#Pues al final he hecho aquí el recursivo y es más rápido jejejejejejejejejeje
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#Pensé: vale que el bruto es más rápido en saber si un número es primo, pero en crear un lista, ahí el bruto puede que no gane
def prime_numbers_below_equal(num): #10 mil repeticiones 0.87 segundos
	prime_numbers = []
	for i in range(2, num + 1):
		if(prime_number(i)): prime_numbers.append(i)
	return prime_numbers

def prime_numbers_below_equal(num): #10 mil repeticiones -> 0,33 segundos
	#DIVIDIENDO ENTRE LA LISTA DE NÚMEROS PRIMOS HACES MENOS DIVISIONES
	prime_numbers = []
	i = 2
	while(i <= num):
		if(not(is_divisible_by_this_list(i, prime_numbers))):
			prime_numbers.append(i)
		i += 1
	return prime_numbers

def prime_factors(num): #factorizacion de num
	#podría hacerlo probando todos los números, pero voy a hacerlo sólo con los primos, más eficaz
	prime_factors = []
	# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
	# prime_numbers = prime_numbers_below_2_recursive(num) NO ME SIRVE PORQUE SI PONES 7, TE DEVUELVE VACÍO
	prime_numbers = prime_numbers_below_equal(num) #debe ser con los primos incluido el propio numero porque puede que el numero no tenga primos
	i = 0
	final = False
	while(i < len(prime_numbers)):
		while(num % prime_numbers[i] == 0):
			prime_factors.append(prime_numbers[i])
			num /= prime_numbers[i]
			if(num == 1): final = True
		i += 1
		if(final): break
	return prime_factors

#///_._4_._///________________________________________________________________________________________________________


def palindromic(string):
	for i in range(0, math.floor(len(string) / 2)):
		if(string[i] != string[-1 + -i]):
			return False
	return True


def max_of_array(array): #existe max() + + + + + + + + + +
	if(len(array)): max = array[0]
	else: max = None

	for i in array:
		if(i > max): max = i
	return max
"""
///_._5_._///________________________________________________________________________________________________________

mcm de 5 y 7, como los dos son primos es su multiplicación: 35
mcm de 10 y 14, es como el mcm de 5 y 7 pero por 2, el número necesario para reducirlos a primos, 2*(5*7) = 70
mcm de 7 y 5*(2*3)? En este caso no podrías reducir los dos números (7 y 5 por dos) ahora sólo puedes reducir el 30 por 2 y 3
	pero el 7 permanece igual, como se procede? pues el mínimo común múltiplo es 7*5*(2*3) = 210

y si es 7*(2) y 5*(3)? también es 210. No importa como estén repartidos los números, es simplemente 2*3*5*7 (todos números primos)

y 2 y 3 el mcm es 6
pero 2 y 3*2 es también 6 (LOS PRIMOS REPETIDOS NO SE CUENTAN), sólo sería 2*3
y 2 y 3*4=3*2*2 es mcm 2*2*3
4 y 10 es 2*2 y 2*5 y el mcm es 2*2*5 = 20

se cogen los números primos de los números y se cogen los sueltos y una vez los repetidos en los dos números

3, 8 -> 24
3*2 , 2*2 -> 12
3*2*2 , 2 -> 12
3*2*2*2 , 1 -> 24
tienes la lista de numeros del numero A y la lista de numeros del B
cuando coges un numero lo quitas de la lista
coges los numeros que solo estan en una lista y te los llevas a la final
los numeros repetidos en las dos listas, pones ese numero una unica vez en la lista final y quitas el numero de las dos listas iniciales
3 2 2 2 , 2 -> 3 2 2 2 esta claro que coges todos los numeros de una lista...
"""

def how_many_times_element_in_array(element, array):
	count = 0
	for i in array:
		if(i == element): count += 1
	return count

def least_common_multiple(a, b): #ESTOY HACIENDO MINIMO COMUN MULTIPLO DE DOS NÚMEROS PERO DEBE SER DE CUANTOS SEA NECESARIO
	prime_factors_a = prime_factors(a)
	prime_factors_b = prime_factors(b)
	prime_factors_lcm = prime_factors_a #cojo los de (a) y le añado los de (b) que cumplan lo de arriba
	i = 0
	while i < len(prime_factors_b):
		difference = how_many_times_element_in_array(prime_factors_b[i], prime_factors_b) - how_many_times_element_in_array(prime_factors_b[i], prime_factors_a)
		for j in range(0, difference):
			prime_factors_lcm.append(prime_factors_b[i])
		#if difference <= 1: i += 1 con estas dos lineas tambien funciona pero la de abajo es mejor
		#else: i += difference pero si del numero i tienes 10 en b y 5 en a, la diferencia es 5, y cuando haces i+5, sigues estando en el numero i, NO FUNCIONA + + + + + + + + + +
		i += how_many_times_element_in_array(prime_factors_b[i], prime_factors_b)
	print(prime_factors_a)
	print(prime_factors_b)
	print(prime_factors_lcm)
	lcm = 1
	for i in prime_factors_lcm:
		lcm *= i
	return lcm

def least_common_multiple_infinite(array_of_numbers):
	array_of_prime_factors = []
	for i in array_of_numbers:
		array_of_prime_factors.append(prime_factors(i))
	lcm = 1
	for i in range(0, max(array_of_numbers)):
		how_many_i_in_prime_factors = []
		for j in range(0, len(array_of_numbers)): # puede ser len de array_of_numbers o array_of_prime_factos... son de la misma longitud
			how_many_i_in_prime_factors.append( how_many_times_element_in_array(i, array_of_prime_factors[j]) )
		for j in range(0, max(how_many_i_in_prime_factors)): lcm *= i
	
	return lcm

#///_._6_._///________________________________________________________________________________________________________
#///_._7_._///________________________________________________________________________________________________________
#///_._8_._///________________________________________________________________________________________________________

"""NO ME HA HECHO FALTA USAR ESTO, PERO LO INTENTÉ PORQUE TENÍA CURIOSIDAD"""
#el mínimo común divisor consiste en coger los factores primos de los dos números y coger los que coincidan.
# tiene sentido: el producto de los que cojas será el mayor número por el que puedes dividir ambos números y que quede entero
#PODRÍA HACER FUNCIÓN QUE DIJERA QUE ELEMENTOS ESTÁN EN TODAS LAS LISTAS
def greatest_common_divisor(array_of_numbers):
	array_of_prime_factors = []
	for i in array_of_numbers:
		array_of_prime_factors.append(prime_factors(i))
	#voy a coger los primos del primer número, y si no me los encuentro en el resto de números, los voy tachando
	prime_factors_mcd = array_of_prime_factors[0]

	#FUNCIONA MAL, TENGO QUE HACER LO DE DIFFERENCE (PROBAR CON EL 12 Y 18 Y SE VE QUE SALE MCD = 12)

	i = 0 #el cero ya has cogido los primos
	while i < len(prime_factors_mcd):
		notin = False
		for j in array_of_prime_factors:
			if prime_factors_mcd[i] not in j:
				notin = True
				break
		if(notin): prime_factors_mcd.pop(i)
		else: i += 1
	
	mcd = 1
	for i in prime_factors_mcd:
		mcd *= i
	return mcd