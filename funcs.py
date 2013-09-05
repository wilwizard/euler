from __future__ import division
import math
import bisect
import itertools
import fractions
import datetime
import re



def phi(n):
    #returns the number of intergers less than n that are coprime to n
    n=int(n)
    k=0
    if n==1:
        return 1
    for x in range(1,n):
        if gcd(x,n)==1:
            k+=1
    return k

def gcd(*args):
    nums=list(args)
    if len(nums)==1:
        return nums[0]
    else:
        gcd=fractions.gcd(nums[0],nums[1])
        for x in nums[2:]:
            gcd=fractions.gcd(gcd,x)
            if gcd==1:
                break
        return gcd
        
def lcm(*args):
    nums=list(args)
    if len(nums)==1:
        return nums[0]
    else:
        lcm=1
        for x in nums:
            lcm=x*lcm//fractions.gcd(lcm,x)
        return lcm


def mandel_color(c,max_iter):
    z=0
    iter=0
    for x in range(max_iter):
        z=z**2+c
    return abs(z)
    
def is_prime(num):
    t0=time.time()
    k=1
    if num==1:
        return False
    elif num==2 or num==3:
        return True
    elif num%2==0 or num%3==0:
        return False
    while 6*k-1<=math.sqrt(num):
        if num%(6*k-1)==0 or num%(6*k+1)==0:
            return False
        k+=1
    #print time.time()-t0
    return True

def is_pala(array):
    if array==array[::-1]:
        return True
    else:
        return False
    
def is_pandig(num,digit):
    array=[int(x) for x in list(str(num))]
    array.sort()
    if array==range(1,digit+1):
        return True
    else:
        return False
        
def is_tri(t):
	n=(math.sqrt(8*t+1)-1)/2
	if n%1==0:
		return True
	else:
		return False
        
def is_penta(p):
    n=(math.sqrt(24*p+1)+1)/6
    if n%1==0:
		return True
    else:
		return False
        
def is_hex(h):
    n=(math.sqrt(1+8*h)+1)/4
    if n%1==0:
		return True
    else:
		return False  
        
def is_squ(s):
    n=math.sqrt(s)
    if n%1==0:
		return True
    else:
		return False  
        
def is_hept(h):
    n=(math.sqrt(9+40*h)+3)/10
    if n%1==0:
		return True
    else:
		return False
        
def is_oct(h):
    n=(math.sqrt(4+12*h)+2)/6
    if n%1==0:
		return True
    else:
		return False
        
	
def factorial(num):
	total = 1
	for x in range(1,num+1):
		total*=x
	return total
	
def digitsum(x):  
    total=0  
    for letter in str(x):  
        total+=int(letter)  
    return total  
   
def triangle(num):
	total = .5*num*(num+1)
	return int(total)
    
def pentagonal(n):
    total=n*(3*n-1)/2
    return int(total)

def nCr(n,r):
	return int(factorial(n)/(factorial(r)*factorial(n-r)))

def nPr(n,r):
	return int(factorial(n)/factorial(n-r))

def divisors(num):
	divs = []
	for x in range(2,int(math.sqrt(num))+1):
		if (num/x % 1.0 == 0):
			divs.append(x)
			divs.append(int(num/x))
	divs = list(set(divs))
	divs.sort()
	return divs
	
def prime_facts(num):
    t0 = time.time()
    temp=num
    facts=[]
    x=2
    while not (is_prime(temp) or temp==1):
        if is_prime(x):
            print x
            while temp/x%1.0==0:
                temp//=x
                facts.append(x)
        x+=1
    if is_prime(temp):
        facts.append(temp)
    print time.time() - t0
    return list(set(facts))
    #to return a factorized version of the number,
    #remove the list(set()) function in the return value
    #i.e. prime_facts(360) -> [2,2,2,3,3,5] and not [2,3,5] 
	
def name_val(word):
	total = 0
	for x in list(word):
		total+=int(ord(x.upper())-64)
	return total
	
def permu(array):
	ret_array = []
	temp_array = []
	if len(array)==2:
		ret_array.append(str(min(array))+str(max(array)))
		ret_array.append(str(max(array))+str(min(array)))
		return ret_array
	else:
		array.sort()
		for x in array:
			temp_array = array[:]
			temp_array.remove(x)
			for y in permu(temp_array):
				ret_array.append(str(x)+str(y))		
		return ret_array
					
def prod(array):
	total=1
	for x in array:
		total*=x
	return total	
    
def change(n):
    n*=100
    
    quarters=n//25
    n%=25
    
    dimes=n//10
    n%=10
    
    nickels=n//5
    n%=5
    
    pennies=n
    
    if quarters: print 'Quarters:', int(quarters)
    if dimes: print 'Dimes:', int(dimes)
    if nickels: print 'Nickels:', int(nickels)
    if pennies: print 'Pennies:', int(pennies)
    
def print_time(format_string):
    
    now=datetime.datetime.now()
    
    year=now.year
    month=now.month
    day=now.day
    
    hour24=now.hour
    hour=hour24%12
    if hour<1:
        hour+=12

    if hour24<12:
        ampm='AM'
    else:
        ampm='PM'
    
    minute=now.minute
    second=now.second
    ms=now.microsecond//1000
    
    format_string=re.sub('%l',str(ms), format_string)
    format_string=re.sub('%s',str(second), format_string)
    format_string=re.sub('%m',str(minute), format_string)
    format_string=re.sub('%h',str(hour24), format_string)
    format_string=re.sub('%H',str(hour), format_string)
    format_string=re.sub('%c',str(ampm), format_string)
    format_string=re.sub('%d',str(day), format_string)
    format_string=re.sub('%M',str(month), format_string)
    format_string=re.sub('%y',str(year), format_string)
    
    
    print str(format_string)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    