import commands
import store

items = store.load('todos.txt')

menu = [
 '1. What you have to do this week',
 '2. Add new task',
 '3. What you have started',
 '4. How much time do you have?',
 '5. How lazy were you?',
 '6. Complete a task',
 '7. What you have done',
 '8. Remove a task',
 '9. Exit menu'
]

while True:
    for i in menu:
        print(i)
    try:
        print('----' * 10)
        choice = int(input("Choose a task: "))
        print('----' * 10)
    except ValueError:
        print('You have to enter the number of your choice')
    else:
        if choice == 1:
            commands.print_todos(items)
            print('--' *16)
        if choice == 2:
            commands.new_element(items)
        if choice == 3:
            commands.print_in_progress(items)
        if choice == 4:
            commands.remaining_time(items)
        if choice == 5:
            commands.expiring(items)
        if choice == 6:
            commands.complete_task(items)
        if choice == 7:
            commands.print_completed(items)
        if choice == 8:
            commands.remove_task(items)
        if choice == 9:
            store.save(items, 'todos.txt')
            exit()
        if choice == 10:
            for item in items:
                print(item)
            
