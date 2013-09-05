from __future__ import division
from sys import argv
import funcs
import fractions
import itertools

bank=range(1,11)

for x in itertools.permutations(bank,3):
    a1=list(x)
    if sum(a1)==16:
        temp1=bank[:]
        for a in a1:
            temp1.remove(a)
        for y in itertools.permutations(temp1,2):
            a2=list(y)
            if sum(a2)+a1[2]==16:
                temp2=temp1[:]
                for a in a2:
                    temp2.remove(a)
                for z in itertools.permutations(temp2,2):
                    a3=list(z)
                    if sum(a3)+a2[1]==16:
                        temp3=temp2[:]
                        for a in a3:
                            temp3.remove(a)
                        for w in itertools.permutations(temp3,2):
                            a4=list(w)
                            if sum(a4)+a3[1]==16:
                                temp4=temp3[:]
                                for a in a4:
                                    temp4.remove(a)
                                if temp4[0]+a4[1]+a1[1]==16:
                                    #print a1,a2,a3,a4,temp4
                                    magic=[]
                                    magic.append(a1)
                                    magic.append([a2[0],a1[2],a2[1]])
                                    magic.append([a3[0],a2[1],a3[1]])
                                    magic.append([a4[0],a3[1],a4[1]])
                                    magic.append([temp4[0],a4[1],a1[1]])
                                    print magic
                                    
                                    


        