def find_min_diff_pair(numbers):
	if len(numbers) < 2:
		return []

	numbers.sort()
	min_diff = float('inf')
	result_pair = []

	for i in range(len(numbers) - 1):
		diff = abs(numbers[i] - numbers[i+1])
		if diff < min_diff:
			min_diff = diff
			result_pair = [numbers[i], numbers[i+1]]

	return result_pair

nums_list = [10, 5, 20, 3, 15]
print(f"Двойка с минимална разлика: {find_min_diff_pair(nums_list)}")