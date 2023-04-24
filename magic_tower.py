from time import sleep
import random
from tower_class import Tower as mt
# Even though import runs the whole code of a file, importing the fileNAME will import a MODULE butname
# importing FROM filename using the CLASS NAME will import AS CLASS and not module.

class Magic_tower(mt):
    def __init__(self):
        super().__init__("Magic tower", 82, 650, 600, 5/5, True, False, False)

    def Magictower_attack(self):
        a = random.randint(1,20)
        if (a <= self.crit_chance):
            self.damage *= 2
        sleepdata = 1000/self.attackspeed
        sleep(sleepdata)
        format_float = "{:.2f}".format(sleepdata)
        print("The Magic tower attacked for", self.damage, "damage and slowed the target for 30% after", format_float, "seconds with a range of", self.range )

magic_tower = Magic_tower()
magic_tower.Magictower_attack()

