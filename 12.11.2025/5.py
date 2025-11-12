my_dictionary = {}
print("You will enter exactly 7 key-value pairs.")
print()

for i in range(7):
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

print("--- 1. Initial Dictionary Contents ---")
print(f"The complete dictionary is: {my_dictionary}")
print()

print("--- 2. Find Key with Largest Value ---")
key_for_largest_value = max(my_dictionary, key=my_dictionary.get)
largest_value = my_dictionary[key_for_largest_value]

print(f"The largest value found is: {largest_value}")
print(f"This value corresponds to key: '{key_for_largest_value}'")
print()

print("--- 3. Replace a Value by Key ---")
key_to_change = input("Enter the key whose value you want to replace: ")

if key_to_change in my_dictionary:
	while True:
		new_value_input = input(f"Enter a NEW integer value for '{key_to_change}': ")
		if new_value_input.isdigit() or (new_value_input.startswith('-') and new_value_input[1:].isdigit()):
			new_value = int(new_value_input)
			break
		else:
			print("That is not a valid integer. Please try again.")

	my_dictionary[key_to_change] = new_value
	print(f"Value replaced. Dictionary is now: {my_dictionary}")
else:
	print(f"The key '{key_to_change}' was not found. No change was made.")
print()

print("--- 4. Delete an Item by Key ---")
key_to_delete = input("Enter the key of the item you want to delete: ")

if key_to_delete in my_dictionary:
	del my_dictionary[key_to_delete]
	print(f"Item deleted. Dictionary is now: {my_dictionary}")
else:
	print(f"The key '{key_to_delete}' was not found. No deletion was made.")
print()

print("--- 5. Add a New Key-Value Pair ---")
while True:
	new_key = input("Enter the NEW key to add: ")
	if not new_key:
		print("Key cannot be empty. Please try again.")
	elif new_key in my_dictionary:
		print(f"The key '{new_key}' already exists. Please enter a different key.")
	else:
		break

while True:
	new_value_input = input(f"Enter an INTEGER VALUE for '{new_key}': ")
	if new_value_input.isdigit() or (new_value_input.startswith('-') and new_value_input[1:].isdigit()):
		new_value = int(new_value_input)
		break
	else:
		print("That is not a valid integer. Please try again.")

my_dictionary[new_key] = new_value
print(f"Item added. Final dictionary: {my_dictionary}")