import student_core
def teacher (code):
    if code == '1234' or code == '4321':
        return input('Would you like to check by Name, Date, or All: ')

def name():
    return input('Who would you like to check up on?: ')

def date():
    return input('What date would you like to see? Please do year-month-day in numeric number ex: 2015-08-24: ')

def wich_instructor():
    return input('Which instructor are you Sean or Nate?: ')

def password(name):
    return input('Welcom '+ name + '! Please type in your password.: ')

def main():
    while True:
        name = wich_instructor()
        code = password(name)
        msg = teacher(code).lower()
        if msg == 'name':
            student = name()
            person = student_core.check_up_name(student)
            print(person)
            break  
        elif msg == 'date':
            fecha = date()
            calendario = student_core.check_up_date(fecha)
            print(calendario)
            break
        elif msg == 'all': 
            print('Here is the whole list \n')   
            todos = student_core.check_up_all()
            print(todos)
            break
        else:
            print('Sorry, invalid choice.')
if __name__ == '__main__':
    main()