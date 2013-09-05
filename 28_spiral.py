from __future__ import division
from sys import argv
import funcs

script, num = argv
file = open('outfile.txt','w')
grid_size = int(num)
xcord = int(grid_size/2)
ycord = int(grid_size/2)
num=1
total=0
grid=[]

for x in range(grid_size):
	grid.append(grid_size*[0])

for x in range(1,grid_size):
	#right and down
	if(x%2==1):
		#right
		for i in range(x):
			grid[ycord][xcord]=num
			xcord+=1
			num+=1
		#down
		for i in range(x):
			grid[ycord][xcord]=num
			ycord+=1
			num+=1
	if(x%2==0):
		#left
		for i in range(x):
			grid[ycord][xcord]=num
			xcord-=1
			num+=1
		#up
		for i in range(x):
			grid[ycord][xcord]=num
			ycord-=1
			num+=1

for x in range(grid_size):
	grid[ycord][xcord]=num
	xcord+=1
	num+=1
for x in grid:
	print x

for x in range(grid_size):
	total+=grid[x][x]
	total+=grid[grid_size-x-1][x]
total-=1
print total
	
	