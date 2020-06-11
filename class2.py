#getting external files (CSV) into a dictionary


import csv
#this is global contacts list
contacts=[]

#defining a class structure for a contact       
class contact():
    def __init__(self, name, tel, address):
        self.name=name
        self.tel=tel
        self.address=address



def get_contacts():
        
        with open("contacts2.csv") as file:
            data = csv.reader(file, delimiter=',')
            for person in data:
                contacts.append(contact(person[0].capitalize(),person[1],person[2]))
                
get_contacts()

# now to search
search = True

while search:
    results=[]
    name=input("Enter person: ").capitalize()
    for contact in contacts:
        if contact.name == name:
            results.append(contact)
    if len(results)>0:
        for result in results:
            print(f"Name:{result.name}, Tel:{result.tel}, Address:{result.address}")
    else:
        print(f"{name} not found")
