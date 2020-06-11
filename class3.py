#getting external files (CSV) into a dictionary

#need to import module to handle csv files
import csv
#this is global contacts list
contacts=[]

#defining a class structure for a contact       
class contacts:
    num=0
    def  __init__(self,ident,contact):
        self.ident=ident
        self.contact=contact
        num+=1

    def nextid():
        return num
        
class contact(contacts):
    def __init__(self, name, tel, address):
        
        self.name=name
        self.tel=tel
        self.address=address



def get_contacts():
        
        with open("contacts2.csv") as file:
            data = csv.reader(file, delimiter=',')
            for person in data:
                c=contacts(0,None)
                    
                ident=contacts.nextid()
                
                   
                temp=contact(person[0],person[1],person[2])
                entry=contacts(ident,temp)
                
                
get_contacts()

# now to search
search = True

while search:
    results=[]
    name=input("Enter person: ").capitalize()
    for contact in contacts:
        if contacts.contact.name == name:
            results.append(contacts.contact)
    if len(results)>0:
        for result in results:
            print(f"Name:{result.name}, Tel:{result.tel}, Address:{result.address}")
    else:
        print(f"{name} not found")
