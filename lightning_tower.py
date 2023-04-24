from time import sleep
import random
from tower_class import Tower as lt
# Even though import runs the whole code of a file, importing the fileNAME will import a MODULE butname
# importing FROM filename using the CLASS NAME will import AS CLASS and not module.

class Lightning_tower(lt):
    def __init__(self):
        super().__init__("Lightning tower", 72, 550, 450, 30/5, True, False, False)

    def Lightning_attack(self):
        
        a = random.randint(1,20)
        if (a <= self.crit_chance):
            self.damage *= 2
            print("The Lightning tower stunned the target for 2 seconds")
        sleepdata = 1000/self.attackspeed
        sleep(sleepdata)
        format_float = "{:.2f}".format(sleepdata)
        print("The Lightning tower attacked for", self.damage, "damage after", format_float, "seconds with a range of", self.range )

lightning_tower = Lightning_tower()
lightning_tower.Lightning_attack()

