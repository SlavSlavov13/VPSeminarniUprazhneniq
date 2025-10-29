sum_of_numbers = 0
product_of_numbers = 1
should_print = False

while True:
	number = int(input("Enter a number (-99 to stop): "))
	if number == -99:
		break
	if number > 0:
		should_print = True
		sum_of_numbers += number
		product_of_numbers *= number

if should_print:
	print(f"\nSum of the entered numbers: {sum_of_numbers}")
	print(f"Product of the entered numbers: {product_of_numbers}")
