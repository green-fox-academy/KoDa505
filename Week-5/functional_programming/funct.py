

def adder0(array):   #ez volt az eddigi megoldas
    newlist = []
    for element in array:
        newlist.append(element+1)
    return newlist

def adder0(array):
    def add(n):
        return n+1
    return list(map(add, array))

def adder(array):
    return list(map(lambda x: x+1, array))  #lambdaval ugyanaz a megoldas

def filterArray0(array):
    def dividable_3(n):
        if n % 3 == 0:
            return True       # ugyanaz ha return n%3 ==0
    return list(filter(dividable_3, array))

def filterArray(array):
    return list(filter(lambda x: x % 3 ==0, array))
