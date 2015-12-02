my_file = open("texts/reversed_zen_order.txt", 'r')

lines = my_file.readlines()

my_file.close()

reversed = ""
for i in range(len(lines)):
    reversed = lines[i] + reversed


print(reversed)
