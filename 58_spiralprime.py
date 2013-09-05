from __future__ import division
from sys import argv
import funcs

script, limit = argv
limit = int(limit)/100

    
percent=1
current_number=1
adder=0
prime_count=0
total_count=1

while percent>limit:
    adder+=2
    
    current_number=current_number+adder
    if funcs.is_prime(current_number):
        prime_count+=1

    current_number=current_number+adder
    if funcs.is_prime(current_number):
        prime_count+=1

    current_number=current_number+adder
    if funcs.is_prime(current_number):
        prime_count+=1
        
    current_number=current_number+adder
    
    total_count+=4
    percent=prime_count/total_count
    print prime_count,total_count

print adder+1