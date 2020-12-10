
def mySqrt(x):

    r = x
    precision = 10 ** (-100)
    
    while abs(x - r * r) > precision:
        r = (r + x / r) / 2
        
    return r

print(mySqrt(2))