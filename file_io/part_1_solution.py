import re

def add_student(first_name):
    with open('students.txt', 'a') as file:
        file.write(first_name)

def find_student(first_name):
    with open('students.txt', 'r') as file:
        for f in file:
            if f == first_name:
                print("{} was found!".format(first_name))

def update_student(first_name,new_name):
    with open('students.txt', 'r+') as file:
        text = file.read()
        text=  re.sub(first_name, new_name, text)
        file.seek(0)
        file.write(text)
        file.truncate()

def remove_student(first_name):
    with open('students.txt', 'r+') as file:
        text = file.read()
        text=  re.sub(first_name, '', text)
        file.seek(0)
        file.write(text)
        file.truncate()
