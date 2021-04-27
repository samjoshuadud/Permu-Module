import math
from collections import Counter

def combination(n, r, coma=False):
    nf = math.factorial(n)
    rf = math.factorial(r)
    m = n - r
    mf = math.factorial(m)
    tf = mf * rf
    result = nf / tf
    if coma == True:
        return (f"{int(result):,}")
    elif coma == False:
        return int(result)

def permutationw(word, coma=False):
    n = len(word)
    fn = math.factorial(n)
    x = Counter(word)
    result = 1
    for j in x.values():
        result *= math.factorial(j)
    total = fn / result
    if coma == True:
        return (f"{int(total):,}")
    elif coma == False:
        return  int(total)

def circle(n, counterc=False, coma=False):
    result = n - 1
    x = math.factorial(result)
    if counterc == True:
        if coma == True:
            return (f"{int(x / 2):,}")
        elif coma == False:
            return int(x / 2)
    elif counterc == False:
        if coma == True:
            return (f"{x:,}")
        elif coma == False:
            return x

def permutationwo(n, r, coma=False):
    c  = math.factorial(n)
    t = n - r
    j = math.factorial(t)
    p = c / j
    if coma == True:
        return (f"{int(p):,}")
    elif coma == False:
        return (int(p))


def factorial(n, coma=False):
   permu = math.factorial(n)
   if coma == True:
       return (f"{permu:,}")
   elif coma == False:
       return (permu)



