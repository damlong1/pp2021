import weakref
option = True

class Student:
  students =[]
  def __init__(self, studentid, studentname, DoB):
    self.studentid = studentid
    self.studentname = studentname
    self.DoB = DoB
    self.__class__.students.append(self)
  def showinfo(self):
    for i in self.students:
     print(i.studentid, i.studentname, i.DoB)

class Course:
  courses =[]
  def __init__(self, courseid, coursename):
    self.courseid = courseid
    self.coursename = coursename
    self.__class__.courses.append(self)
  def showcourse(self):
    for i in self.courses:
     print(i.courseid, i.coursename)

class Mark:
  marks =[]
  def __init__(self, mark):
      self.mark = mark
      self.__class__.marks.append(self)
  def showmarks(self):
      for i in self.marks:
          print(i.mark)

while option:
   option = input("1.Input Students\n2.Input Courses\n3.Input marks\n"
                  "4.Show list of students\n5.Show list of courses\n6.Show Marks\n7.End\n")
   if option == '1':
      option = True
      numofstu = int(input('Number of students: '))
      for num in range(0, numofstu):
       student = Student(
        input('Student id: '),
        input('Student name: '),
        input('Student DoB: ')
       )
   elif option == '2':
       option = True
       numofcourse = int(input('Number of courses: '))
       for num in range(0, numofcourse):
        course = Course(
           input('Course id: '),
           input('Coursename: '),
        )
   elif option == '3':
        option = True
        print('List of courses:')
        print(course.showcourse())
        print('List of students:')
        print(student.showinfo())
        mark = Mark(
            input('Input mark( by form CourseName: Name: Mark ): ')
        )
   elif option == '4':
       option = True
       print('List of students:')
       print("ID | Name| DoB\n")
       print(student.showinfo())
   elif option == '5':
       option = True
       print('List of courses:')
       print("CourseID| Name\n")
       print(course.showcourse())
   elif option == '6':
     option = True
     print('List of marks:')
     print("Course| Name| Mark\n")
     print(mark.showmarks())
   else:
       break

