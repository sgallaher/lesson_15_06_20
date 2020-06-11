#getting external files (CSV) into a dictionary


import csv



def contacts():
    with open("contacts.csv") as file:
        data = csv.reader(file, delimiter=',')
        people=dict(data)
    return people


#open contacts
people = contacts()
#get input
person = input("Enter name: ").capitalize()
if person in people:
    print(f"{person}'s phone number is {people[person]}")
else:
    print(f"You don't seem to have {person}'s phone number")
    
    
