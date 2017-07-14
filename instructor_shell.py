import student_core
def teacher(code):
    if code == '1234' or code == '4321':
        return input('Would you like to check by Name, Date, or All: ')
    else:
        return 'Sorry invalid code.'

def student():
    return input('Who would you like to check up on?: ')

def date():
    return input('What date would you like to see? Please do year-month-day in numeric number ex: 2015-08-24: ')

def wich_instructor():
    return input('Which instructor are you Sean or Nate?: ')

def password(name):
    if name == 'sean' or name == 'nate':
        return input('Welcome '+ name + '! Please type in your password.: ')
    else:
        return None
        
def main():
    while True:
        name = wich_instructor().lower()
        code = password(name)
        msg = teacher(code).lower()
        if msg == 'name':
            name = student()
            person = student_core.check_up_name(name)
            print(person)
            break  
        elif msg == 'date':
            schedule = date()
            calendar = student_core.check_up_date(schedule)
            print(calendar)
            break
        elif msg == 'all': 
            print('Here is the whole list \n')   
            see_all = student_core.check_up_all()
            print(see_all)
            break
        else:
            print('Sorry, invalid choice.')
if __name__ == '__main__':
    main()