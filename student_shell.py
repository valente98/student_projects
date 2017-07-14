import disk
import datetime
def intro():
    msg = input('Welcome to BASE CAMP CODING ACADEMY!\n Please type in your first and last name.: ')
    return msg

def main():
    name = intro().lower()
    students = disk.roster()
    current = datetime.datetime.now()
    for item in students:
        if name.lower() == item[0]:
            disk.Check_in(name)
            print('Welcome to Base Camp '+ name.title() + '! Your check in time is ' + str(current))
        
if __name__ == '__main__':
    main()