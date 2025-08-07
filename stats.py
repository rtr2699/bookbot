def get_num_words(text):
    total = len(text)
    return total


def character_count(book):
	chars = book.lower()
	characters_list = {}
	for char in chars:
		if char in characters_list:
			characters_list[char] = characters_list[char] + 1
		else:
			characters_list[char] = 1
	return characters_list


def sort_on(char):
	return  char["num"]

def get_sorted_characters(characters_list):
	letters = []

	for char in characters_list:

		letters.append({"char": char, "num": characters_list[char]})

	letters.sort(reverse=True, key=sort_on)
	return letters

