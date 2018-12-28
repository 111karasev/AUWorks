import numpy as np
import math
def evk(a, b):
    if b==0:
        return a
    else:
        return evk(b, a%b)

def isNumberPrime(a):
    if a%2==0:
        if a == 2:
            return True
        return False
    i=3
    while i*i<a:
        if a%i==0:
            return False
        i+=2
    return True

def str_base(number, base):
    nums=[]
    while number!=0:
        mod=number%base
        if(mod>=10):
            nums.append(chr(ord('A')+mod-10))
        else:
            nums.append(mod)
        number=number//base
    nums.reverse()
    return ''.join(nums)

def evk_up(a, b):
    if a==0:
        return (b, 0, 1)
    evk, x, y=evk_up(b%a, a)
    return (evk, y-b//a*x, x)
