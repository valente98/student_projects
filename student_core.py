import datetime
import disk
def check_up_name(name):
    list_name = disk.instructor()
    check = ''
    for item in list_name:
        if name == item[0]:
            check += ('\n'+str(item))
    print(check)

def check_up_date(date):
    list_date = disk.instructor()
    check = ''
    for item in list_date:
        if item[1].startswith(date):
            check += ('\n'+str(item))
    print(check)

def check_up_all():
    print('Here is the whole list \n')
    for_all = disk.instructor()
    for item in for_all:
        print('\n'+str(item))
