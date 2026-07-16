class Taxi: 
 def __init__(self,model:str, capacity:str, variant:str):
    self.__model = model
    self.__capacity = capacity
    self.__variant = variant
     

 def getModel(self):
        return self.__model
    
 def getCapacity(self):
        return self.__capacity
    
 def setCapacity(self, capacity):
        self.__capacity = capacity

 def getVariant(self):
        return self.__variant
    
 def setVariant(self, variant):
        self.variant = variant

class Vehicle(Taxi):
 def __init__(self, model, capacity, variant, color:str):
      super().__init__(model, capacity, variant)
      self.__color = color

 def vehicleInfo(self):
      return self.getModel() + " " + self.getVariant() + " in " + self.__color + " with " + self.getCapacity() + " seats"
   

v1 = Vehicle("i20 Active", "4", "SX", "Bronze")
print(v1.vehicleInfo())
print(v1.getModel())