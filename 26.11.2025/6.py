def process_fruit_names(fruit_list):
	processed_list = []

	for fruit in fruit_list:
		mid_index = len(fruit) // 2
		half_word = fruit[:mid_index]
		processed_list.append(half_word)

	processed_list.sort()
	return processed_list

fruits = ["Банан", "Ябълка", "Портокал", "Киви"]
print(f"Обработен списък: {process_fruit_names(fruits)}")