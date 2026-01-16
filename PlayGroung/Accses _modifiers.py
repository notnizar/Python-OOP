class acc:
    def __init__(self, name:str, age:int, mindset: str) -> None:
        self.name = name # its a public attribute  cause it have  not _ or  __
        self._age = age # its protected only childes  can accses
        self.__mindset = mindset #  now its private and  should have a setter and getter



