a = 0

while a < 100:
    if a % 3 == 0 and a % 5 == 0:
        print('Fizzbuzz')
    elif a % 3 == 0:
        print('fizz')
    elif a % 5 == 0:
        print('buzz')
    elif str(3) in str(a) and str(5) in str(a):
        print('Fizzbuzz')
    elif str(3) in str(a):
        print('Fizz')
    elif str(5) in str(a):
        print('buzz')
    else:
        print(a)
    a +=1
