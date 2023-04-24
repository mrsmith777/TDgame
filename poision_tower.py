from time import sleep
import random
from tower_class import Tower as pt
# Even though import runs the whole code of a file, importing the fileNAME will import a MODULE butname
# importing FROM filename using the CLASS NAME will import AS CLASS and not module.

class Poision_tower(pt):
    def __init__(self):
        super().__init__("Poision tower", 20, 1750, 520, 10/5, False, True, False)

    
    def Poision_attack(self):
        i = 0
        b = i

        a = random.randint(1,20)
        if (a <= self.crit_chance):
            self.Damage = self.damage * 2
        sleepdata = 1000 / self.attackspeed
        sleep(sleepdata)
        format_float = "{:.2f}".format(sleepdata)
        print("The Poision tower attacked for", self.damage, "damage after", format_float, "seconds with a range of", self.range )
        b = b + 1
        if (b >= 3):
            b=3
        dot_dmg = self.damage*b/3
        format_dot = "{:.2f}".format(dot_dmg)
        print("The Poision tower also applied a dot for", format_dot, "damage / sec" )

poision_tower = Poision_tower()
poision_tower.Poision_attack()

