import random

def get_user_choice():
    while True:
        user_input = input("What's your choice? (rock, paper, or scissors): ").strip().lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Oops! That ain't a valid choice. Try rock, paper, or scissors.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You won this time!"
    else:
        return "Computer wins this round!"

def main():
    print("Hey there! Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer picked: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Wanna play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print("Thanks for playing Rock, Paper, Scissors! See ya next time.")

if __name__ == "__main__":
    main()
    