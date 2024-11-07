# BinduMath.py
from mpmath import mp # type: ignore

def printBigpi(n):
    mp.dps = n + 1  
    return str(mp.pi)  
print(printBigpi(10))
    