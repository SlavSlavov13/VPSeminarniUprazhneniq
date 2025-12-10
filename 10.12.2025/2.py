class TriangleChecker:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def is_triangle(self):
		try:
			side_a = float(self.a)
			side_b = float(self.b)
			side_c = float(self.c)
		except ValueError:
			return "Трябва да въведете само числа!"

		if side_a <= 0 or side_b <= 0 or side_c <= 0:
			return "Нищо няма да работи с отрицателни числа!"

		if (side_a + side_b > side_c) and (side_a + side_c > side_b) and (side_b + side_c > side_a):
			return "Ура, можете да построите триъгълник!"
		else:
			return "Жалко, но не можете да направите триъгълник от това ."

def main():
	while True:
		print("\n--- Check Triangle ---")
		print("Type 'exit' to quit.")

		a_input = input("Enter side A: ")
		if a_input.lower() == "exit":
			break
		b_input = input("Enter side B: ")
		c_input = input("Enter side C: ")

		checker = TriangleChecker(a_input, b_input, c_input)

		print(f"\nResult: {checker.is_triangle()}")

if __name__ == "__main__":
	main()