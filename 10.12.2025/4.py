class Products:
	def __init__(self, name, price):
		self.name = name
		self.price = price

	def reduce_price(self, percent):
		discount = self.price * (percent / 100)
		self.price -= discount
		print(f"Цената е намалена с {percent}%. Нова цена: {self.price:.2f} лв.")

	def show_info(self):
		print(f"Продукт: {self.name}, Цена: {self.price:.2f} лв.")

class Kniga(Products):
	def __init__(self, name, price, publisher, genre):
		super().__init__(name, price)
		self.publisher = publisher
		self.genre = genre

	def read_excerpt(self):
		print(f"Чета откъс от книгата '{self.name}'...")

	def show_info(self):
		super().show_info()
		print(f"Издателство: {self.publisher}, Жанр: {self.genre}")

class Electronics(Products):
	def __init__(self, name, price, warranty_months, power):
		super().__init__(name, price)
		self.warranty_months = warranty_months
		self.power = power

	def turn_on(self):
		print(f"Уредът '{self.name}' е включен.")

	def show_info(self):
		super().show_info()
		print(f"Гаранция: {self.warranty_months} месеца, Мощност: {self.power}W")

def main_task4():
	print("\n--- ЗАДАЧА 4 DEMO ---")

	my_book = Kniga("Pod Igoto", 25.00, "Prosveta", "Historical Fiction")
	my_book.show_info()
	my_book.read_excerpt()
	my_book.reduce_price(10)

	print("-" * 20)

	my_device = Electronics("Microwave Samsung", 150.00, 24, 800)
	my_device.show_info()
	my_device.turn_on()
	my_device.reduce_price(20)

if __name__ == "__main__":
	main_task4()