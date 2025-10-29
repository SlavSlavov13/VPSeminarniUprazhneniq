minimum_of_interval = int(input("Enter the minimum of the interval: "))
maximum_of_interval = int(input("Enter the maximum of the interval: "))

while maximum_of_interval < minimum_of_interval:
	print("Maximum of the interval must be greater than or equal to minimum.\n")
	maximum_of_interval = int(input("Enter the maximum of the interval: "))

user_number = int(input("Enter a number: "))

if minimum_of_interval <= user_number <= maximum_of_interval:
	print(f"The number {user_number} is within the interval [{minimum_of_interval}, {maximum_of_interval}].")
else:
	print(f"The number {user_number} is outside the interval [{minimum_of_interval}, {maximum_of_interval}].")
