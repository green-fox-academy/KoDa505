#create a function that returns its factorial

def factorial1(numb):
    output = 1
    i = 1
    while i <= numb:
        output *= i
        i += 1
    return output

print(factorial1(6))


def factorial(numb):
    fact = 1
    for n in range(1, numb+1):
        fact *= n
    return fact


print(factorial(6))


def factorial2(numb):
    if numb == 1:
        return 1
    else:
        return factorial2(numb-1) * numb

print(factorial2(6))
