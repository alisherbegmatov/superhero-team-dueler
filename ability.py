from random import randint

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        random_value = randint(0, self.max_damage)
        return random_value

if __name__ == "__main__":
    print(Ability("Debbugging Ability", 20).attack())
