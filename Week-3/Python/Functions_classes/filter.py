numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def even(mylist):
    evens = []
    for i in mylist:
        if i % 2 == 0:
            evens.append(i)
    return evens

evens = even(numbers)
print(evens)


# van egy masik lehetoseg is, akkor globalis valtozonak adja meg
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

evens = []

def even(mylist):
    for i in mylist:
        if i % 2 == 0:
            evens.append(i)
    
even(numbers)
print(evens) """
