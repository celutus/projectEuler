def sum_of_the_squares_of_the_first_n_natural_numbers(n):
	sum = 0
	for i in range(1, n+1):
		sum += i**2
	return sum

def square_of_the_sum_of_the_first_n_natural_numbers(n):
	sum = 0
	for i in range(1, n+1):
		sum += i
	square = sum**2
	return square

def another_way(n):
	sum = 0
	for i in range(1, n+1):
		for j in range(1, n+1):
			if(i != j): sum += i*j
	return sum


number = 100
print( square_of_the_sum_of_the_first_n_natural_numbers(number) - sum_of_the_squares_of_the_first_n_natural_numbers(number))
print( another_way(number))


