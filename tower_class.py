
# the crit strike chance of the towers are always divisible by 5 therefore
# in the child classes they are divided by 5 and the roll is always between 1 and 20
# beceause the rng works better with smaller ranges

class Tower:
    def __init__(self, name, damage, attackspeed, range, crit_chance, is_magic, is_poision, is_physical):
        self.name = name
        self.damage = damage
        self.attackspeed = attackspeed
        self.range = range
        self.crit_chance = crit_chance
        self.is_magic = is_magic
        self.is_poision = is_poision
        self.is_physical = is_physical


