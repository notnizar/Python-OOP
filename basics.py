class Student:
    def __init__(self,  name, major, gpa) -> None:
        self.name = name
        self.__major = major
        self.__gpa = gpa  #Encapsolation

    @property
    def major(self):
       return self.__major.upper()
    
    @major.setter
    def major(self, value):
       if value != "":
          self.__major = value
       else: 
          print("Inviled  Input")
        

    def set_gpa(self, value): ## self mean  the var in the class
       ## To set the gpa data with validation
       if 0 <= value <= 4:
          self.__gpa = value
          print("GPA Added")
       else:
          print("Enter A number between  0 and 4")

    def get_gpa(self):
       return self.__gpa

    def greeting (self):
     print(f"Welcome my name is {self.name} and my major is {self.major}")


std1 = Student("Nizar", "Ai and Data", 3.5)
std1.greeting()