from time import sleep
import random
from tower_class import Tower as wt
# Even though import runs the whole code of a file, importing the fileNAME will import a MODULE butname
# importing FROM filename using the CLASS NAME will import AS CLASS and not module.

class Wololo_tower(wt):
    def __init__(self):
        super().__init__("Arrow tower", 8, 1500, 375, 0, True, False, False)

    def Wololo_attack(self):
        
        a = random.randint(1,100)
        if (a <= 1):
            print("The Wololo tower converted the enemy")
        sleepdata = 1000/self.attackspeed
        sleep(sleepdata)
        format_float = "{:.2f}".format(sleepdata)
        print("The Wololo tower attacked for", self.damage, "damage after", format_float, "seconds with a range of", self.range )

wololo_tower = Wololo_tower()
wololo_tower.Wololo_attack()

