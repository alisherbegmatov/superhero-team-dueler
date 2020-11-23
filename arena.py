from superheroes import *
import os

class Arena:
    def __init__(self):
        self.team_one = Team("Marvel Team")
        self.team_two = Team("DC Team")
    
    def create_ability(self):
        name = input("What is the ability name?\n")
        max_damage = int(input("What is the max damage of the ability?\n"))

        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the weapon name?\n")
        max_damage = int(input("What is the max damage of the weapon?\n"))

        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What is the armor name?\n")
        max_armor = int(input("What is the max defense of the armor?\n"))

        return Armor(name, max_armor)

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add Ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")

            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)
        
        return hero
    
    def build_team_one(self):
        num_of_heroes = int(input("How many heroes would you like on Team One?\n"))
        for _ in range(num_of_heroes):
            hero = self.create_hero()
            self.team_one.add_hero(hero)   
    
    def build_team_two(self):
        num_of_heroes = int(input("How many heroes would you like on Team Two?\n"))
        for _ in range(num_of_heroes):
            hero = self.create_hero()
            self.team_two.add_hero(hero)   
    
    def team_battle(self):
        self.team_one.attack(self.team_two)
    
    def team_stats(self, team):
        print("\n")
        print(team.name + " Statistics:")
        team.stats()

        team_kills = 0
        team_deaths = 1
        for hero in team.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        
        print(f"Average K/D: {team_kills / team_deaths}")

        hero_names = ""
        for hero in team.heroes:
            if hero.deaths == 1:
                hero_names += hero.name + "\n"

        if hero_names == "":
            print("No heroes survived :/")
        else:
            print("The following heroes survived:")
            print(hero_names)

    def show_stats(self):
        self.team_stats(self.team_one)
        self.team_stats(self.team_two)
        print("\n")

if __name__ == "__main__":
    game_is_running = True
    arena = Arena()

    os.system('cls' if os.name == 'nt' else 'clear')
    arena.build_team_one()
    arena.build_team_two()
    
    while game_is_running:
        arena.team_battle()
        arena.show_stats()

        play_again = input("Play again?\n[Y] Yes\n[N] No\n")

        if play_again.lower() == "n":
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
