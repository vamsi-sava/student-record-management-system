from database import connect_db

def add_student():

    conn = connect_db()
    cursor = conn.cursor()

    Student_ID = int(input('enter the student id:'))
    Name = input('enter the student name:')
    Department = input('enter the Department:')
    Year = int(input('enter the year:'))
    Semester = int(input('enter the semester:'))
    Subject1 = int(input('enter the subject1:'))
    Subject2 = int(input('enter the subject2:'))
    Subject3 = int(input('enter the subject3:'))
    Subject4 = int(input('enter the subject4:'))
    Subject5 = int(input('enter the subject5:'))

    Total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5

    Perecentage = Total // 5

    if Perecentage >= 90:
        Grade = 'A+'
    elif Perecentage >= 80:
        Grade = 'A'
    elif Perecentage >= 70:
        Grade = 'B'
    elif Perecentage >= 60:
        Grade = 'C'
    elif Perecentage >= 50:
        Grade = 'D'
    else:
        Grade = 'F'

    query = """
    INSERT INTO students
    (Student_ID, Name, Department, Year,
    Semester,
     Subject1,Subject2,Subject3,
    Subject4,Subject5,
     Total, Perecentage, Grade)
    VALUES
    (%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,
    %s,%s,%s)
    """
    values = (
        Student_ID,
        Name,
        Department,
        Year,
        Semester,
        Subject1,
        Subject2,
        Subject3,
        Subject4,
        Subject5,
        Total,
        Perecentage,
        Grade
    )

    cursor.execute(query,values)
    conn.commit()

    print('Student added successfully')
    print('total=',Total)
    print('percentage=',Perecentage)
    print('Grade=',Grade)

    cursor.close()
    conn.close()
def view_students():
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM students"

    cursor.execute(query)
    students = cursor.fetchall()

    if len(students) == 0:
        print('No student records found')
    else:
        for student in students:
            print('------- Students Records --------')
            print(f'Student_ID : {student[0]}')
            print(f'Name : {student[1]}')
            print(f'Department : {student[2]}')
            print(f'Year : {student[3]}')
            print(f'Semester : {student[4]}')
            print(f'Subject1 : {student[5]}')
            print(f'Subject2 : {student[6]}')
            print(f'Subject3 : {student[7]}')
            print(f'Subject4 : {student[8]}')
            print(f'Subject5 : {student[9]}')
            print(f'Total : {student[10]}')
            print(f'Perecentage : {student[11]}')
            print(f'Grade : {student[12]}')
    print('---------------------------------------------')

    cursor.close()
    conn.close()

def search_student():
    conn = connect_db()
    cursor = conn.cursor()

    Student_ID = int(input('enter the student id:'))

    query = """
    SELECT * FROM students
    WHERE Student_ID = %s
    """

    cursor.execute(query,(Student_ID,))

    student = cursor.fetchone()

    if student:
        print("Student Found")
        print("--------------------------")
        print(f"Student ID : {student[0]}")
        print(f"Name       : {student[1]}")
        print(f"Department : {student[2]}")
        print(f"Year       : {student[3]}")
        print(f"Semester   : {student[4]}")
        print(f"Total      : {student[10]}")
        print(f"Percentage : {student[11]}")
        print(f"Grade      : {student[12]}")
    else:
        print('Student not found')
    
    cursor.close()
    conn.close()

def update_student():
    conn = connect_db()
    cursor = conn.cursor()

    Student_ID = int(input('enter the student id:'))

    query = "SELECT * FROM students WHERE Student_ID = %s"

    cursor.execute(query,(Student_ID,))

    student = cursor.fetchone()

    if  student:
        print('Enter New Student Details')
        Name = input('enter the student name:')
        Department = input('enter the Department:')
        Year = int(input('enter the year:'))
        Semester = int(input('enter the semester:'))
        Subject1 = int(input('enter the subject1:'))
        Subject2 = int(input('enter the subject2:'))
        Subject3 = int(input('enter the subject3:'))
        Subject4 = int(input('enter the subject4:'))
        Subject5 = int(input('enter the subject5:'))

        Total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5

        Perecentage = Total // 5

        if Perecentage >= 90:
            Grade = 'A+'
        elif Perecentage >= 80:
            Grade = 'A'
        elif Perecentage >= 70:
            Grade = 'B'
        elif Perecentage >= 60:
            Grade = 'C'
        elif Perecentage >= 50:
            Grade = 'D'
        else:
            Grade = 'F'
        update_query = """
        UPDATE students
        SET
        Name = %s,
        Department = %s,
        Year = %s,
        Semester = %s,
        Subject1 = %s,
        Subject2 = %s,
        Subject3 = %s,
        Subject4 = %s,
        Subject5 = %s,
        Total = %s,
        Perecentage = %s,
        Grade = %s
        WHERE Student_ID = %s
        """
        values = (
            Name,
            Department,
            Year,
            Semester,
            Subject1,
            Subject2,
            Subject3,
            Subject4,
            Subject5,
            Total,
            Perecentage,
            Grade,
            Student_ID
        )

        cursor.execute(update_query, values)

        conn.commit()
        
        print('Student updated successfully')
    else:
        print('Student not found')
    cursor.close()
    conn.close()
def delete_student():
    conn = connect_db()
    cursor = conn.cursor()

    Student_ID = int(input('enter the student id:'))

    query = 'SELECT * FROM students WHERE Student_ID = %s'

    cursor.execute(query,(Student_ID,))

    student = cursor.fetchone()

    if student:
        
        Choice = input('Are you sure do you want to delete student really? (Y/N):')

        if Choice.upper() == 'Y':
            delete_query = 'DELETE FROM students WHERE Student_ID = %s'
            cursor.execute(delete_query,(Student_ID,))
            conn.commit()
            print('Deleted successfully')
        else:
            print('Deletion canacelled')
    else:
        print('Student not found')

    cursor.close()
    conn.close()






