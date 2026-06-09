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

    numb_of_dice = int(input("How Many Dice?: "))


    for die in range(numb_of_dice):
        dice.append(random.randint(1, 6))

    for die in dice:
        for line in dice_art.get(die):
            print(line)

    for die in dice:
        total += die
    print (f"Total : {total}")
dice_game()
    