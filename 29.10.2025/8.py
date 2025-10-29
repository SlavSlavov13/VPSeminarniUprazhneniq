number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

type_of_action = input("Enter the type of action (+, -, *, **, /): ")
while type_of_action not in ['+', '-', '*', '**', '/']:
	type_of_action = input("Invalid action. Please enter one of (+, -, *, **, /): ")

if type_of_action == '+':
	result = number1 + number2
elif type_of_action == '-':
	result = number1 - number2
elif type_of_action == '*':
	result = number1 * number2
elif type_of_action == '**':
	result = number1 ** number2
elif type_of_action == '/':
	while number2 == 0:
		number2 = int(input("Division by zero is not allowed. Please enter a non-zero second number: "))
	result = number1 / number2

print(f"The result of {number1} {type_of_action} {number2} is: {result}")
