while True:
	number_of_inputs_str = input("How many key-value pairs will you enter? ")
	if number_of_inputs_str.isdigit():
		number_of_inputs = int(number_of_inputs_str)
		if number_of_inputs > 0:
			break
		else:
			print("Please enter a positive integer.")
	else:
		print("That is not a valid integer. Please try again.")

my_dictionary = {}
print(f"You will enter {number_of_inputs} items.")

for i in range(number_of_inputs):
	while True:
		key = input(f"Enter key #{i + 1}: ")
		if not key:
			print("Key cannot be empty. Please try again.")
		elif key in my_dictionary:
			print(f"The key '{key}' already exists. Please enter a different key.")
		else:
			break

	while True:
		value_input = input(f"Enter an INTEGER VALUE for '{key}': ")
		if value_input.isdigit() or (value_input.startswith('-') and value_input[1:].isdigit()):
			value = int(value_input)
			break
		else:
			print("That is not a valid integer. Please try again.")

	my_dictionary[key] = value

print()
print(f"Dictionary created: {my_dictionary}")
print()

key_to_check_for = input("Enter a key to check if it exists in the dictionary: ")
if key_to_check_for in my_dictionary:
	print(f"The key '{key_to_check_for}' exists in the dictionary with value {my_dictionary[key_to_check_for]}.")
else:
	print(f"The key '{key_to_check_for}' does not exist in the dictionary.")
print()

key_to_change = input("Enter the key whose value you want to change: ")

if key_to_change in my_dictionary:
	while True:
		new_value_input = input(f"Enter a NEW integer value for '{key_to_change}': ")
		if new_value_input.isdigit() or (new_value_input.startswith('-') and new_value_input[1:].isdigit()):
			new_value = int(new_value_input)
			break
		else:
			print("That is not a valid integer. Please try again.")

	my_dictionary[key_to_change] = new_value
	print(f"Value changed. Dictionary: {my_dictionary}")
else:
	print(f"The key '{key_to_change}' was not found in the dictionary. No change was made.")

print()

key_to_delete = input("Enter the key you want to delete: ")

if key_to_delete in my_dictionary:
	del my_dictionary[key_to_delete]
	print(f"Item deleted. Dictionary: {my_dictionary}")
else:
	print(f"The key '{key_to_delete}' was not found in the dictionary. No deletion was made.")

print()

print("--- All keys in the dictionary ---")
for key in my_dictionary.keys():
	print(key)
print()

print("--- All values in the dictionary ---")
for value in my_dictionary.values():
	print(value)
print()

print("--- Dictionary contents (sorted by key) ---")
all_keys = list(my_dictionary.keys())
all_keys.sort()

print("Format: Key -> Value")
for key in all_keys:
	print(f"'{key}' -> {my_dictionary[key]}")