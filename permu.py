import math
from collections import Counter

def combination(n, r, coma=False):
    nf = math.factorial(n)
    rf = math.factorial(r)
    m = n - r
    mf = math.factorial(m)
    tf = mf * rf
    result = nf / tf
    if coma: return (f"{int(result):,}")
    elif coma == False: return int(result)

def permutationword(word, coma=False):
    n = len(word)
    fn = math.factorial(n)
    x = Counter(word)
    result = 1
    for j in x.values(): result *= math.factorial(j)
    total = fn / result
    if coma: return (f"{int(total):,}")
    elif coma == False: return  int(total)

def permutationint(n, *args, coma=False):
    fn = math.factorial(n)
    result = 1
    for i in args: result *= math.factorial(i)
    if coma: return (f"{int(fn / result):,}")
    elif coma == False: return int(fn / result)

def circle(n, counterc=False, coma=False):
    result = n - 1
    x = math.factorial(result)
    if counterc:
        if coma: return (f"{int(x / 2):,}")
        elif coma == False: return int(x / 2)
    elif counterc == False:
        if coma: return (f"{x:,}")
        elif coma == False: return x

def permutationwo(n, r, coma=False):
    c  = math.factorial(n)
    t = n - r
    j = math.factorial(t)
    p = c / j
    if coma: return (f"{int(p):,}")
    elif coma == False: return (int(p))


def factorial(n, coma=False):
   permu = math.factorial(n)
   if coma: return (f"{permu:,}")
   elif coma == False: return (permu)



