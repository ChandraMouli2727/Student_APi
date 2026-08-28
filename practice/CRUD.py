import json
print("Student Management System\n")

with open('students.json','r') as f:
        students = json.load(f)

'''students = [
    {"id":1,"name":"Chandra","email":"chandra@example.com","marks":[99,80,85]},
    {"id":2,"name":"Mouli","email":"mouli@example.com","marks":[29,40,85]},
    {"id":3,"name":"Arjun","email":"arjun@example.com","marks":[39,80,95]}
]'''
def calculate_average(marks):
    if marks is None or len(marks) == 0:
        return 0
    avg = round(sum(marks)/len(marks),2)
    return avg

def calculate_grade(average):
    if not isinstance(average,(int,float)):
        return "Avg NO must be Number Data Type"
    if average >= 80:
        return 'A'
    elif average >= 60:
        return 'B'
    else:
        return 'C'

print(calculate_grade("Hello"))
def student_summary(dt):
   if(len(dt)) == 0:
       return "No elements found"
   if dt['marks'] is None or len(dt['marks']) == 0:
        return "mark List contains atleast 1 element"
   avg = calculate_average(dt['marks'])
   grade = calculate_grade(avg)
   return {'Name':dt['name'],'Email':dt['email'],'Average':avg,'Grade':grade}

def find_topper(stds):
    summary_list = []
    for std in stds:
       std_summ = student_summary(std)
       summary_list.append((std['name'],std_summ['Average'],std_summ['Grade']))
    max_avg = max(summary_list,key = lambda x: x[1])
    print("=== Topper ===\n")
    print(f'Name : {max_avg[0]}\n Average : {max_avg[1]}\n Grade : {max_avg[2]}')

find_topper(students)

def find_lower(stds):
    summary_list = []
    for std in stds:
       std_summ = student_summary(std)
       summary_list.append((std['name'],std_summ['Average'],std_summ['Grade']))

    min_avg = min(summary_list,key = lambda x: x[1])
    print("=== lower ===\n")
    print(f'Name : {min_avg[0]}\n Average : {min_avg[1]}\n Grade : {min_avg[2]}')

find_lower(students)


def find_students_by_grade(students, grade):
    matching_students  = []
    for std in students:
       std_summ = student_summary(std)
       if std_summ['Grade'] == grade:
            matching_students .append((std['name'],std_summ['Average'],std_summ['Grade']))
           # print(f'{std['name']} -> {avg} -> {grade}')
    return matching_students 

grd = find_students_by_grade(students, "C")
requested_grade = 'C'
print(f'=== Grade {requested_grade} Students ===\n')
if len(grd) == 0:
    print("NO students found")
else:
    for name, marks, grade in grd:
        print(f"{name} → {marks} → {grade}")

def display_student_summary():
    print("=== Student Summary ===\n")
    for student in students:
        summary = student_summary(student)
        print(summary)

def student_validation():
    student_name = input("Enter student Name\n")
    if not student_name:
        return "Student name is required"

    email = input("Enter student Email\n")
    if not email:
        return "Email is required"

    marks = input("Enter marks separated by comma\n")
    if not marks:
        return "At least 1 subject mark is required"

    ll = []
    for i in marks.split(','):
        if not i.strip():
            return "Mark cannot be empty"
        try:
            a = int(i.strip())
        except ValueError:
            return f"Invalid mark: {i}"
        if not 0 <= a <= 100:
            return "Mark must be between 0 and 100"
        ll.append(a)

    return student_name, email, ll


def add_student():
    result = student_validation()
    if isinstance(result, str):
        print(result)
        print("Student NOT added")
        return

    student_name, email, marks = result
    next_id = max((std['id'] for std in students), default=0) + 1
    student = {
        'id': next_id,
        'name': student_name,
        'email': email,
        'marks': marks
    }

    students.append(student)

    with open('students.json', 'w') as f:
        json.dump(students, f, indent=4)

    print("=== Student Added ===\n")
    print(student_summary(student))

# add_student(students)

# display_student_summary()

def update_student():
    std_id = input("Enter student Id to Update\n").strip()
    try:
        student_id = int(std_id)
    except ValueError:
        print("Invalid student ID")
        return 

    student = next(
        (std for std in students if std['id'] == student_id),
        None)

    if not student:
        print("ID not found")
        return

    print("Student found:", student)
    result = student_validation()
    if isinstance(result, str):
            print(result)
            print("Student NOT Updated")
            return
    
    student_name, email, marks = result

    student['name'] = student_name
    student['email'] = email
    student['marks'] = marks
    with open('students.json', 'w') as f:
        json.dump(students, f, indent=4)
    print("=== Student Updated Successfully===\n")
    print(student_summary(student))

#add_student(students)
#update_student(students)

def delete_student():
    std_id = input("Enter student Id to Delete\n").strip()

    try:
        student_id = int(std_id)
    except ValueError:
        print("Invalid student ID")
        return

    student = next(
        (std for std in students if std['id'] == student_id),
        None
    )

    if not student:
        print("ID not found")
        return

    print("Student found:", student)

    confirm = input("Are you sure you want to delete? (y/n): ").strip().lower()

    if confirm != "y":
        print("Delete cancelled")
        return

    students.remove(student)

    with open('students.json', 'w') as f:
        json.dump(students, f, indent=4)

    print("=== Student Deleted Successfully ===\n")

#add_student()
#delete_student()
#display_student_summary()



