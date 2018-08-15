students = []

class Student:
    def add_student(self, name, student_id=344):
        student = {"name":name, "student_id": student_id}
        students.append(student)




python = Student()
python.add_student("john")

print(students)

student = Student()

print(student)

newStudent = Student()
print(newStudent)


