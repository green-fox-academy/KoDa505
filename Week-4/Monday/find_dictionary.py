students = [
    {'name':'Tibi', 'age': 8},
    {'name':'Adorjan', 'age': 9},
    {'name':'Agoston', 'age': 6},
    {'name':'Aurel', 'age': 7},
    {'name':'Dezso', 'age': 12}
]


students_at_least_8 = []
for student in students:
    if student['age'] >= 8:
        students_at_least_8.append(student['name'])

print(students_at_least_8)


student_ages_starting_with_A = []
for i in students:
    if i['name'][0] == 'A':
        student_ages_starting_with_A.append(i['age'])

print(student_ages_starting_with_A)
