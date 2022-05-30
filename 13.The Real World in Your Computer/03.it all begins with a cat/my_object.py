class Printer3D() : 

    def __init__(self, brand, name, printing_type, resolution, price):
        self.brand = brand
        self.name = name
        self.printing_type = printing_type
        self.resolution = resolution
        self.price = price

    def technology(self) : 
        print (self.name + " uses " + self.printing_type + " technology.")
    def material(self, material) :
        print (self.name +" uses " + material + " as material to print")

um3 = Printer3D("Ultimake", "Ultimaker 3", "Fused deposing modeling", "0.06 mm", "4500.-")
um3.technology()

sl1 = Printer3D("Prusa", "Prusa SL1", "SLA", "0.015mm", "5000.-")
sl1.technology()
sl1.material("ABS resin")