import myfunction

def the_n_prime_number(n):
	i = 1
	founded = 0
	while(founded < n):
		i += 1
		if(myfunction.prime_number(i)): founded += 1
	return i
print( the_n_prime_number(10001))		