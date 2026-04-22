class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy
    
# Don't modify the above code
    def feed(self):
        self.hunger -= 1
        print(f"{self.name} has been fed.")
        print(f"{self.name}'s hunger level: {self.hunger}")

# TODO: Create a pet named "Whiskers" that is a species of 'cat' with hunger level 6 and energy level 8
whiskers = Pet("Fluffy", "cat", 6,8)

whiskers.feed()
whiskers.feed()
whiskers.feed()


# Don't modify the following code
print(f"{whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}") 
