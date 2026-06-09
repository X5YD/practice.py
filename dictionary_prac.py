def menu_storage():
    menu = {"pizza": 3.00,
            "nachos": 4.50,
            "popcorn": 6.00,
            "fries": 2.50,
            "chips": 1.00,
            "pretzel": 3.50,
            "soda": 3.00,
            "lemonade": 4.25}
    return menu


def con():
    menu = menu_storage()
    cart = []
    total = 0
    print("-----MENU-----")
    for items, values in menu.items():
        print(f"{items:<10} : ${values:.2f}")
    while True:
        user_input = input("Enter The Items That You Want [Q To Quit] :").lower().strip()
        if user_input == "q":
            break
        elif menu.get(user_input) is not None:
            cart.append(user_input)
    for item in cart:
        total += menu.values(item)
    print(f"Your Total Is : ${total}")
con()