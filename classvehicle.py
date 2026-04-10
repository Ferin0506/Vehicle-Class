#Create a class 
class Vehicle:

    #Create init method
    def __init__(self, max_speed, mileage):
        
        #Bind arguments
        self.max_speed = max_speed
        self.mileage = mileage

#Object creation
modelX= Vehicle(180, 20)

#Access the variables inside init method
print("Model Max Speed:", modelX.max_speed)
print("Modle Mileage:", modelX.mileage)