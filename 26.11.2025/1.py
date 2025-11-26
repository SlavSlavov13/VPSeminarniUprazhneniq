def check_sequence(numbers):
	current_sum = 0
	for num in numbers:
		if num <= current_sum:
			return False
		current_sum += num
	return True

nums = [1, 2, 4, 8, 16]
print(f"Резултат от проверката: {check_sequence(nums)}")