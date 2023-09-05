def plants_vs_zombies(zombies,plants):

    plant_power = sum(plants)
    zombie_power = sum(zombies)

    plant_surv = 0
    zombie_surv = 0
    for i in range(min(len(zombies) , len(plants))):
            if plants[i] > zombies[i]:
                plant_surv += 1
            elif zombies[i] > plants[i]:
                zombie_surv += 1
    if len(zombies) > len(plants):
        zombie_surv = len(zombies) - len(plants)
    elif len(zombies) < len(plants):
        plant_surv = len(plants) - len(zombies)

    if zombie_surv > plant_surv:
        return False
    elif plant_surv > zombie_surv:
        return True
    else:
        if plant_power < zombie_power:
            return False
        else:
            return True

print(plants_vs_zombies([1, 3, 5, 7], [2, 4, 6, 8]))
print(plants_vs_zombies([1, 3, 5, 7], [2, 4]))
print(plants_vs_zombies([1, 3, 5, 7], [2, 4, 0, 8]))
print(plants_vs_zombies([2, 1, 1, 1], [1, 2, 1, 1]))