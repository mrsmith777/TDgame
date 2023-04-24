
# #it works if the main is in the same folder
# from arrow_tower import arrow_tower_instance
# #called the arrow tower as instance so I know that the towers were instanciated this way
# from poision_tower import poision_tower
# from magic_tower import magic_tower
# from whirlwind_tower import whirlwind_tower
# from wololo_tower import wololo_tower
# from lightning_tower import lightning_tower
# from luminous_tower import luminous_tower
''' T1 tower imports'''
''' It's probably not a good practice to import in a function '''


def T1_tower_attacks():
    
    print(" T1 tower attack simulations: \n")
    from arrow_tower import arrow_tower_instance
    from poision_tower import poision_tower
    from magic_tower import magic_tower
    from whirlwind_tower import whirlwind_tower
    from wololo_tower import wololo_tower
    from lightning_tower import lightning_tower
    from luminous_tower import luminous_tower
    print("\n End of simulation °_° \n")

def T2_tower_attacks():
    pass

T1_tower_attacks()




