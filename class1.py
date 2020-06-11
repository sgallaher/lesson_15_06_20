class person:
    num=0
    def __init__(self,name):
        self.ident=person.num
        self.name=name
        person.num+=1
    def getme(self):
        print(self.name)

    def nextid():
        print(person.num)
        
people = []
people.append(person("shane"))
people.append(person("Harry"))

for p in people:
    p.getme()
    print(f"{p.ident}, {p.name}")
person.nextid()


        
