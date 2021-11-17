##this code is the definition and first instance of a class
class Game:
    variable1 = 'Hello'
    variable2 = 'World'


## parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)
        return msg

##child class instance
class Human(Organism):
    name = "Macguyver"
    species = "Homosapiens"
    legs = 2
    arms = 2
    origin = "Earth"

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum and a roll of duct tape"
        return msg

## another child class instance
class Dog(Organism):
    name = "Spot"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"
        
    def bite(self):
        msg = "\nEmits a loud, menancing growl and bites down ferociously on its target!"
        return msg

## even another child class instance
class Bacterium(Organism):
    name = "X"
    species = "Bacteria"
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = "Mars"

    def replication(self):
        msg = "\nThe cells begin to divide and split into two seperate organisms!"
        return msg

##this section of the code deals with polymorphism
##parent class
class Plane:
    Manufacturer = "Unknown"
    Airline = "unknown"
    Seats = 0
    Engines = 1

    def flightTime(self):
        msg = "\nThis plane can carry " + Plane.seats + " passengers at " +(100 * Plane.engines()) + " mph."
        return msg

##this code demonstrates polymorphism of a child class
class JetFighter(Plane):
    Manufacturer = "LockHeed Martin"
    Airline = "U.S. Military"
    seats = 1
    engines = 2
    afterburners = 1

    def flightTime(self):
        msg = "\n This plane can carry " + str(JetFighter.seats) + " passengers at " + str((100 * JetFighter.engines) + (1000 * JetFighter.afterburners)) + " mph."
        return msg

##this code demonstrates polymorphism of another child class
class JumboJet(Plane):
    Manufacturer = "Boeing"
    Airline = "Delta"
    seats = 100
    engines = 5
    cargo = 750

    def flightTime(self):
        msg = "\n This plane can carry " + str(JumboJet.seats) + " passengers at " + str((100 * JumboJet.engines) - (JumboJet.cargo)) + " mph."
        return msg

    
if __name__== "__main__":
    ##this code demonstrates our most basic class
    x = Game()
    print("{} {}".format(x.variable1, x.variable2))

    ##this code demonstrates the parent and child class of Organism and Human respectively
    human = Human()
    print(human.information())
    print(human.ingenuity())

    ##this code demonstrates the parent and child class of Organism and Dog
    dog = Dog()
    print(dog.information())
    print(dog.bite())

    ##this code demonstrates the parent and child class of Organism and Bacteria
    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())
    
    ##This code demonstrates polymorphism
    F16 = JetFighter()
    print(F16.flightTime())

    AirBus = JumboJet()
    print(AirBus.flightTime())
