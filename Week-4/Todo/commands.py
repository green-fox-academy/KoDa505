#my_file = open('todos.txt')

#list = my_file.read()

#my_file.close()

#print(list)


items = [
        {'task': 'vegyel tejet', 'state': 'todo'},
        {'task': 'takarits', 'state': 'todo'},
        {'task': 'fizesd be a szamlat', 'state': 'completed'},
    ]


def print_todos(items):
    for i in items:
        if i['state'] == 'todo':
            print(i['task'])


def new_element(items):
    addition = input('Enter the new task: ')
    items.append({'task': addition, 'state': 'todo'})

def print_completed(items):
    for i in items:
        if i['state'] == 'completed':
            print(i['task'])

def print_in_progress(items):
    for i in items:
        if i['state'] == 'inprogress':
            print(i['task'])


def order_todos(items):
    orderedtodo = []
    for i in items:
        if i['state'] == 'todo' or i['state'] == 'inprogress':
            orderedtodo.append(i['task'])
    return orderedtodo


def complete_task(items):
    orderedtodo = order_todos(items)
    print('Which task did you complete?')
    print('0. Back')
    j = 1
    for i in orderedtodo:
        print(str(j) + '. ' + i)
        j += 1
    index = int(input('Enter the number of the task that you completed: ')) -1
    if index == -1:
        print('Back to main menu')
    for task in items:
        if task['task'] == orderedtodo[index]:
            task['state'] = 'completed'

def remove_task(items):
    j = 1
    for i in items:
        print(str(j) + '. ' + i['task'])
        j += 1
    index = int(input('Enter the number of the task that you want to remove: ')) -1
    items.pop(index)


donelist = []
def print_donelist(items):
    for i in items:
        if i['state'] == 'completed':
            donelist.append(i['task'])
    print(donelist)
