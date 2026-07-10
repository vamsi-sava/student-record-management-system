from login import login

from student import add_student
from student import view_students
from student import search_student
from student import update_student
from student import delete_student

if login():
    while True:
        print('=============================================')

        print('STUDENT RESULT MANAGEMENT RECORD SYSTEM')

        print('=============================')

        print('1.Add student')

        print('2.View students')

        print('3.Search student')

        print('4.Update student')

        print('5.Delete student')

        print('6.Exit')

        try:
            Choice = int(input('enter your choice:'))

            if Choice == 1:
                add_student()
            elif Choice == 2:
                view_students()
            elif Choice == 3:
                search_student()
            elif Choice == 4:
                update_student()
            elif Choice == 5:
                delete_student()
            elif Choice == 6:
                print('Thankyou for using STUDENT RECORD MANAGEMENT SYSTEM')
                break
            else:
                print('INVALID CHOICE!')
        
        except ValueError:
            print('Please enter VALID NUMBER!')


