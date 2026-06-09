import random
def rpc_calc(bot_choice, user_choice):
    if bot_choice == "rock" and user_choice == "paper":
        return (f"{bot_choice} : You Won")
    elif bot_choice == "rock" and user_choice == "scissors":
        return (f"{bot_choice} : You Lost")
    elif bot_choice == "paper" and user_choice == "scissors":
        return (f"{bot_choice} : You Won")
    elif bot_choice == "paper" and user_choice == "rock":
        return (f"{bot_choice} : You Lost")
    elif bot_choice == "scissors" and user_choice == "rock":
        return (f"{bot_choice} : You Won")
    elif bot_choice == "scissors" and user_choice == "paper":
        return (f"{bot_choice} : You Lost")
    else:
        return (f"{bot_choice} : Draw")
def rpc_game():    
    score = 0
    while True:
        bot_choice = random.choice(["rock", "paper", "scissors"])
        user_choice = input("Enter Your Choice [|Rock|Paper|Scissors] Q To Quite : ").lower().strip()
        if user_choice == "q":
            break
        result = rpc_calc(bot_choice, user_choice)
        print(result)
        if rpc_calc(bot_choice, user_choice) == ("You Won"):
            score += 1
    print(f"Your Score : {score}")
rpc_game()