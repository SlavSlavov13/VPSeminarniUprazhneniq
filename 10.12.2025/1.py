class Person:
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

	def display_basic_info(self):
		print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary:.2f}")

class Employee(Person):
	def __init__(self, name, age, salary, position):
		super().__init__(name, age, salary)
		self.position = position

	def display_position(self):
		print(f"Name: {self.name} - Position: {self.position}")


def get_float(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Error: Invalid input type. Please enter a valid number.")

def get_int(prompt):
	while True:
		try:
			return int(input(prompt))
		except ValueError:
			print("Error: Invalid input type. Please enter an integer.")


def main():
	employees = []

	while True:
		print("\n--- MENU ---")
		print("1. Add multiple people")
		print("2. Add a single person")
		print("3. Show basic data (Name, Age, Salary)")
		print("4. Find person with highest salary")
		print("5. Find youngest person")
		print("6. Delete a person by name")
		print("7. Delete all records")
		print("8. Sort by Name")
		print("9. Show positions only")
		print("0. Calculate Avg Age (Under 30) - [Exception Test]")
		print('Type "exit" to stop the program')

		choice = input("\nChoose an option: ")

		if choice == '1':
			count = get_int("\nHow many people do you want to add? ")
			for i in range(count):
				print(f"\nPerson {i+1}:")
				name = input("Enter Name: ")
				age = get_int("Enter Age: ")
				salary = get_float("Enter Salary: ")
				position = input("Enter Position: ")
				employees.append(Employee(name, age, salary, position))

		elif choice == '2':
			print("\n--- Add Person ---")
			name = input("Enter Name: ")
			age = get_int("Enter Age: ")
			salary = get_float("Enter Salary: ")
			position = input("Enter Position: ")
			employees.append(Employee(name, age, salary, position))
			print("Employee added.")

		elif choice == '3':
			print("\n--- Basic Data ---")
			for emp in employees:
				emp.display_basic_info()

		elif choice == '4':
			if not employees:
				print("\nList is empty.")
			else:
				richest = max(employees, key=lambda x: x.salary)
				print(f"\nHighest Salary: {richest.name} (${richest.salary:.2f})")

		elif choice == '5':
			if not employees:
				print("\nList is empty.")
			else:
				youngest = min(employees, key=lambda x: x.age)
				print(f"\nYoungest Person: {youngest.name} ({youngest.age} years old)")

		elif choice == '6':
			name_to_delete = input("\nEnter the name of the person to delete: ")
			found = False

			for emp in employees:
				if emp.name == name_to_delete:
					employees.remove(emp)
					print(f"Successfully deleted {name_to_delete}.")
					found = True
					break

			if not found:
				print(f"Error: Could not find anyone named '{name_to_delete}'.")

		elif choice == '7':
			employees.clear()
			print("\nAll records have been deleted.")

		elif choice == '8':
			employees.sort(key=lambda x: x.name)
			print("\nList sorted by name.")

		elif choice == '9':
			if not employees:
				print("\nList is empty.")
			else:
				print("\n--- Positions ---")
				for emp in employees:
					emp.display_position()

		elif choice == '0':
			under_30 = [e for e in employees if e.age < 30]
			total_age = sum(e.age for e in under_30)

			try:
				if len(under_30) == 0:
					raise ZeroDivisionError("\nNo employees under 30 found.")

				average = total_age / len(under_30)
				print(f"\nAverage age of people under 30: {average:.2f}")

			except ZeroDivisionError as e:
				print(f"\nException Caught: {e}")
				print("Cannot calculate average (division by zero).")

		elif choice == 'exit':
			print("\nExiting...")
			break

		else:
			print("\nInvalid choice, please try again.")

if __name__ == "__main__":
	main()