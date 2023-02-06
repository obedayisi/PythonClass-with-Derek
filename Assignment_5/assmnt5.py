myfile = open('swallows.txt', 'r')
print("ARTHUR\t")
for line1 in myfile:
	if line1.startswith('ARTHUR'):
		sentence1 = line1.split(':')
		actor1 = sentence1.pop(0)
		print(sentence1)
print('\n')
print("SOLDIER #1")
myfile.close()

myfile = open('swallows.txt')
for line in myfile:
	#print(line)
	if line.startswith('SOLDIER'):
		sentence2 = line.split(':')
		actor2 = sentence2.pop(0)
		print(sentence2)


