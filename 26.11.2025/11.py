from collections import Counter

def count_it(sequence):
	nums = [int(x) for x in sequence if x.isdigit()]

	counts = Counter(nums)
	most_common = counts.most_common(3)

	result_dict = {num: count for num, count in most_common}
	return result_dict

seq = "12312312456789000"
print(count_it(seq))