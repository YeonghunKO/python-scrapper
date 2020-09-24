# 계산기

def plus (a,b):
    x = float(a)
    y = float(b)
    return x + y
def minus(a,b):
    x = float(a)
    y = float(b)
    return x - y
def multiple(a,b):
    x = float(a)
    y = float(b)
    return x * y
def division (a,b):
    x = float(a)
    y = float(b)
    return x / y
def remainder(a,b):
    x = float(a)
    y = float(b)
    return x % y
def power(a,b):
    x = float(a)
    y = float(b)
    return x ** y
def negation(a):
    x = float(a)
    y = -x
    return y
    

r_plus = plus(1.2 , "1.5")
print(r_plus)

r_division = division(5, "1.6")
print(r_division)

r_negation = negation("9.4")
print(r_negation)


