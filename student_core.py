import datetime
import disk
def check_up_name(student):
    list_name = disk.instructor()
    check = ''
    for item in list_name:
        if student.lower() == item[0]:
            check += ('\n'+str(item))
    return check

def check_up_date(fecha):
    list_date = disk.instructor()
    check = ''
    for item in list_date:
        if item[1].startswith(fecha):
            check += ('\n'+str(item))
    return check

def check_up_all():
    check = ''
    for_all = disk.instructor()
    for item in for_all:
        check += ('\n'+str(item))
    return check
