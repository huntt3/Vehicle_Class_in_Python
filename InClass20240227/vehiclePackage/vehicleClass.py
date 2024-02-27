#vehicleClass.py

class Vehicle:
    '''
    Vehicle Class
    This class models a vehicle on a used car lot
    Change Order: We need to add maximum speed to the model
    Change Order: Need a way to 'read' maximum speed from the model
    Change Order: Some developers need to use the constructor without having to provide the maximum speed
    '''
    # Constructor. It's called when we instantiate an object of vehicle type.
    def __init__(self, type, max_speed = None):
        '''
        Param type: The kind of vehicle
        Param max_speed: Maximum speed of the Vehicle, defaults to None
        '''
        self.type = type;
        self._privatetype = 42 #This is the weak attempt to support data hiding
        self.max_speed = max_speed
        # An instance method. It operates on an instance of the vehicle class
    
    def printType(self):
        print(self.type);
    def getMaxSpeed(self):
        return(self.max_speed)
    if __name__ == "__main__":
        # Some code to test the class would go here.
        # If there's no code, just pass
        pass