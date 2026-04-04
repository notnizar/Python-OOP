class Person:
    def __init__(self, name:str, nationalID:str):
        self.__name = name
        self.__nationalID = nationalID

    def getPersonalinfo(self):
        return (f"Name: {self.__name}, ID: {self.__nationalID}")

    def setPersonalinfo(self, name, nationalID):
        self.__name = name
        self.__nationalID = nationalID

class OrgaMember:
    def __init__(self, memberID:int, role:str):
        self.__memberID = memberID
        self.__role = role

    def getMemberRole(self):
        return f"Role: {self.__role}"
    
    def setMemberRole(self, role):
        self.__role = role

class Employee(Person, OrgaMember):
    def __init__(self, name, nationalID, memberID, role, salary:float, dep:str):
        Person().__init__(name, nationalID)
        OrgaMember().__init__(self, memberID, role)
        self.__salary = salary
        self.__dep = dep

    def calculatePay(self):
        pass

    def promote(self):
        pass

e1 = Employee()
e1 = Employee()       
        