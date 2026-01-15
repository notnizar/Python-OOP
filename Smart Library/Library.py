from datetime import datetime, timedelta
import Media

class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.inventory = []

    def add_items(self, item):
        if isinstance(item, Media): ## here i am casting the object
            self.inventory.append(item)
        else:
            print("Only media obkects can be  added")

    def find_item_by_id(self, media_id):
        for item in self.inventory:
            if item.media_id == media_id:
                return item
        return None
    def borrow_item(self, media_id):
        item = self.find_item_by_id(media_id)
        if item:
            if not item.is_borrowed:
                item.is_borrowed = True
                item.due_date = datetime.now() + timedelta(days=14)
                print(f"Success '{item.title}' Due date: {item.due_date.strftime('%Y-%m-%d')}")
            else:
                print(f"Fail: '{item.title}' is already checked out")
        else:
            print("not found")

    def return_item(self, media_id):
        item = self.find_item_by_id(media_id)
        if item and item.is_borrowed:
            if datetime.now() > item.due_date:
                days_late = (datetime.now() - item.due_date).days
                fine = item.calculate_fine(days_late)
                print(f"Fine: {fine:.2f} JOD")
            
            item.is_borrowed = False
            item.due_date = None
            print(f"Success: '{item.title}' has been returned")
        else:
            print("Item was not borrowed")

    def show_inventory(self):
        print(f"\n--- {self.name} Inventory ---")
        for item in self.inventory:
            print(item)