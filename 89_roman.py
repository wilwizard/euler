from __future__ import division
from sys import argv
import funcs
import fractions

def roman_to_dec(numberals):
    
    num_list=list(numberals)
    for i in range(len(num_list)):
        if num_list[i]=='M':
            num_list[i]=1000
        elif num_list[i]=='D':
            num_list[i]=500
        elif num_list[i]=='C':
            num_list[i]=100
        elif num_list[i]=='L':
            num_list[i]=50
        elif num_list[i]=='X':
            num_list[i]=10
        elif num_list[i]=='V':
            num_list[i]=5
        elif num_list[i]=='I':
            num_list[i]=1
        else:
            num_list[i]=0
           
        
    for i in range(len(num_list)-1):
        if num_list[i+1]>num_list[i]:
            num_list[i]=-num_list[i]
    

    return sum(num_list)

def dec_to_roman(dec):

    numberal=''
    
    
    while dec>0:
        if dec>=1000:
            numberal+='M'
            dec-=1000
        
        elif dec>=900:
            numberal+='CM'
            dec-=900
        
        elif dec>=500:
            numberal+='D'
            dec-=500
        
        elif dec>=400:
            numberal+='CD'
            dec-=400
        
        elif dec>=100:
            numberal+='C'
            dec-=100
        
        elif dec>=90:
            numberal+='XC'
            dec-=90
            
        elif dec>=50:
            numberal+='L'
            dec-=50
            
        elif dec>=40:
            numberal+='XL'
            dec-=40
        
        elif dec>=10:
            numberal+='X'
            dec-=10
        
        elif dec>=9:
            numberal+='IX'
            dec-=9
        
        elif dec>=5:
            numberal+='V'
            dec-=5
        
        elif dec>=4:
            numberal+='IV'
            dec-=4
        
        elif dec>=1:
            numberal+='I'
            dec-=1


    return numberal

script, filename= argv

outfile = open('roman_debug.txt','w')
file = open(filename,'r')
line = file.readline()

total=0

while line:
    numberals = line.rstrip()
    #print numberals
    
    len1=len(numberals)
    val=roman_to_dec(numberals)
    len2=len(dec_to_roman(val))
    
    total+=len1-len2
    
    
    line = file.readline()

print total