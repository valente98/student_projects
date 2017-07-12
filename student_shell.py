import student_core
import disk
import datetime
def main():
    current = datetime.datetime.now()
    msg = student_core.intro()
    disk.Check_in(msg)
    print('You have checked in at', current)



if __name__ == '__main__':
    main()