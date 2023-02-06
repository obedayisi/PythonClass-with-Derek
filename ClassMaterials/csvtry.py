# create and open a new file
myfile = open("lumberjack.csv",'w')

# we're writing a single line at a time
myfile.write("I'm a lumberjack and I'm OK,")
myfile.write("I sleep all night and I work all day,")
myfile.write("He's a lumberjack and he's OK,")
myfile.write("He sleeps all night and he works all day,")
myfile.write("I cut down trees, I eat my lunch,")

# closing
myfile.close()

# opening a file, and iterating through 1 line at a time
#for line in open("lumberjack.csv"):
	#if ("lumberjack" in line):
		#print(line)