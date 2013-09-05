from __future__ import division
from sys import argv
import funcs

script, filename = argv
file = open(filename)
file2 = open('outfile.txt','w')
line = file.readline()
words = line.split('","')
words.sort()

total = 0
for x in words:
	temp = 0
	for letter in x:
		temp+=ord(letter)-64
	file2.write(x+':'+str(temp)+':'+str(words.index(x)+1)+'\n')
	if funcs.is_tri(temp):
		total+=1
print total