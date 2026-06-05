from note import note_storage
def note_game():
    secret, text = note_storage()
    while True:
        print(f" {text}")
        user_input_note = input("Find The Hidden Number Above [Type Quite To Leave] :  ")
        if user_input_note.lower() == "quite":
            break
        try:
            user_input_note = int(user_input_note)
            if user_input_note == secret:
                print("Correct!  ")
                break
            else:
                print("Try Again...!  ")
        except ValueError:
            print("Thats Not A Number...!  ")
    return(user_input_note)