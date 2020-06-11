#getting external files (CSV) into a dictionary


import csv

contacts=[]
        
class contact():
    def __init__(self, name, tel, address):
        self.name=name
        self.tel=tel
        self.address=address
    def tel(self,name):
        return self.tel


def get_contacts():
        
        with open("contacts2.csv") as file:
            data = csv.reader(file, delimiter=',')
            for person in data:
                contacts.append(contact(person[0],person[1],person[2]))
                
get_contacts()
for contact in contacts:
    print(f"{contact.name}, tel: {contact.tel}, Address: {contact.address}")

    
    
