
def get_fizzish(number, base):
    return number % base == 0 or str(base) in str(number)

def fizz_buzz(minimum, maximum):
    fizz_number = 3
    buzz_number = 5
    n = minimum
    while n <= maximum:
        if get_fizzish(n, fizz_number) and get_fizzish(n, buzz_number):
            print('fizzbuzz')
        elif get_fizzish(n, fizz_number):
            print('fizz')
        elif get_fizzish(n, buzz_number):
            print('buzz')
        else:
            print(n)
        n += 1

fizz_buzz(5, 70)
