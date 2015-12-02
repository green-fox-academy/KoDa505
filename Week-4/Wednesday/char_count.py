

# write a function that reads a file and prints how many lines and characters in it
def counting(filename):
    my_file = open(filename, 'r')
    text = my_file.read()
    my_file.close()
    textlength = (len(text))
    lines = text.split("\n")
    line_numbers = (len(lines))
    return(line_numbers, textlength)

print(counting('zen_of_python.txt'))
