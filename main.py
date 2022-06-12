import random
possible_actions = ["R", "P", "S"]
playername=input("Please enter your name:").title()
CPU="CPU"
dic={}

print("Welcome",playername)

while True:
    player = input("Enter a choice (R, P, S): ").title()
    dic[playername]=player
    CPU_choice = random.choice(possible_actions)
    dic[CPU]=CPU_choice
    print(playername,"picks",player)
    print("CPU picks",CPU_choice)
    print(dic)
    if player not in possible_actions:
        print("Invalid Input,Try Again")

    elif player == CPU_choice:
        print(f"Both players selected {player}. It's a tie!")
    elif player == "R":
        if CPU_choice == "S":
            print("Rock beats scissors! You win!")
        else:
            print("Paper beats rock! You lose.")
    elif player == "P":
        if CPU_choice == "R":
            print("Paper beats rock! You win!")
        else:
            print("Scissors beats paper! You lose.")
    elif player == "S":
        if CPU_choice == "P":
            print("Scissors beats paper! You win!")
        else:
            print("Rock beats scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
    
