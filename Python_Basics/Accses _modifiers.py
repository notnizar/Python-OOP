class House:
    def __init__(self, location:str, price:int, discount: int) -> None:
        self.location = location # its a public attribute  cause it have  not _ or  __
        self._price = price # its protected only childes  can accses
        self.__discount = discount #  now its private and  should have a setter and getter
    
    @property # property is useful cause it make us validate the data in vars and treat them as attributes
    def discount(self):
        return self.__discount
    
    @discount.setter
    def discount(self, amount):
        if amount < 0: 
         raise ValueError("It should be +")
        self.__discount = amount

    @discount.deleter #this delete the var data its useful  for memory management and security
    def discount(self):
       self.__discount = None

