# A Sample class with init method 
class Person: 

	# init method or constructor 
	def __init__(self, name): 
		self.name = 'shameer' 

	# Sample Method 
	def say_hi(self): 
		print('Hello, my name is', self.name) 

p = Person()
print(p.name)
p.say_hi() 
