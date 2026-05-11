class Person():
    def __init__(self, f_name:str, l_name:str):
        self.f_name = f_name
        self.l_name = l_name

    def __str__(self):
        return f"Member Name: " + self.f_name + " " + self.l_name
    
    def greet(self):
        print("Hello, I am a person at Al-Zaytoonah University")
    
class Student(Person):
    def __init__(self, f_name, l_name, std_id:int, gpa:float):
        super().__init__(f_name, l_name)
        self.std_id = std_id
        self.gpa = gpa

    def greet(self):
        print(f"Hello, I am a student. My GPA is {self.gpa}")

    def is_honors(self):
         if(self.gpa >= 3.5):
             return True
         else:
             return False
         
class Teacher(Person):
    def __init__(self, f_name, l_name, emp_id:int, sub:str):
        super().__init__(f_name, l_name)
        self.emp_id = emp_id
        self.sub = sub

    def greet(self):
        print(f"Hello, I am a teacher. I teach {self.sub}")

class UniversitySystem():
   def __init__(self):
       self.member_list =  []
   
   def add_members(self, person):
       self.member_list.append(person)

   def show_all(self):
       for p in self.member_list:
         p.greet()

   def filter_honors(self):
       for p in self.member_list:
           if isinstance(p, Student) and p.is_honors():
              print(p.f_name + " " + p.l_name)


system = UniversitySystem()

teacher = Teacher("Ibrahim", "Atoum", 1001, "Data Science")
student1 = Student("Saif", "Osama", 2001, 3.8)
student2 = Student("Salma", "Ali", 2002, 3.2)

system.add_members(teacher)
system.add_members(student1)
system.add_members(student2)

print(" all Members: ")
system.show_all()

print(" honors: ")
system.filter_honors()

