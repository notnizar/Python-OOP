class Employee:
    def __init__(self,  name:str, employee_id:int, salary:float):
        self.__name = name
        self.__employee_id = employee_id
        self.__salary = salary

    
    def get_details(self):
        pass

    def calculate_bouns(self):
        pass

    
class Manager(Employee):
    def __init__(self, departmment, team_size):
        super().__init__(departmment, team_size)
        self.__departmment = departmment
        self.__team_size = team_size


    def manage_team(self):
        print(f"Manager is leading {self.__team_size} people")

    def set_team_size(self):
        pass

e1 = Employee()
e2 = Employee()