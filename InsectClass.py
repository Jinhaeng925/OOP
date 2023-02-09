import random

# The Insect class simulates an insect


class Insect:
    # The _ _init_ _ method initializes the
    # insect to have 2 wings and 2 legs
    # Capitalize the first letter of the Class Name as best practice

    def __init__(self, n, w, l):
        self.name = n
        self.wings = w
        self.legs = l
        self.flight = 0

    # The length method determines the length of flight
    # randomly chooses between 1-10 miles

    def flightLength(self):
        self.flight = random.randint(1, 10)

    # The get_flightLength method returns the value
    # referenced by flightLength

    def get_flightLength(self):
        return self.flight

    # The get_insectName method returns the name of the insect

    def get_insectName(self):
        return self.name
