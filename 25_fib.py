from __future__ import division
from sys import argv
import funcs

script, limit = argv
limit = int(limit)

prev = 0
current = 1
term = 1
while len(str(current))<limit:
	next=current+prev
	prev = current
	current = next
	term+=1
print term
