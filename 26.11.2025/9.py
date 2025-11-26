from collections import namedtuple

def good_students(students_tuple):
	total_grade = sum(s.grade for s in students_tuple)
	average_grade = total_grade / len(students_tuple)

	good_ones = [s.name for s in students_tuple if s.grade > average_grade]

	names_string = ", ".join(good_ones)
	print(f"Студентите {names_string} се справят добре този семестър!")

Student = namedtuple('Student', ['name', 'age', 'grade', 'city'])

students_data = (
	Student('Иван', 20, 4.50, 'София'),
	Student('Петър', 21, 5.50, 'Пловдив'),
	Student('Мария', 20, 6.00, 'Варна'),
	Student('Георги', 22, 3.50, 'Бургас'),
	Student('Елена', 21, 5.00, 'София'),
	Student('Александър', 20, 4.00, 'Русе'),
	Student('Виктория', 22, 5.80, 'Пловдив')
)

good_students(students_data)