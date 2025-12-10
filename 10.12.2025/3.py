class Slujitel:
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	def work(self):
		print(f"{self.name} works.")

	def show_salary(self):
		print(f"Salary: {self.salary}")

class Manager(Slujitel):
	def __init__(self, name, salary, subordinates_count):
		super().__init__(name, salary)
		self.subordinates_count = subordinates_count

	def hold_meeting(self):
		print(f"Manager {self.name} is holding a meeting.")

	def show_info(self):
		print(f"Manager: {self.name}, Salary: {self.salary}, Subordinates: {self.subordinates_count}")

class Developer(Slujitel):
	def __init__(self, name, salary, language, experience_years):
		super().__init__(name, salary)
		self.language = language
		self.experience_years = experience_years

	def write_code(self):
		print(f"Developer {self.name} writes code in {self.language}.")

	def show_info(self):
		print(f"Dev: {self.name}, Language: {self.language}, Experience: {self.experience_years} years")

def main():
	mgr = Manager("Ivan", 5000, 10)
	dev = Developer("Maria", 4000, "Python", 5)

	print("--- Manager Actions ---")
	mgr.show_info()
	mgr.work()
	mgr.hold_meeting()

	print("\n--- Developer Actions ---")
	dev.show_info()
	dev.work()
	dev.write_code()

if __name__ == "__main__":
	main()