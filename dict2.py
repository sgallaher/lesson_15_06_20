#dictionaries in Python

people = {
    "Hermione": "555-555-111",
    "Ron": "555-555-222",
    "Harry": "555-555-333"
    }

#get input
person = input("Enter name: ").capitalize()
if person in people:
    print(f"{person}'s phone number is {people[person]}")
    
