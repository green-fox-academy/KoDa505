


def create_numb(oneish, fiveish, tenish, arabint):
    roman_int = ''
    if arabint <= 3:
        roman_int = arabint*oneish
    if arabint == 4:
        roman_int = oneish + fiveish
    if arabint == 5:
        roman_int = fiveish
    if arabint > 5 and arabint <= 8:
        roman_int = fiveish + (arabint-5)*oneish
    if arabint == 9:
        roman_int = oneish + tenish
    return roman_int



def roman_num(number):
    original_number = number
    conv = ''
    if number > 3999:
        print("This number cannot be converted to Roman numeral")
        return
    m = number // 1000
    number = number - (m*1000)
    conv = conv + (m * 'M')
    c = number // 100
    number = number - (c*100)
    conv = conv + create_numb('C', 'D', 'M', c)
    x = number // 10
    number = number - (x*10)
    conv = conv + create_numb('X', 'L', 'C', x)
    i = number
    conv = conv + create_numb('I', 'V', 'X', i)
    print(str(original_number) + ' = ' + conv)
    return conv

while True:
    try:
        decimal_int = int(input('Enter a number between 1 and 3999: '))
    except ValueError:
        print('You have to enter a decimal number')
    else:
        if decimal_int < 0:
            print('You have to enter a positive integer')
        elif decimal_int > 3999:
            print('You have to enter a smaller number')
        else:
            roman_num(decimal_int)
            break
