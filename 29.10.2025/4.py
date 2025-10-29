minimum_of_interval = int(input("Enter the minimum of the interval: "))
maximum_of_interval = int(input("Enter the maximum of the interval: "))

while maximum_of_interval < minimum_of_interval:
	print("Maximum of the interval must be greater than or equal to minimum.\n")
	maximum_of_interval = int(input("Enter the maximum of the interval: "))

number_of_inputs = int(input("Enter the number of inputs: "))

while number_of_inputs < 0:
	number_of_inputs = int(input("Number of inputs cannot be negative. Please enter again: "))

count_within_interval = 0
sum_of_numbers_within_interval = 0

for i in range(number_of_inputs):
	value = int(input(f"Enter value {i + 1}: "))
	if minimum_of_interval <= value <= maximum_of_interval:
		count_within_interval += 1
		sum_of_numbers_within_interval += value

print(f"\nTotal number of inputs: {number_of_inputs}")
print('-------------------------')
print(f"Number of inputs within the interval [{minimum_of_interval}, {maximum_of_interval}]: {count_within_interval}")
if count_within_interval > 0:
	print(f"Sum of inputs within the interval: {sum_of_numbers_within_interval}")
