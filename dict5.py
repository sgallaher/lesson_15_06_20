#getting external files (CSV) into a dictionary


import csv



def contacts():
    try:
        
        with open("contacts2.csv") as file:
            data = csv.reader(file, delimiter=',')
            people=dict(data)
        print(people)
        return people
    except:
        print("This won't work, as contact2.csv isn't using pairs")
        return None


#open contacts
people = contacts()
#get input
person = input("Enter name: ").capitalize()
if person in people:
    print(f"{person}'s phone number is {people[person]}")
else:
    print(f"You don't seem to have {person}'s phone number")
    
    
