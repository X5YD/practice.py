def email_v():
    while True:
        user_email = input(f"Enter Your Email : [Must Have @ and . ]\nType Quit To Stop : ").lower().strip()
        if user_email == "quit":
            break
        at_index = user_email.find("@")
        dot_index = user_email.find(".")
        if at_index or dot_index != -1 and at_index < dot_index:
            print("Valid ✔️ !")
            break
        else:
            print("Invalid ❌ ")
email_v()