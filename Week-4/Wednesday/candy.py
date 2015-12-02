students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Teodor', 'age': 3, 'candies': 2}
    ]

#create a function that counts the students that has more than four candies


def count_rich_students(studentlist):
    rich = 0
    for student in studentlist:
        if student['candies'] > 4:
            rich += 1
    return rich

print(count_rich_students(students))

def is_rich(kid):
    return kid['candies'] > 4

def filter_rich_students(studentlist):
    return len(list(filter(is_rich, studentlist)))

def rich_kids_oneline(people):
    return len(list(filter(lambda x: x['candies'] > 4, people)))

print(filter_rich_students(students))
print(rich_kids_oneline(students))
