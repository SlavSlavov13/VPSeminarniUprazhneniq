def get_most_valuable_item(items):
	if not items:
		return None
	return max(items, key=items.get)

inventory = {
	"Златен часовник": 500,
	"Сребърен пръстен": 150,
	"Диамантена огърлица": 2000,
	"Стара картина": 50
}

print(f"Най-ценният предмет е: {get_most_valuable_item(inventory)}")