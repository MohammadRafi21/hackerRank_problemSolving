no_student = int(input())
students = []
for i in range(no_student):
    name = input()
    marks = float(input())
    newList = [name,marks]
    students.append(newList)

grade = [student[1] for student in students]

lowest = min(grade)
grade2 = [i for i in grade if i != lowest]

second_lowest = min(grade2)
sec_student = [student[0] for student in students if student[1]==second_lowest]
sec_student.sort()
for i in sec_student:
    print(i)