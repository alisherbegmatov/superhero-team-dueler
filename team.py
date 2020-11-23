from random import choice

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()
    
    def add_hero(self, hero):
        self.heroes.append(hero)
    
    def remove_hero(self, name):
        found_hero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                found_hero = True
        
        if not found_hero:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
    
    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} K/D: {kd}")
    
    def revive_heroes(self, health = 100):
        for hero in self.heroes:
            hero.health = health
    
    def attack(self, other_team):
        living_heroes = [hero for hero in self.heroes]
        living_oponents = [hero for hero in other_team.heroes]
        print(0)
        while len(living_heroes) > 0 and len(living_oponents) > 0:
            print(1)
            current_hero = choice(living_heroes)
            current_opponent = choice(living_oponents)
            print(2)
            current_hero.fight(current_opponent)
            print(3)
            if not current_hero.is_alive() and not current_opponent.is_alive():
                living_heroes.remove(current_hero)
                living_oponents.remove(current_opponent)
            elif not current_hero.is_alive():
                living_heroes.remove(current_hero)
            elif not current_opponent.is_alive():
                living_oponents.remove(current_opponent)
            else:
                living_heroes.remove(current_hero)
                living_oponents.remove(current_opponent)
