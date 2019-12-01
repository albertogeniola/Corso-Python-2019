class Cannon:
    """
    This is the cannon class that we used as main example in the slides.
    This kind of cannon is capable of firing a single bullet as well as
    firing multiple bullets on a row
    """
    def __init__(self, initial_ammunition):
        self.ammunition = initial_ammunition
        self.part_number = '2639836'

    def fire_ball(self):
        print("Firing a ball!")
        if self.ammunition > 0:
            self.ammunition -= 1
        else:
            print("Damn! We are out of ammo!")

    def fire_multiple(self, bullets):
        for i in range(0, bullets):
            self.fire_ball()
