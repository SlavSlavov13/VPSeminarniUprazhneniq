number_of_inputs = int(input("Enter the number of inputs: "))

while number_of_inputs < 0:
	number_of_inputs = int(input("Number of inputs cannot be negative. Please enter again: "))

for i in range(number_of_inputs):
	number = int(input(f"\nEnter number {i + 1}: "))
	power = int(input("Enter the power to raise the number to: "))
	number_powered = number ** power
	print(f"{number} raised to the power of {power} is {number_powered}")