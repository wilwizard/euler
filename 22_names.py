from __future__ import division
from sys import argv
import funcs

script, filename = argv
file = open(filename)
file2 = open('outfile.txt','w')
line = file.readline()
names = line.split('","')
names.sort()

total = 0
for x in names:
	temp = 0
	for letter in x:
		temp+=ord(letter)-64
	file2.write(x+':'+str(temp)+':'+str(names.index(x)+1)+'\n')
	total+=temp*(names.index(x)+1)
print total