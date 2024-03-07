import random


# generates an integer between 0 and 6
# to simulate a roll of a die
def roll_die():
    roll_result = random.randint(1, 6)
    return roll_result


# rolls two dice and returns total and whether we
# had a double roll

def two_rolls(who):
    double_score = "no"

    # roll two dice

    roll_1 = roll_die()
    roll_2 = roll_die()

    # checks if they have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Finds the total points (so far)
    first_points = roll_1 + roll_2

    # Show the user the result
    print(f"{who} {roll_1} & {roll_2} - Total: {first_points} ")
    return first_points, double_score


# checks that users enter an integer

# that is more than 13

def int_check(question):
    while True:
        error = "Please enter an integer that is 13 or more"

        try:
            response = int(input(question))
            # checks that the number is more than / equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print("Please enter an integer that is 13 or more")


# main routine goes here


# initialise user score and computer score
user_score = 0
comp_score = 0
num_rounds = 0

target_score = int_check("Enter a target score: ")

while user_score < target_score and comp_score < target_score:
    # Add one to the number of rounds (for our heading)
    num_rounds += 1
    print(f"🎲🎲🎲 Round {num_rounds}🎲🎲🎲")

    # Start of a single round

    # initialise 'pass' variables
    user_pass = "no"
    computer_pass = "no"

    # Start round...
    input("Press <enter> to begin this round:")

    # Get initial dice rolls for user

    user_first = two_rolls("User")
    user_points = user_first[0]
    double_points = user_first[1]

    # intialise roll again so its not undefined
    roll_again = ""

    # Tell the user if they are eligible for double score
    if double_points == "yes":
        print("If you win this round, you gain double points!")

    # Get initial dice rolls for computer
    computer_first = two_rolls("Computer")
    computer_points = computer_first[0]

    # print(f"The computer rolled a total of {computer_points}.")

    # loop (while both user / computer have <= 13 points)...
    while computer_points < 13 and user_points < 13:
        # user_pass = "no"

        # ask user if they want to roll again, update
        # points / status
        if user_points == 13:
            user_pass = "yes"

        # if user_pass == "no":
        elif user_pass == "no":
            roll_again = input("Do you want to roll the dice"
                               "(type 'no' to pass)")

        if roll_again == "no":
            user_pass = "yes"

        if roll_again == "yes":
            user_move = roll_die()
            user_points += user_move

            # if user goes over 13 points, tell them that they lose and set points to 0
            if user_points > 13:
                print(f"💥💥💥Oops! You rolled a {user_move} so your total is {user_points} "
                      f"Which is over 13 points . 💥💥💥 ")

                # reset user points to zero so that when we update their
                # score at the end of round it is correct.
                user_points = 0

                break
            else:
                print(f"you rolled a {user_move} and have a total score of {user_points}.")

        # if computer has 10 points or more (and is winning),
        # it should pass!
        # computer_pass = "no"

        if computer_points >= 10 and computer_points >= user_points:
            computer_pass = "yes"

        # computer rolls dice only if it has not passed
        if computer_pass == "yes":
            pass

        else:
            # Roll die for computer and update computer points
            computer_move = roll_die()
            computer_points += computer_move

            # check computer has not gone over...
            if computer_points > 13:
                print(f"💥💥💥The computer rolled a {computer_move}. The computer "
                      f" now has {computer_points}. This is over 13 points so the computers loses! 💥💥💥")
                computer_points = 0
                break
            else:
                print(f"The computer rolled a {computer_move}. The computer "
                      f"now has {computer_points}.")
                print()

        # tell user if they are winning, losing or if it's a tie.
        if user_points > computer_points:
            result = "😖😖😖You are ahead.😖😖😖"
        elif user_points < computer_points:
            result = "😱😱😱The computer is ahead!😱😱😱"
        else:
            result = "🐺It's currently a tie!🐺"

        print(f"***Round Update***: {result} ")
        print(f"User score: {user_points} \t | \t Computer score: {computer_points}")

        # code idented below as otherwise round des nut end!
        if computer_pass == "yes" and user_pass == "yes":
            break

    # Outside loop - double user points if they won and are eligible

    # Show rounds result
    print()

    if user_points < computer_points:
        print("Sorry - you lost this round and no points "
              "have been added to your total score. The computer's score has "
              f"increased by {computer_points} points. ")
        add_points = computer_points
    # currently does not include double points!
    elif user_points > computer_points:
        # Double user points if they are eligible
        if double_points == "yes":
            user_points *= 2

        print(f"Yay! You won the round and {user_points} points have "
              f"been added to your score")
        add_points = user_points
    else:
        print(f"👍👍👍The result for this round is a tie. You and the computer "
              f"both have {user_points}👍👍👍")
        add_points = user_points

    # end of a single round

    # if user wins then points are added
    if user_points < computer_points:
        comp_score += add_points

    # if the user wins add their points to their score
    elif user_points > computer_points:
        user_score += add_points

    # if it's a tie add the points to both scores
    else:
        comp_score += add_points
        user_score += add_points
    print()
    print(f"User: {user_score} points | Computer: {comp_score} points")
    print()
