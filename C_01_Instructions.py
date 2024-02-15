# a loop for testing purposes
while True:
    print("🎲🎲Roll it 13🎲🎲")
    want_instructions = input("Do you want to read the instructions?").lower()

    # checks if users enter yes or no
    if want_instructions== "yes" or want_instructions== "y":
        print("you chose yes")
    elif want_instructions== "no" or want_instructions== "n":
        print("you chose no")

    else:
        print("you did not choose a valid response")
