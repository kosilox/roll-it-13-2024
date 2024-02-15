# checks if users enter yes or no
def yes_no(question):


    while True:
        print("🎲🎲Roll it 13🎲🎲")
        Response = input(question).lower()

        if Response== "yes" or Response== "y":
            return "yes"
        elif Response== "no" or Response== "n":
            return "no"
        else:
            print("you did not choose a valid response")
# Main routine
want_instructions = yes_no("Do you want to read the instructions?")