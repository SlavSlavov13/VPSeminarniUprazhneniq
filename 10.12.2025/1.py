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

def add_multiple_people(employees):
	count = get_int("\nHow many people do you want to add? ")
	for i in range(count):
		print(f"\nPerson {i+1}:")
		name = input("Enter Name: ")
		age = get_int("Enter Age: ")
		salary = get_float("Enter Salary: ")
		position = input("Enter Position: ")
		employees.append(Employee(name, age, salary, position))

def add_single_person(employees):
	print("\n--- Add Person ---")
	name = input("Enter Name: ")
	age = get_int("Enter Age: ")
	salary = get_float("Enter Salary: ")
	position = input("Enter Position: ")
	employees.append(Employee(name, age, salary, position))
	print("Employee added.")

def show_basic_data(employees):
	if not employees:
		print("\nList is empty.")
	else:
		print("\n--- Basic Data ---")
		for emp in employees:
			emp.display_basic_info()

def find_highest_salary(employees):
	if not employees:
		print("\nList is empty.")
	else:
		richest = max(employees, key=lambda x: x.salary)
		print(f"\nHighest Salary: {richest.name} (${richest.salary:.2f})")

def find_youngest_person(employees):
	if not employees:
		print("\nList is empty.")
	else:
		youngest = min(employees, key=lambda x: x.age)
		print(f"\nYoungest Person: {youngest.name} ({youngest.age} years old)")

def delete_person_by_name(employees):
	if not employees:
		print("\nList is empty.")
		return

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

def delete_all_records(employees):
	if not employees:
		print("\nList is already empty.")
	else:
		employees.clear()
		print("\nAll records have been deleted.")

def sort_by_name(employees):
	if not employees:
		print("\nList is empty.")
	else:
		employees.sort(key=lambda x: x.name)
		print("\nList sorted by name.")

def show_positions(employees):
	if not employees:
		print("\nList is empty.")
	else:
		print("\n--- Positions ---")
		for emp in employees:
			emp.display_position()

def calculate_avg_age_under_30(employees):
	if not employees:
		print("\nList is empty.")
		return

	under_30 = [e for e in employees if e.age < 30]
	total_age = sum(e.age for e in under_30)

	try:
		if len(under_30) == 0:
			raise ZeroDivisionError("No employees under 30 found.")

		average = total_age / len(under_30)
		print(f"\nAverage age of people under 30: {average:.2f}")

	except ZeroDivisionError as e:
		print(f"\nException Caught: {e}")
		print("Cannot calculate average (division by zero).")

def main():
	employees = []

	actions = {
		'1': add_multiple_people,
		'2': add_single_person,
		'3': show_basic_data,
		'4': find_highest_salary,
		'5': find_youngest_person,
		'6': delete_person_by_name,
		'7': delete_all_records,
		'8': sort_by_name,
		'9': show_positions,
		'0': calculate_avg_age_under_30
	}

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

		if choice == 'exit':
			print("\nExiting...")
			break

		if choice in actions:
			actions[choice](employees)
		else:
			print("\nInvalid choice, please try again.")

if __name__ == "__main__":
	main()