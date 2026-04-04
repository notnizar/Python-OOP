from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self,name: str, user_id:int) -> None:
        self.name = name
        self.user_id = user_id
        self.borrowed_items = []

    @abstractmethod
    def get_limit(self):
        """Limit the user how much book can take based on role"""
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.name} (ID: {self.user_id})"
    
class Student(User):
    def get_limit(self):
        return 5
    
class Prof(User):
    def get_limit(self):
        return 10