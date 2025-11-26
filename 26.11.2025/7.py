def get_divisors(number):
	divisors = []
	for i in range(1, (number // 2) + 1):
		if number % i == 0:
			divisors.append(i)
	divisors.append(number)
	return divisors

num = 12
print(f"Делители на {num}: {get_divisors(num)}")