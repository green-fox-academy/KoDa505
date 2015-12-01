

"""
def split_the_bill(x):
    summa = 0
    for i in x:
        print(i)


split_the_bill({'A': 20, 'B': 15, 'C': 10})"""

x = {'A': 20, 'B': 15, 'C': 10}
summa = 0

for key, value in x.items():
    summa += value
    one_person = summa / len(x)
print(summa)
print(len(x))

for key, value in x.items():
    



"""
for key, value in x.items():
    print(value)
    print(key)
"""
