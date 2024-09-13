def main():
	book_path = "./books/frankenstein.txt"
	text = get_book_text(book_path)
	num_words = count_words(text)
	char_dict = count_characters(text)
	dict_list = convert_dict_to_list(char_dict)
	print('--- Begin report of books/frankenstein.txt ---')
	print(f'{num_words} words found in the document')
	print()
	dict_list.sort(reverse=True, key=sort_on)
	for dicti in dict_list:
		ch = dicti['char']
		val = dicti['num']
		if ch.isalpha():
			print(f"The '{ch}' character was found {val} times")
	print('--- End report ---')

def sort_on(dict):
	return dict["num"]

def convert_dict_to_list(dicti):
	new_list = []
	for key in dicti:
		new_dict = {}
		new_dict['char'] = key
		new_dict['num'] = dicti[key]
		new_list.append(new_dict)
	return new_list

def get_book_text(path):
	with open(path) as f:
		content = f.read()
		return content

def count_words(text):
	words = text.split()
	return len(words)

def count_characters(text):
	text = text.lower()
	char_dict = {}
	for ch in text:
		if ch in char_dict:
			char_dict[ch] += 1
		else:
			char_dict[ch] = 1
	return char_dict

main()
