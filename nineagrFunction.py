students = [] 

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    print(students_titlecase)

def add_student(name, student_id=34):
    student = {"name":name, "student_id":student_id}
    students.append(student)

# we can pass muliple values in *args
def with_args(name, *args):
    print(name)
    print(args)

# we can pass multiple value with key in **kwargs
def with_kwargs(name, **kwargs):
    print(name)
    print(kwargs)
    print(kwargs["city"], kwargs["country"])

#students_list = get_students_titlecase()

#add_student(student_id=10,name="shaheela")
#print(students)
#print_students_titlecase()

#print("this is sout from get", students_list)

#with_args("shaheela","loves python", 57, None, "hi")

#with_kwargs("aakash", city="london", country="UK")