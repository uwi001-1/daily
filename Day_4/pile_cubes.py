#Pile up cubes vertically
#They must be piled from largest to smallest

def pile_up_cubes(cubes):
    for i in range(len(cubes) - 1):
        if cubes[i] < cubes[i + 1]:
            return False
    return True

cubes = [4, 3, 2, 1]
if pile_up_cubes(cubes):
    print("Yes, they can be piled.")
else:
    print("No, they can't be piled.")