




def declare_winner(fighter1, fighter2, first_attacker):
    b = True if fighter1.name == first_attacker else False
    loop = True
    while loop:
        if b:
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health < 0:
                loop = False
                return f"{fighter1.name} attacks {fighter2.name}: {fighter2.name} now has {fighter2.health} health and is dead. {fighter1.name} wins."
            b = not b
        else:
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health < 0:
                loop = False
                return f"{fighter2.name} attacks {fighter1.name}: {fighter1.name} now has {fighter1.health} health and is dead. {fighter2.name} wins."