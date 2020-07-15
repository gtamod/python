class Computer:
    def __init__(self,name,age):
        
         self.name='shameer'
         self.age=21

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1=Computer()
c1.age=21
c2=Computer()

c1.compare()
c2.compare()
if c1.compare(c2):
    print('they are same')
else:
    print('different')

print(c1.name)
print(c2.name)
