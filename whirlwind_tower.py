from time import sleep
import random
from tower_class import Tower as wwt
# Even though import runs the whole code of a file, importing the fileNAME will import a MODULE butname
# importing FROM filename using the CLASS NAME will import AS CLASS and not module.

class Whirlwind_tower(wwt):
    def __init__(self):
        super().__init__("Whirlwind tower", 42, 1100, 100, 15/5, False, False, True)

    def Whirlwind_attack(self):
        
        a = random.randint(1,20)
        if (a <= self.crit_chance):
            self.damage *= 2
        sleepdata = 1000/self.attackspeed
        sleep(sleepdata)
        format_float = "{:.2f}".format(sleepdata)
        print("The Whirlwind tower attacked for", self.damage, "damage after", format_float, "seconds with a range of", self.range )

whirlwind_tower = Whirlwind_tower()
whirlwind_tower.Whirlwind_attack()

