number_of_inputs = input("How many strings will you enter? ")

while not number_of_inputs.isdigit():
	print("That is not a valid integer. Please try again.")
	number_of_inputs = input("How many strings will you enter? ")

number_of_inputs = int(number_of_inputs)

while number_of_inputs <= 0:
	print("Please enter a positive integer.")
	number_of_inputs = int(input("How many strings will you enter? "))

list_of_strings = []

for i in range(number_of_inputs):
	user_input = input("Enter a string: ")
	list_of_strings.append(user_input)

print()

longest_string = max(list_of_strings, key=len)
print(f"The longest string is: '{longest_string}' with length {len(longest_string)}")

print()

string_to_swap = input("Enter the text you want to swap: ")
if string_to_swap in list_of_strings:
	index_of_string_to_swap = list_of_strings.index(string_to_swap)
	new_text = input("Enter the new text to swap with: ")
	list_of_strings[index_of_string_to_swap] = new_text
	print("Updated list after swapping:", list_of_strings)
else:
	print(f"The text '{string_to_swap}' is not in the list. No swap performed.")

print()

string_to_delete = input("Enter the text you want to delete: ")
if string_to_delete in list_of_strings:
	list_of_strings.remove(string_to_delete)
	print("Updated list after deletion:", list_of_strings)
else:
	print(f"The text '{string_to_delete}' is not in the list. No deletion performed.")

print()

index_to_insert_string_at = int(input("Enter the index where you want to insert a new string: "))
while index_to_insert_string_at < 0 or index_to_insert_string_at > len(list_of_strings):
	print("Invalid index. Please enter a valid index.")
	index_to_insert_string_at = int(input("Enter the index where you want to insert a new string: "))
new_string = input("Enter the new string to insert: ")
list_of_strings.insert(index_to_insert_string_at, new_string)
print("Updated list after insertion:", list_of_strings)
