student = []

def write_file(student):
    try:
        
        f = open("student.txt", "a")
        for a in student:
            f.write(a + "\n")
        f.close()
        print("yes i m able to write")
    except Exception:
        print("could not write")


def add_student(name):
    student.append(name)

def read_file():
    try:
        f = open("student.txt", "r")
        for stud in f.readlines():
            add_student(stud)
        f.close()
    except Exception:
        print("could not read")


student_name= input("enter your name")

add_student(student_name)

write_file(student)
read_file()
print(student)