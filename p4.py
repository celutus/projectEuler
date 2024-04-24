"""
Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99

Find th elargest palindrome made from the product of two 3-digit numbers
"""

from functions_file import palindromic, max_of_array

palindromic_numbers = []

for i in range(0, 999 + 1):
	for j in range(0, 999 + 1):
		num = i * j
		if(palindromic(str(num))):
			palindromic_numbers.append(num)



print(max_of_array(palindromic_numbers))