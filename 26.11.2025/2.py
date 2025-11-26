def calculate_median(numbers):
	numbers.sort()
	n = len(numbers)
	if n % 2 == 1:
		median = numbers[n // 2]
	else:
		mid1 = numbers[n // 2 - 1]
		mid2 = numbers[n // 2]
		median = (mid1 + mid2) / 2
	return round(median, 1)

sorted_nums = [1, 2, 3, 4, 5, 6]
print(f"Медиана: {calculate_median(sorted_nums)}")