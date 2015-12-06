import datetime
import dtimes
import time

def print_todos(items):
    for i in items:
        if i['state'] == 'todo':
            print(i['task'])


def new_element(items):
    addition = input('Enter the new task: ')
    duedate = dtimes.duedate()
    items.append({'task': addition, 'state': 'todo', 'duedate': duedate})

def print_completed(items):
    for i in items:
        if i['state'] == 'completed':
            print(i['task'])

def print_in_progress(items):
    for i in items:
        if i['state'] == 'inprogress':
            print(i['task'])


def order_todos_and_inprogresses(items):
    orderedtodo = []
    for i in items:
        if i['state'] == 'todo' or i['state'] == 'inprogress':
            orderedtodo.append(i['task'])
    return orderedtodo

def order_todos(items):
    orderedtodo = []
    for i in items:
        if i['state'] == 'todo':
            orderedtodo.append(i['task'])
    return orderedtodo



def complete_task(items):
    orderedtodo = order_todos_and_inprogresses(items)
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

def make_task_inprogress(items):
    orderedtodo = order_todos(items)
    print('Which task have you started?')
    print('0. Back')
    j = 1
    for i in orderedtodo:
        print(str(j) + '. ' + i)
        j += 1
    index = int(input('Enter the number of the task that you have started: ')) -1
    if index == -1:
        print('Back to main menu')
    for task in items:
        if task['task'] == orderedtodo[index]:
            task['state'] = 'inprogress'

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



def remaining_time(items):
    j = 1
    for i in items:
        print(str(j) + '. ' + i['task'])
        j += 1
    index = int(input('Enter the number of the task: ')) -1
    duedatestring = items[index]['duedate']
    duedate = datetime.datetime.strptime(duedatestring, '%Y-%m-%d %H:%M:%S')
    start = datetime.datetime.today()
    delta = duedate-start
    print("---" * 10)
    print(delta)
    print("---" * 10)


def expiring(items):
    for item in items:
        if item['state'] == 'todo' or item['state'] == 'inprogress':
            duedatestring = item['duedate']
            duedate = datetime.datetime.strptime(duedatestring, '%Y-%m-%d %H:%M:%S')
            start = datetime.datetime.today()
            if start > duedate:
                print("! ! ! " * 10)
                print(item['task'] + ' ' + item['duedate'])
                print("laziness alarm!  " * 3)
                print("! ! ! " * 10)
