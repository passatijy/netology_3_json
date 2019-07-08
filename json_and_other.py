import sys
import xml
import json
import xml.etree.ElementTree as ET

def parse_xml(filename):
	with open (filename, encoding = 'UTF8') as f:
		data =ET.parse(f).getroot()
	longtext = ''
	for description in data.iter('description'):
		longtext = longtext + description.text
	return longtext.lower().split()

def parse_json(filename):
	with open (filename, encoding = 'UTF8') as f:
		data =json.load(f)
		longtext = ''
		for elem in data['rss']['channel']['items']:
			longtext = longtext + elem['description']
		return longtext.lower().split()

def count_words(inp_list, chars):
	i = 0
	counter_dict = {}
	for word in inp_list:
		counter = 0
		for otherword in inp_list:
			if len(word) >= chars:
				if word == otherword:
					counter = counter + 1
					inp_list.remove(otherword)
		counter_dict[word] = counter
		i = i + 1
	return counter_dict

def search_most_used_word(inp_list):
	rev_sorted = sorted(inp_list.items(), key = lambda kv: (kv[1],kv[0]), reverse = True)
	return rev_sorted

def print_result(count, inp_list):
	i = 0 
	while i < count :
		print('Top used word: ', inp_list[i][0],' used: ', inp_list[i][1])
		i = i+1

# вызываю парсинг xml, параметры - имя файла, длинна слова для подсчета
file = 'newsafr.xml'
dict_with_word = count_words(parse_xml(file),6)
result_list = search_most_used_word(dict_with_word)
# печатаю результат, функция вывода принимает количество топовых слов и список результатов
print('From xml:')
print_result(10,result_list)

# вызываю парсинг json, параметры - имя файла, длинна слова для подсчета
file = 'newsafr.json'
dict_with_word = count_words(parse_json(file),9)
result_list = search_most_used_word(dict_with_word)
# печатаю результат, функция вывода принимает количество топовых слов и список результатов
print('From json:')
print_result(10,result_list)