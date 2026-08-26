print("Student Management System\n")
students = [
    {"id":1,"name":"Chandra","email":"chandra@example.com","marks":[99,80,85]},
    {"id":2,"name":"Mouli","email":"mouli@example.com","marks":[29,40,85]},
    {"id":3,"name":"Arjun","email":"arjun@example.com","marks":[39,80,95]}
]
def calculate_average(marks):
    if marks is None or len(marks) == 0:
        return 'Lists contains atleast 1 element'
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

def add_student(students):

    student_name = input("Enter student Name \n")
    if not student_name:
            return 'Student name is  required'
    email = input("Enter student Email \n")
    if not email:
            return 'Email is required'
    marks = input("Enter marks separated by comma , \n")
    ll = []
    if not marks:
        return 'Atleast 1 subject marks are required'
    for i in marks.split(','):
            if not i.strip():
               print("Mark cannot be empty")
               print("Student NOT added")
               return
            try:
               a = int(i.strip())
            except ValueError:
               print(f"Invalid mark: {i}")
               print("Student NOT added")
               return
            if 0 <= a <= 100:
               ll.append(a)
            else:
              print("Mark must be between 0 and 100")
              print("Student NOT added")
              return

    
    if students:
        next_id = max(std['id'] for std in students) + 1
    else:
        next_id = 1
    l_object = {'id' : next_id,'name':student_name,'email':email,'marks':ll}
    students.append(l_object)
    print("=== Student Added === \n")
    res = student_summary(l_object)
    print(res)

add_student(students)






