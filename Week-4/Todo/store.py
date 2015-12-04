
def load(filename):
    my_file = open(filename)

    text = my_file.readlines()
    my_file.close()

    tagok = []
    items = []
    for line in text:
        line = line.rstrip("\n")
        tagok = line.split('#')
        items.append({'task': tagok[0], 'state': tagok[1], 'duedate': tagok[2]})

    return(items)




def save(items,filename):
    my_file = open(filename, 'w')
    for item in items:
        line = "{}#{}#{}\n".format(item['task'], item['state'], item['duedate'])
        my_file.write(line)
    my_file.close()
