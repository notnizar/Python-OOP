class Student:
  def __init__(self, name):
   self.name = name
   self.__age = None # private member

  @property
  def age(self):
   return self._age
  
  @age.setter
  def age(self, value):
  # VALIDATION: Checking if it makes sense
   if value < 0:
    print("❌ Age can't be negative!")
   elif value > 150:
    print("❌ Age can't be over 150!")
   else:
    self._age = value


stud = Student('Dania')
stud.age = 21
print(stud.name)
print(stud.age)
