import student_core
import datetime
def Check_in(msg):
    """(str) --> str"""
    current = datetime.datetime.now()
    message = '\n{}, {}'.format(msg, current)
    with open('checkins.txt', 'a') as file:
        file.write(message)
