number_of_inputs = int(input("Enter the number of inputs: "))

while  number_of_inputs > 55 or number_of_inputs < 35:
	number_of_inputs = int(input("Number of inputs cannot be less than 35 or more than 55. Please enter again: "))

sum_of_double_digit_numbers = 0
count_of_double_digit_numbers = 0
count_of_positive_numbers = 0
count_of_negative_numbers = 0

for i in range(number_of_inputs):
	number = int(input(f"\nEnter number {i + 1}: "))

	while number < -200 or number > 200:
		number = int(input("Number must be between -200 and 200. Please enter again: "))

	if 10 <= abs(number) <= 99:
		sum_of_double_digit_numbers += number
		count_of_double_digit_numbers += 1

	if number > 0:
		count_of_positive_numbers += 1
	elif number < 0:
		count_of_negative_numbers += 1

print(f"\nTotal number of inputs: {number_of_inputs}")
print('-------------------------')
print(f"Number of double-digit numbers: {count_of_double_digit_numbers}")
if count_of_double_digit_numbers > 0:
	average_of_double_digit_numbers = sum_of_double_digit_numbers / count_of_double_digit_numbers
	print(f"Average of double-digit numbers: {average_of_double_digit_numbers:.2f}")
print('-------------------------')
print(f"Number of positive numbers: {count_of_positive_numbers}")
print(f"Number of negative numbers: {count_of_negative_numbers}")
