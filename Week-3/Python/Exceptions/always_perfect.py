def check_root(string):
    tokens = string.split(",")
    if len(tokens) != 4:
        return 'incorrect input'
    numbers = []
    for token in tokens:
        try:
            numbers.append(int(token))
        except ValueError:
            return "incorrect input"

    for i in range(len(numbers)-1):
        if numbers[i] + 1 != numbers[i+1]:
            return'not consecutive'
    product = 1
    for number in numbers:
        product *= number
    perfect_number = product + 1
    root = int(perfect_number ** 0.5)

    return "{}, {}".format(perfect_number, root)


print(check_root('3,s,5,6'))
print(check_root('11,13,14,15'))
print(check_root('3,s,5,6'))
print(check_root('10,11,12,13,15'))
print(check_root('11,13,14,15'))
print(check_root('4,5,6,7'))
print(check_root('10,11,12,13'))
