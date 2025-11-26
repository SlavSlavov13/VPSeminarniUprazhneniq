my_dict = {"first_one": "можем да го направим"}

def biggest_dict(**kwargs):
	my_dict.update(kwargs)
	return my_dict

print(biggest_dict(name="Иван", age=25, city="София"))
print(biggest_dict(country="Bulgaria", hobby="четене"))