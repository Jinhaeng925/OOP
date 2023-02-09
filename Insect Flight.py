import InsectClass as ins


# The main function.
def main():

    wings = 2
    legs = 4
    # Create an object from the InsectClass.
    # this creates an instance called 'mosquito' of the class 'Insect()'
    mosquito = ins.Insect('mosquito', wings, legs)
    # this creates an instance called 'mosquito' of the class 'Insect()'
    houseFly = ins.Insect('housefly', wings, legs)

    # get flight length for mosquito and houseFly
    mosquito.flightLength()
    houseFly.flightLength()

    # Display the side of the coin that is facing up.
    print(
        f"The {mosquito.get_insectName()} can fly: {mosquito.get_flightLength()} miles")
    print(
        f"The '{houseFly.get_insectName()}' can fly: {houseFly.get_flightLength()} miles")


# Call the main function.
main()
