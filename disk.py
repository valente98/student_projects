import datetime
def Check_in(name):
    """(str) --> str"""
    current = datetime.datetime.now()
    message = '\n{}, {}'.format(name, current)
    with open('checkins.txt', 'a') as file:
        file.write(message)

def instructor():
    name = []
    with open('checkins.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        name.append([split_string[0], split_string[1]])
    return name

def roster():
    names = []
    with open('roster.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        names.append([split_string[0]])
    return names
        