class Manager:
    def __init__(self, departmment:str, team_size:int):
        self.__departmment = departmment
        self.__team_size = team_size
    
    def manage_team(self):
        pass
    def set_team_size(self):
        pass

class Employee(Manager):
    def __init__(self, departmment, team_size, name:str, employee_id:int, salary:float):
        super().__init__(departmment, team_size)
        self.__name = name
        self.__employee_id = employee_id
        self.__salary = salary

    def get_details(self):
        pass

    def calculate_bouns(self):
        pass

e1 = Employee()
e2 = Employee()