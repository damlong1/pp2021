option = True

students=[]
numstudent = int(input("Enter number of students in a class: "))
for num in range(0,numstudent):
    stuid=input("Enter ID of students: \n")
    students.append(stuid)
    stuname=input("Enter name of students: \n")
    students.append(stuname)
    stubos=input("Enter date of birth of students:\n ")
    students.append(stubos)

courses=[]
numcour = int(input("Enter number of courses: "))
for num in range(0,numcour):
    courid=int(input("Enter id of course:"'\n'))
    courses.append(courid)
    courname=input("Enter name of course:\n")
    courses.append(courname)

marks=[]
while option:
 print('List of courses:')
 for num1 in range(1, numcour+2, 2):
    print(courses[num1])
 courmark=input("Enter the course to put marks for: ")
 marks.append(courmark)

 print('List of students:')
 for num in range(1, numstudent+5, 3):
     print(students[num])
 stumark=input("Enter the student to put marks for: ")
 marks.append(stumark)

 mark=input("Enter the mark: ")
 marks.append(mark)

 option=input("Continue input or print?\n 1.Continue input \n 2.print marks \n ")
 if option == '1':
    option = True
 else :
     option = False

     for x in marks:
      print(''.join(str(x)))






