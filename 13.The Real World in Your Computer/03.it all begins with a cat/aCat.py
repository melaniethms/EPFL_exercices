class Cat :

    def __init__(self, name, species):
        self.name = name
        self.species = species 

    def sleep(self) :
        print ( self.name + " is sleeping")
    def show(self) :
        print(self.species + " is the species of " + self.name)
    def eat(self, food) :
        print( self.name + " is eating " + food)

tom = Cat("Tom", "Tabby")
tom.weight = 2
tom.color = "Orange"
tom.sleep()
tom.show()
tom.eat("croquettes")

athena = Cat("Athena", "Siamese")
athena.weight = 1.5
athena.color = "Brown"
athena.sleep()

print("Athena is a " + athena.species + " cat.")
print("But Tom is a " + tom.species + " cat.")