import csv 

with open("student_data.csv") as student_file:
    data = csv.reader(student_file)
    students = []
    for row in data:
        if row[0] != "Students":
            students.append(row[0])
    print(students)