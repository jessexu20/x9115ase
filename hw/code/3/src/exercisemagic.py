class Employeee:
    def __init__(self, name='', age=0):
        self.name=name
        self.age=age
    def __lt__(self,other):
        return self.age<other.age
    def __repr__(self):
        return "Name: %s. Age: %s" %(self.name,self.age)

#some tests of the class:
a=Employeee('Zhe Yu',26)
b=Employeee('Dong Yang',27)
print repr(a)
print repr(b)
print a<b