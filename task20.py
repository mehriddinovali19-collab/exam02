def find_shortest_name_student(students: list) -> str:
    shortest = students[0]
    for student in students: 
        if len(student['name']) < len(shortest['name']):
            shortest = student
    return shortest
            


students = [
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Ali', 'age': 18},
    {'name': 'Muhammad', 'age': 21}
]
print(find_shortest_name_student(students))  # {'name': 'Ali', 'age': 18}

students2 = [
    {'name': 'Jo', 'age': 19},
    {'name': 'Ali', 'age': 20},
    {'name': 'Bob', 'age': 18}
]
print(find_shortest_name_student(students2))  # {'name': 'Jo', 'age': 19}