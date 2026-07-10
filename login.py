
def login():

    USERNAME = 'Admin@1431'

    PASSWORD = 'Vamsi@1431'

    while True:
        print('----------WELCOME TO STUDENT MANAGEMENT RECORD SYSTEM-----------')

        user_name = input('Enter the username:')
        password = input('enter the password')

        if user_name == USERNAME and password == PASSWORD:
            print('Login Successfully')
            return True
        else:
            print('INVALID username or password')
            print('Please try again')
    
