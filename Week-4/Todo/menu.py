import todo
import beolvasas

items = beolvasas.load('todos.txt')

menu = [
 '1. what to do this week?',
 '2. add new task',
 '3. complete a task',
 '4. remove a task',
 '5. exit menu'
]

while True:
    for i in menu:
        print(i)
    try:
        choice = int(input("Choose a task: "))
        print('----' * 10)
    except ValueError:
        print('You have to enter the number of your choice')
    else:
        if choice == 1:
            todo.print_todos(items)
            print('--' *16)
        if choice == 2:
            todo.new_element(items)
        if choice == 3:
            todo.complete_task(items)
        if choice == 4:
            todo.remove_task(items)
        if choice == 5:
            beolvasas.save(items, 'todos.txt')
            exit()
