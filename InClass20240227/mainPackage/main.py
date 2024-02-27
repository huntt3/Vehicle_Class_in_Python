#main.py
from vehiclePackage.vehicleClass import *
if __name__ == "__main__":
    #Instantiate an object of type Vehicle
    myCorvette = Vehicle("Car", 120)
    myCorvette.printType()
    #print(myCorvette.getMaxSpeed())
    
    maxSpeed = myCorvette.getMaxSpeed()
    print("Maximum Speed:",maxSpeed)
    
    #Instantiate another Vehicle object
    myBoeing787 = Vehicle("Plane")
    myBoeing787.printType()                 #Object of type vehicle
    
    #I want a list of 3 vehicles: Car, Boat, Spaceship
    
    myBoat = Vehicle("Boat")
    mySpaceship = Vehicle("Spaceship")
    
    myVehicles = [myCorvette, myBoat, mySpaceship]
    print("The vehicles are:")
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getMaxSpeed())