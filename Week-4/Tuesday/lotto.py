import csv
from prettytable import PrettyTable

lottery_file = open('otos.csv', 'r')
lottery_reader = csv.reader(lottery_file, delimiter = ';')



history = []
for row in lottery_reader:
    drawn = row[-5:]
    drawn_numbers = []
    for elem in drawn:
        drawn_numbers.append(int(elem))

    history.append(drawn_numbers)

winners = {}
for fivenumbers in history:
    for number in fivenumbers:
        if number in winners:
            winners[number] += 1
        if number not in winners:
            winners[number] = 1

table = PrettyTable(["number", "winners"])
for key in winners:
    table.add_row([key, winners[key]])


print(table.get_string(sortby='winners', reversesort=True))
