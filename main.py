from rooms import room_choose
from find_note import note_game
from numb_guess import game_calc


def lvl_one():
    room = room_choose()
    if room == "room1":
        print("You Have Entered Room One...! ")
        note_game()
    elif room == "room2":
        print("You Have Entered Room Two...! ")
        game_calc()
lvl_one()