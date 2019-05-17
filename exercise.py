class System:

    def __init__(self, bodies = []):
        self.bodies = bodies
    
    def add(self, celestial_body):
     
        if celestial_body.name in [body.name for body in self.bodies]: 
            print("Aleady exist")
        else:
            self.bodies.append(celestial_body)
    
    def total_mass(self):
        total_mass = 0
        for body in self.bodies:
            total_mass += body.mass
        return total_mass

class Body(System):

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
    
class Planet(Body):

    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day
        self.year = year

class Star(Body):

    def __init__(self, name, mass, type):
        super().__init__(name, mass)
        self.type = type

class Moon(Body):

    def __init__(self, name, mass, month, planet):
        super().__init__(name, mass)
        self.month = month
        self.planet = planet



earth = Planet("Earth", 130, 899, 365)
sun = Star("Sun", 240, "G-star")
northern_star = Moon("Northern_star", 568, 294, "moon")
System().add(earth)
System().add(sun)
System().add(northern_star)
System().add(earth)

print(System().bodies)
print(System().total_mass())