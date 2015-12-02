my_list = open("texts/reversed_zen_lines.txt", 'r')

lines = my_list.readlines()

my_list.close()

reversed = ""
for i in range(len(lines)):
    reversed = reversed + lines[i][::-1]


print(reversed)
