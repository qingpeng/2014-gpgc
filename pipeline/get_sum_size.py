file_in = open('ls.log','r')
all = 0
for line in file_in:
	line = line.rstrip()
	fields = line.split()
	all = all + int(fields[4])
	
print all

