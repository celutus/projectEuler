"""
Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is th esmallest positive number that is evely divisible by all of the numbers from 1 to 20?
"""

#la solucion es hacer minimo comun multiplo de 1,2,3...19,20
#o hacer fuerza bruta probando numeoros a dividir por todos estos... lo que no tiene valor

import myfunction


print(myfunction.least_common_multiple_infinite([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(myfunction.least_common_multiple_infinite([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))

"""
diso que locura después de resolverlo chatGPT me dice esto:
To compute this efficiently, we can use the property that the LCM of two numbers a and b can be found using their greatest common divisor (GCD) with the formula:

LCM(a,b) = abs(a*b)/GCM(a,b)

For multiple numbers, we can extend this by finding the LCM of numbers progressively:
LCM(a,b,c) = LCM(LCM(a,b),c)
and so on
"""