while True:
	items_count = input("How many integers will you enter for each set? ")
	if items_count.isdigit():
		items_count = int(items_count)
		if items_count > 0:
			break
		else:
			print("Please enter a positive integer.")
	else:
		print("That is not a valid integer. Please try again.")

print()

set_a = set()
print(f"--- Enter {items_count} integers for Set A ---")
for i in range(items_count):
	while True:
		value_input = input(f"Enter integer #{i + 1}: ")
		if value_input.isdigit() or (value_input.startswith('-') and value_input[1:].isdigit()):
			value = int(value_input)
			break
		else:
			print("That is not a valid integer. Please try again.")

	set_a.add(value)
	print(f"Set A so far: {set_a}")

print()

set_b = set()
print(f"--- Enter {items_count} integers for Set B ---")
for i in range(items_count):
	while True:
		value_input = input(f"Enter integer #{i + 1}: ")
		if value_input.isdigit() or (value_input.startswith('-') and value_input[1:].isdigit()):
			value = int(value_input)
			break
		else:
			print("That is not a valid integer. Please try again.")

	set_b.add(value)
	print(f"Set B so far: {set_b}")

print()

print(f"Set A created: {set_a}")
print(f"Set B created: {set_b}")

print()

print("--- 1. Set Sizes ---")
print(f"Size of Set A: {len(set_a)}")
print(f"Size of Set B: {len(set_b)}")
print()

print("--- 2. Union (A | B) ---")
print(f"The union of Set A and Set B is: {set_a | set_b}")
print()

print("--- 3. Difference (A - B) and (B - A) ---")
print(f"The difference (A - B) is: {set_a - set_b}")

print(f"The difference (B - A) is: {set_b - set_a}")
print()

print("--- 4. Intersection (A & B) ---")
print(f"The intersection of Set A and Set B is: {set_a & set_b}")
print()

print("--- 5. Remove element from Set A ---")
while True:
	element_to_remove_str = input("Enter an integer to remove from Set A: ")
	if element_to_remove_str.isdigit() or (element_to_remove_str.startswith('-') and element_to_remove_str[1:].isdigit()):
		element_to_remove = int(element_to_remove_str)
		break
	else:
		print("That is not a valid integer. Please try again.")

if element_to_remove in set_a:
	set_a.remove(element_to_remove)
	print(f"Successfully removed {element_to_remove} from Set A.")
	print(f"Set A is now: {set_a}")
else:
	print(f"The element {element_to_remove} is not in Set A. No change was made.")

print()

print("--- 6. Clearing both sets ---")
set_a.clear()
print(f"Set A has been cleared. Set A is now: {set_a}")
set_b.clear()
print(f"Set B has been cleared. Set B is now: {set_b}")
