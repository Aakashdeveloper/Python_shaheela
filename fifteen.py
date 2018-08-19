students = []


class Student:

    school_name = 'sant marry'

    def __init__(self, name, student_id=29):
        self.name =name;
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student"+self.name

    def get_name_capitalize(self):
        return self.school_name.capitalize()

    def get_school_name(self):
        return self.school_name


mark = Student("Mark")
print(mark.get_name_capitalize())
print(mark.get_school_name())
print(Student.school_name)

# print(students)
# sum1 = mark.add(3)
# print(sum1)