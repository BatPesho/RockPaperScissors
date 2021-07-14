from random import randint
play_again = True
score = 0
score1 = 0
current_scores = "YOU {} : {} OPPONENT"
first_to_ten_mode = False


def print_move(number):
    if number == 0:
        # Rock
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    if number == 1:
        # Paper
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)

    if number == 2:
        # Scissors
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)


while play_again:
    continue_check = True
    choice_check = True
    while choice_check:
        try:
            choice = int(input("\r\n"+"0 : Rock  1 : Paper  2 : Scissors""\n\n""What will you choose?:"))
        except ValueError:
            print("Please enter a valid number.")
            continue
            pass
        if choice != 0 and choice != 1 and choice != 2:
            print("Please enter a valid number.")
            continue
        else:
            choice_check = False
    print_move(choice)
    choice1 = randint(0, 2)
    print_move(choice1)
    if choice == choice1:
        print("NOBODY WINS!")
        print(current_scores.format(score, score1))
    elif choice == 0 and choice1 == 2:
        print("YOU WIN")
        score += 1
        print(current_scores.format(score, score1))
    elif choice == 2 and choice1 == 0:
        print("YOU LOSE")
        score1 += 1
        print(current_scores.format(score, score1))
    elif choice == 1 and choice1 == 0:
        print("YOU WIN")
        score += 1
        print(current_scores.format(score, score1))
    elif choice == 0 and choice1 == 1:
        print("YOU lOSE")
        score1 += 1
        print(current_scores.format(score, score1))
    elif choice == 2 and choice1 == 1:
        print("YOU WIN")
        score += 1
        print(current_scores.format(score, score1))
    elif choice == 1 and choice1 == 2:
        print("YOU lOSE")
        score1 += 1
        print(current_scores.format(score, score1))
    while continue_check:
      #  if first_to_ten_mode and score == 10 or score1 == 10:

        question = input("Do you want to play again? [y/n]")
        if question == "y" or question == "Y":
            continue_check = False
        elif question == "n" or question == "N":
            play_again = False
            continue_check = False
        else:
            print("Please enter a valid argument")
            continue

exit()

