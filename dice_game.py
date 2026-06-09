import random

# ● ┌ ─ ┐ └ ┘
def dice_ascii():
    dice_art = {
        1: ("┌─────────┐",
            "|         |",
            "|    ●    |",
            "|         |",
            "└─────────┘"),
        2: ("┌─────────┐",
            "| ●       |",
            "|         |",
            "|       ● |",
            "└─────────┘"),
        3: ("┌─────────┐",
            "| ●       |",
            "|    ●    |",
            "|       ● |",
            "└─────────┘"),
        4: ("┌─────────┐",
            "| ●     ● |",
            "|         |",
            "| ●     ● |",
            "└─────────┘"),
        5: ("┌─────────┐",
            "| ●     ● |",
            "|    ●    |",
            "| ●     ● |",
            "└─────────┘"),
        6: ("┌─────────┐",
            "| ●     ● |",
            "| ●     ● |",
            "| ●     ● |",
            "└─────────┘"),
    }
    return dice_art

def dice_game():
    dice_art = dice_ascii()
    dice = []
    total = 0
    while True:
        dice = []
        total = 0
        dice_numb = input("How Many Dice? [Q To Quit] : ").lower().strip()
        if dice_numb == "q":
            break
        dice_numb = int(dice_numb)
        for times in range(dice_numb):
            dice.append(random.randint(1, 6))
        for numb in range(5):
            for die in dice:
                print(dice_art.get(die)[numb], end= "")
            print()
        for value in dice:
            total += value
        print(f"Total : {total}")
dice_game()