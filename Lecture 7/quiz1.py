from cannon import Cannon


# Build some cannons
cannon_1 = Cannon(25)
cannon_2 = Cannon(10)
cannon_3 = Cannon(1)

# Start firing
cannon_1.fire_ball()
cannon_2.fire_multiple(4)
cannon_3.fire_multiple(6)

# Keep firing
cannon_1.fire_multiple(cannon_2.ammunition + cannon_3.ammunition)

# Quiz
print("Cannon1: {}".format(cannon_1.ammunition))
print("Cannon2: {}".format(cannon_2.ammunition))
print("Cannon3: {}".format(cannon_3.ammunition))

