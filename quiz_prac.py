def q():
    questions = ("What Does STR Mean In Python? ",
                "Who Is The Creator Of Linux? ",
                "What Is The Hardest Programing Language? ")
    return questions


def a():
    answers = (("A. Float", "B. Integer", "C. Boolean", "D. String"),
               ("A. Bill Gates", "B. Steve Jobs", "C. Linus Torvalds", "D. Big Daddy Zuck"),
               ("A. Python", "B. HTML", "C. C++", "D. JavaScript"))
    return answers


def quiz():
    answers = a()
    questions = q()
    options = ("D", "C", "C")
    user_answers = []
    answers_index = 0
    score = 0
    for question in questions:
        print("----------------")
        print(question)
        for answer in answers[answers_index]:
            print(answer)
        user_answer = input("Enter Your Answer [| A | B | C | D |] ").upper()
        user_answers.append(user_answer)
        if user_answer == options[answers_index]:
            print("Correct..!")
            score += 1
        else:
            print("Incorrect..!")
        answers_index += 1
    print("----------")
    print(  "RESULT"  )
    print("----------")
    print(f"Answers: ")
    for option in options:
        print(option, end= " ")
    print(" ")
    print(f"Guesses: ")
    for answer in user_answers:
        print(answer, end=" ")
    score = int(score / len(questions) * 100 )
    print(f"\n Score : {score}%")
quiz()