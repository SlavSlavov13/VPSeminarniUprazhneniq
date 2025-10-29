number_of_inputs = int(input("Enter the number of inputs: "))

while number_of_inputs < 0:
	number_of_inputs = int(input("Number of inputs cannot be negative. Please enter again: "))

number_of_evens = 0
number_of_odds = 0
max_even = float('-inf')
min_odd = float('inf')

for i in range(number_of_inputs):
	value = int(input(f"Enter value {i + 1}: "))
	if value % 2 == 0 and value != 0:
		number_of_evens += 1
		if value > max_even:
			max_even = value
	else:
		number_of_odds += 1
		if value < min_odd:
			min_odd = value

print(f"\nTotal number of inputs: {number_of_inputs}")
print('-------------------------')
print(f"Number of even inputs: {number_of_evens}")
if number_of_evens > 0:
	print(f"Maximum even input: {max_even}")
print('-------------------------')
print(f"Number of odd inputs: {number_of_odds}")
if number_of_odds > 0:
	print(f"Minimum odd input: {min_odd}")
