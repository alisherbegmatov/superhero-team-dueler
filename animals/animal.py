class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def drink(self):
        print(f"{self.name} is drinking.")

class Frog(Animal):
    def jump(self):
        print(f"{self.name} is jumping.")

if __name__ == "__main__":
    random_animal = Animal("Frog")
    random_animal.eat()
    random_animal.drink()

    frog = Frog("🐸")
    frog.drink()
    frog.jump()
