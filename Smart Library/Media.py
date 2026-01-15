from abc import ABC, abstractmethod
from datetime  import datetime, timedelta

class Media(ABC): ## ABC means that is abstracted class
    def __init__(self,title: str,meadi_id:int) -> None:
        self.title = title
        self.meadi_id = meadi_id
        self.is_borrowed = False # the (_) in the var mean is private
        self.due_date = None

    @abstractmethod
    def calculate_fine(self, days_overdue):
        pass

    def __str__(self) -> str:
        status = "Brorowed" if self.is_borrowed else "Avilabil"
        return f"[{self.meadi_id}] {self.title} - {status}"
    
## subClasses
class Book(Media):
    def __init__(self, title: str, meadi_id: int, author: str, pages: int) -> None:
        super().__init__(title, meadi_id)
        self.author = author
        self.pages = pages

    def calculate_fine(self, days_overdue):
        return days_overdue * 0.50
    

class DVD(Media):
    def __init__(self, title: str, meadi_id: int, director : str, duration:int) -> None:
        super().__init__(title, meadi_id)
        self.director = director
        self.duration = duration

    def calculate_fine(self, days_overdue):
        return days_overdue * 1.50




