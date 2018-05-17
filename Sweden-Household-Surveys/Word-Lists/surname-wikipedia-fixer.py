import sys
import codecs
readList = []
fileList = []
with open("tempsurnames.txt", 'r', encoding='utf-8') as read_file:	
	for line in read_file:
		if '(' in line:
			line = line.split('(')
			line = line[0] +'\n'
		if 'family'.lower() in line:
			line = line.replace('family', '')
		line = line.replace(' ', '')
		if len(line) > 2:
			readList.append(line.encode('utf-8'))
with open("Occupations.txt", "r", encoding='utf-8') as the_file:

	for line in the_file:
		fileList.append(line.encode('utf-8'))
with open("Occupations.txt", "a", encoding='utf-8') as the_file:
	for item in readList:
		if item in fileList:
			print("already")
		else:
			the_file.write(item.decode('utf-8'))

print(readList)
print(fileList)
				
