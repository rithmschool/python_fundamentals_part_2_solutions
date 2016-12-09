import csv

# Part 2

def print_names():
    with open('users.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("{} {}".format(row['first_name'], row['last_name']))

def add_name():
    with open('users.csv', 'a') as file:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(file, fieldnames)
        first = input("First name please: ")
        last = input("Last name please: ")
        writer.writerow(dict(first_name=first, last_name=last))