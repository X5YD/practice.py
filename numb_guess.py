import random
def ifs(user_input, bot_guess):
    if user_input < bot_guess:
        return "Too Low"
    elif user_input > bot_guess:
        return "Too High"
    else:
        return "Correct...!"
def game_calc():
    bot_guess = random.randint(1, 100)
    attempts = 0
    result = None
    while True:
        user_input = input("Guess The Number [Type Quit To Leave]  : ")
        if user_input.lower() == "quit":
            break
        try:
            user_input = int(user_input)
            result = ifs(user_input, bot_guess)
            attempts += 1
            print(f"{result} \nAttempts : {attempts}")
            if result == "Correct...!":
                print(f"You Have Comepleted The Game In {attempts} Attemps")
                break
        except ValueError:
            print("Thats Not A Number...! ")
    return result