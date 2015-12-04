def is_complete(numbers):
    if len(numbers) != 9:
        return False
    if len(numbers) == 9:
        return True

def integer_checking(numbers):
    for i in numbers:
        if i <=0:
            return False
        if i > 9:
            return False
