list_of_numbers = []

number_of_inputs = input("How many numbers do you want to enter? ")
while not number_of_inputs.isdigit():
	print("That is not a valid integer. Please try again.")
	number_of_inputs = input("How many numbers do you want to enter? ")

number_of_inputs = int(number_of_inputs)

while number_of_inputs <= 0:
	print("Please enter a positive integer.")
	number_of_inputs = int(input("How many numbers do you want to enter? "))

for _ in range(number_of_inputs):
	user_input = input("Enter a number: ")
	while not user_input.isdigit():
		print("Invalid input. Please enter a valid number.")
		user_input = input("Enter a number: ")
	number = int(user_input)
	list_of_numbers.append(number)

print()

tripled_list = []
for i in range(len(list_of_numbers)):
	tripled_list.append(list_of_numbers[i] * 3)
print('Tripled list: ', end='')
print(tripled_list)

print()

for i, number in enumerate(list_of_numbers):
	print(f'Index {i}: {number}')

print()

number_to_check_for = int(input("Enter a number to check if it's in the list: "))
if number_to_check_for in list_of_numbers:
	print(f"The number {number_to_check_for} is in the list.")
else:
	print(f"The number {number_to_check_for} is not in the list.")

print()

print("Sorted list: ", end='')
print(sorted(list_of_numbers))

print()

print(f"Maximum number in the list: {max(list_of_numbers)}")

print()

index_of_number_to_delete = int(input("Enter the index of the number you want to delete: "))
while index_of_number_to_delete < 0 or index_of_number_to_delete >= len(list_of_numbers):
	print("Invalid index. No element deleted.")
	index_of_number_to_delete = int(input("Enter a valid index of the number you want to delete: "))
else:
	del list_of_numbers[index_of_number_to_delete]
	print("Updated list after deletion:", list_of_numbers)

print()

index_of_element_to_change = int(input("Enter the index of the element you want to change: "))
while index_of_element_to_change < 0 or index_of_element_to_change >= len(list_of_numbers):
	print("Invalid index. No element changed.")
	index_of_element_to_change = int(input("Enter a valid index of the element you want to change: "))
else:
	new_value = int(input("Enter the new value: "))
	list_of_numbers[index_of_element_to_change] = new_value
	print("Updated list after change:", list_of_numbers)
