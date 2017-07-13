import student_core
import disk
import datetime
def intro():
    msg = input('Welcome to BASE CAMP CODING ACADEMY!\n Please type in your first and last name.: ')
    return msg

def main():
    msg = intro()
    if msg:
        disk.Check_in(msg)
    else:
        print('Sorry invalid answer')



if __name__ == '__main__':
    main()