import random

choices = ["rock", "paper", "scissors"]

while True:
    user_score = 0
    computer_score = 0

    print("""=== Rock-Paper-Scissors Game ===
1. Start
2. Exit""")

    user_input = input("Enter your choice: ")

    if user_input == '1':
        while True:
            for round_num in range(1, 6):
                print("\n=== Round {} ===".format(round_num))

                print("1. Rock\t2. Paper\t3. Scissors")

                user_choice = int(input("Enter your choice (1-3): "))
                if user_choice not in [1, 2, 3]:
                    print("Invalid choice. Please choose 1, 2, or 3.")
                    continue

                user_choice = choices[user_choice - 1]
                computer_choice = random.choice(choices)

                print("\nYour Choice: {}\tComputer's Choice: {}".format(user_choice, computer_choice))

                if user_choice == computer_choice:
                    print("It's a draw!")
                    user_score += 1
                    computer_score += 1
                elif (user_choice == "rock" and computer_choice == "scissors") or \
                    (user_choice == "paper" and computer_choice == "rock") or \
                    (user_choice == "scissors" and computer_choice == "paper"):
                    print("You win this round!")
                    user_score += 1
                else:
                    print("Computer wins this round!")
                    computer_score += 1

            print("\n===== Game Score =====")
            print("Your Score: {}\tComputer Score: {}".format(user_score, computer_score))
            print("=======================")

            if user_score == computer_score:
                print("The game is a draw.")
            elif user_score > computer_score:
                print("Congratulations! You win the game.")
            else:
                print("Sorry, the computer wins the game.")

            play_again = input("Do you want to play another round? (yes/no): ").lower()
            if play_again != 'yes':
                break

    elif user_input == '2':
        print("Exiting the game. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1 or 2.")
