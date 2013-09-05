from sys import argv

script, filename = argv

file = open(filename, 'r')
line = ' '
array = []
while line:
	line = file.readline()
	line = line.rstrip()
	temp = line.split()
	temp = map(int, temp)
	if temp == []:
		break
	array.append(temp)
for x in range(len(array)-2,-1,-1):
	for y in range(len(array[x])):
		array[x][y] += max(array[x+1][y],array[x+1][y+1])
	array.pop()
	
print array