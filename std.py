class Student:
    def __init__(self,name,rno,phno):
        self.name =name
        self.rno =rno
        self.phnnumber =phno
    def display(self):
        print(self.name, self.rno,self.phnnumber)
std =Student("amit",220,88888888)
std.display()