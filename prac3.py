def student_list():
    students = {"Alireza" : 90,
            "Arshya" : 100,
            "Kasra" : 85,
            "Mani" : 70}
    return students
def grade_checker():
    students = student_list()   
    while True:
        user_input = input("Enter The Name Of The Student [Type Quit To Stop] : ").strip().capitalize()
        if user_input == "Quit":
            break
        if user_input in students:
            print(f"Name : {user_input} Grade : {students.get(user_input)}")
        else:
            print(f"{user_input} Is Not A Student...! ")
grade_checker()