## Animal is-a object
class Animal(object):
	pass
	
## class Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name
		self.name = name
		
## class Cat is-a Animal
class Cat(Animal):

	def __init__(self,name):
		## Cat has-a name
		self.name = name
	
##class Person is-a object
class Person(object):

	def __init__(self, name):
		##Person has-a name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
##class Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		##Employee has-a name
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary
		
##class Fish is-a object
class Fish(object):
	pass

##class Salmon is-a Fish
class Salmon(Fish):
	pass
	
##class Halibut is-a Fish
class Halibut(Fish):
	pass
	
## rover is-a dog
rover = Dog("Rover")

##satan is a Cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

## Mary has a pet named satan
mary.pet = satan

## Frank is-a employee and has a salary of 120000
frank = Employee("Frank", 120000)

## frank's pet is-a rover
frank.pet = rover

## crouse is-a Salmon
crouse = Salmon()

## Harry is-a halibut
harry = Halibut()


		