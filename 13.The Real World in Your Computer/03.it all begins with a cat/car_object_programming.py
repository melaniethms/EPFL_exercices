from unicodedata import name


class Car :
    def __init__(self, name, color, speed) :
        self.name = name
        self.color = color
        self.speed = speed


    def drive(self) :
        print("the " + self.color + " " + self.name + " is driving at " + self.speed)
    def fuel(self, fuel) :
        print ("the " + self.name + " only consume " + fuel)
    def seats(self, seats) :
        print("their is " + str(seats) + " in a " + self.name)
    

Kia = Car("Kia", "red", "88 km/h")
Kia.drive()
Kia.fuel("sans plomb 99")
Kia.seats(4)

Porsche = Car("Porsche", "black", "200 km/h")
Porsche.drive()
Porsche.fuel ("blood of innocent people")
Porsche.seats(2)