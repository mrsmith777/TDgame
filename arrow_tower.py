from time import sleep
import random
from tower_class import Tower as at
# Even though import runs the whole code of a file, importing the fileNAME will import a MODULE butname
# importing FROM filename using the CLASS NAME will import AS CLASS and not module.

class Arrow_tower(at):
    def __init__(self):
        super().__init__("Arrow tower", 42, 850, 850, 30/5, False, False, True)

    def Arrow_attack(self):
        
        a = random.randint(1,20)
        if (a <= self.crit_chance):
            self.damage *= 2
        sleepdata = 1000/self.attackspeed
        sleep(sleepdata)
        format_float = "{:.2f}".format(sleepdata)
        print("The Arrow tower attacked for", self.damage, "damage after", format_float, "seconds with a range of", self.range )

arrow_tower_instance = Arrow_tower()
arrow_tower_instance.Arrow_attack()

