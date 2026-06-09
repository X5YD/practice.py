questions = ("What is the capital of France?",
             "What is the largest planet in our solar system?", 
             "What is the chemical symbol for gold?", 
             "Who painted the Mona Lisa?", 
             "What is the longest river in the world?")

options = (("A. Paris", "B. London", "C. Berlin", "D. Rome"),
           ("A. Jupiter", "B. Saturn", "C. Mars", "D. Venus"),
           ("A. Ag", "B. Au", "C. Al", "D. Fe"),
           ("A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"),
           ("A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"))

answers = ("A", "A", "B", "C", "A")

guesses = []
score = 0
question_numb = 0

for question in questions:
    print("__________________________")
    print(question)
    for option in options[question_numb]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_numb]:
        score += 1
        question_numb += 1
print("__________________________")
print("RESULTS")
print("Answers: ", end="")
for answer in answers:
    print(f"{answer}" , end= " ")
print(" ")
print("Guesses: ", end="")
for guess in guesses:
    print(f"{guess}", end=" ")
score = int(score / len(questions) * 100)
print(f"\nYour score is: {score}%")