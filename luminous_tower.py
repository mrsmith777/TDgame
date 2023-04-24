from time import sleep
import random
from tower_class import Tower as lut
# Even though import runs the whole code of a file, importing the fileNAME will import a MODULE butname
# importing FROM filename using the CLASS NAME will import AS CLASS and not module.

class Luminous_tower(lut):
    def __init__(self):
        super().__init__("Luminous tower", 25, 1800, 650, 15/5, True, False, False)

    def Luminous_attack(self):
        
        a = random.randint(1,20)
        if (a <= self.crit_chance):
            self.damage *= 2
        sleepdata = 1000/self.attackspeed
        sleep(sleepdata)
        format_float = "{:.2f}".format(sleepdata)
        print("The Luminous tower attacked for", self.damage, "damage after", format_float, "seconds with a range of", self.range )

luminous_tower = Luminous_tower()
luminous_tower.Luminous_attack()

