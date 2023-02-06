myfile = open('swallows.txt')
for line in myfile:
    if line.startswith('ARTHUR'):
        print(line)
