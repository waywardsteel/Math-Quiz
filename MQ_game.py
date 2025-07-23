import random

# checks user response, question
# repeats if users don't enter yes / no
def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes or no.")

# === PROGRAM START ===
print("Welcome to the addition and subtraction quiz!")

def instructions():
    print("""
*** Instructions ***

This is a math quiz about addition and subtraction.
- All questions use numbers under 20.
- You can choose a fixed number of questions or unlimited questions.
- After the quiz, you'll see your score and quiz history.

To start:
- Type 'fixed' to choose how many questions you want.
- Or press Enter to play in infinite mode.

Good luck!
""")


def get_integer_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            user_input = int(input(prompt))
            if (min_value is not None and user_input < min_value) or \
                    (max_value is not None and user_input > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
                continue
            return user_input
        except ValueError:
            print("Please enter a valid whole number.")

# random number generator for +, - and x
def generate_question():
    operation = random.choice(["+", "-", "*"])
    num1 = random.randint(0, 12)
    num2 = random.randint(0, 12)

    if operation == "-" and num2 > num1:
        num1, num2 = num2, num1

    if operation == "+":
        question = f"{num1} + {num2}"
        answer = num1 + num2
    elif operation == "-":
        question = f"{num1} - {num2}"
        answer = num1 - num2
    else:  # multiplication
        question = f"{num1} × {num2}"
        answer = num1 * num2

    return question, answer




# ask if want instructions
want_instructions = yes_no("Do you want instructions? (yes/no): ")
if want_instructions == "yes":
    instructions()

# ask if want infinite or fixed amout of questions
while True:
    mode = input("Do you want 'fixed' mode or 'infinite' mode: ").strip().lower()
    if mode == "fixed" or mode == "":
        break
    else:
        print("Invalid input. Please type 'fixed' or press Enter.")

quiz_history = []
score = 0
question_number = 0

# see how many questions they want
if mode == "fixed":
    num_questions = get_integer_input("How many questions would you like? (1 to 20): ", 1, 20)
else:
    mode = "infinite"
    num_questions = None


# correct - yes or no
while True:
    question_number += 1
    question, correct_answer = generate_question()
    print(f"\nQuestion {question_number}: {question}")

    user_answer = get_integer_input("Your answer: ")

    if user_answer == correct_answer:
        print("✅ Correct!")
        result = "Correct"
        score += 1
    else:
        print(f"❌ Incorrect. The correct answer was {correct_answer}.")
        result = "Incorrect"

    history_line = f"Q{question_number}: {question} | Your Answer: {user_answer} | Correct: {correct_answer} | {result}"
    quiz_history.append(history_line)

    # In infinite mode, it just keeps going automatically
    if mode == "fixed":
        if question_number >= num_questions:
            break

    else:
        keep_going = yes_no("Do you want to continue? (yes/no): ")
        if keep_going == "no":
            break


#END OF QUIZ

#show score
print("\n🎉 Math quiz complete!")
print(f"You got {score} out of {question_number} correct.")

#GAME HISTORY

#check if user wants to see game history
if yes_no("Do you want to see game history? yes / no ") == "yes":
    for line in quiz_history:
        print(line)
else:
    print("🎉Ok thanks for playing🎉")