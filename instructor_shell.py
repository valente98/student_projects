import student_core
def teacher():
    msg = input('Would you like to check by Name, Date, or All: ')
    return msg

def name():
    msg = input('Who would you like to check up on?: ')
    return msg

def date():
    msg = input('What date would you like to see? Please do year-month-day in numeric number: ')
    return msg

def main():
    while True:
        msg = teacher()
        if msg.lower() == 'name':
            name = name()
            student_core.check_up_name(name)
            break  
        elif msg.lower() == 'date':
            date = date()
            student_core.check_up_date(date)
            break
        elif msg.lower() == 'all':    
            student_core.check_up_all()
            break
        else:
            print('Sorry, invalid choice.')
if __name__ == '__main__':
    main()