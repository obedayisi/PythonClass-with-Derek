# create and open a new file
myfile = open("lumberjack.txt",'w')

# we're writing a single line at a time
myfile.write("I'm a lumberjack and I'm OK\n")
myfile.write("I sleep all night and I work all day\n\n")
myfile.write("He's a lumberjack and he's OK\n")
myfile.write("He sleeps all night and he works all day\n\n")
myfile.write("I cut down trees, I eat my lunch")

# closing
myfile.close()

# opening a file, and iterating through 1 line at a time
for line in open("lumberjack.txt"):
	if ("lumberjack" in line):
		print(line)