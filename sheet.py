# Opening a csv file and arranging the content in form of a List.

with open("student_data.csv") as student_file:
    data = student_file.readlines()
    print(data)