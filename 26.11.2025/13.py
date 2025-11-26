def set_gen(numbers):
	result = set()
	counts = {}

	for num in numbers:
		if num not in counts:
			counts[num] = 1
			result.add(num)
		else:
			counts[num] += 1
			new_val = str(num) * counts[num]
			result.add(new_val)

	return result

nums_list = [4, 5, 4, 6, 4, 5, 7]
print(set_gen(nums_list))