number_of_inputs = int(input("Enter the number of elements: "))

while number_of_inputs < 0:
	number_of_inputs = int(input("Number of inputs cannot be negative. Please enter again: "))

sum_of_evens = 0
sum_of_odds = 0
average_of_evens = 0
average_of_odds = 0
count_of_evens = 0
count_of_odds = 0

for i in range(number_of_inputs):
	element = int(input(f"Enter element {i + 1}: "))
	if element % 2 == 0 and element != 0:
		sum_of_evens += element
		count_of_evens += 1
	else:
		sum_of_odds += element
		count_of_odds += 1

print(f"\nNumber of all elements: {number_of_inputs}")
print('-------------------------')
print(f"Number of even elements: {count_of_evens}")
if count_of_evens > 0:
	average_of_evens = sum_of_evens / count_of_evens
	print(f"Sum of even elements: {sum_of_evens}")
	print(f"Average of even elements: {average_of_evens:.2f}")
print('-------------------------')
print(f"Number of odd elements: {count_of_odds}")
if count_of_odds > 0:
	average_of_odds = sum_of_odds / count_of_odds
	print(f"Sum of odd elements: {sum_of_odds}")
	print(f"Average of odd elements: {average_of_odds:.2f}")
