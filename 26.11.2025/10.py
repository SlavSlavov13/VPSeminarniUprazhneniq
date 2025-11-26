def sieve(numbers):
	unique_nums = set(numbers)
	sorted_unique = sorted(unique_nums, reverse=True)
	return tuple(sorted_unique)

nums = [1, 2, 3, 2, 4, 5, 1, 6, 9, 0]
print(sieve(nums))