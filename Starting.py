class Student:
    def __init__(self,  name, major) -> None:
        self.name = name
        self.major = major

    def greeting (self):
     print(f"Welcome my name is {self.name} and my major is {self.major}")


std1 = Student("Nizar", "Ai and Data")
std1.greeting()