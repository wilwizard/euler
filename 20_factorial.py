from __future__ import division
from sys import argv
import funcs

script, number = argv
number = int(number)

fact = funcs.factorial(number)
print funcs.digitsum(fact)