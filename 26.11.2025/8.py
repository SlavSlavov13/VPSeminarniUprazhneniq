def find_non_unique_elements(sequence):
	counts = {}
	for item in sequence:
		if item in counts:
			counts[item] += 1
		else:
			counts[item] = 1

	duplicates = [item for item, count in counts.items() if count > 1]
	return duplicates

seq = [1, 2, 3, 2, 4, 5, 1, 6, 1]
print(f"Неуникални елементи: {find_non_unique_elements(seq)}")