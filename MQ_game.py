import random

def yes_no(question):

    # Checks user response is yes / no

    while True:

        response = input(question).lower()

        #check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
           return "no"
        else:
            print("please enter yes / no")

def instructions():
    """Prints instructions"""

    print("""
*** Instructions ***

Do a math quiz about addition and subtraction, adding and subtracting numbers under 20.
At the end check how many you got right with your quiz history!
To start type 'fixed' if you want a select amount of questions and 
press 'enter' / input 'infinite' if wanting unlimited questions
Good Luck!
    """)

# Main routine

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("do you want instruction")

# Display the instructions if the user want to see them
if want_instructions == "yes":
    instructions()

print ()
print()

def get_integer_input(prompt, min_value=None, max_value=None):
    #Function to get a valid integer input from user with optional bounds checking.
    while True:
        try:
            user_input = int(input(prompt))
            if (min_value is not None and user_input < min_value) or \
                    (max_value is not None and user_input > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
                continue
            return user_input
        except ValueError:
            print("Please enter an number between 1 - 20")


def generate_question():
    #Generate a random addition or subtraction question.
    operation = random.choice(["+", "-"])
    num1 = random.randint(0, 20)
    num2 = random.randint(0, 20)

    if operation == "-" and num2 > num1:
        #Swap to avoid negative answers
        num1, num2 = num2, num1

    if operation == "+":
        question = f"{num1} + {num2}"
        answer = num1 + num2
    else:
        question = f"{num1} - {num2}"
        answer = num1 - num2

    return question, answer


def main():
    print("Welcome to a addition and subtraction quiz!")

    while True:
        mode = input(
            "Do you want 'fixed number of questions' or 'infinite mode? ").strip().lower()
        if mode == "" or mode == "fixed":
            break
        else:
            print("Please press Enter for infinite mode or type 'fixed'.")

    quiz_history = []
    score = 0
    question_number = 0

    if mode == "fixed":
        num_questions = get_integer_input("How many questions would you like to answer? (Enter a number between 1 and 20): ", 1,
                                          20)
    else:
        num_questions = None  # Infinite mode

    while True:
        question_number += 1
        question, correct_answer = generate_question()
        print(f"\nQuestion {question_number}: {question}")

        user_answer = get_integer_input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            result = "Correct"
            score += 1
        else:
            print(f"Incorrect. The correct answer was {correct_answer}.")
            result = "Incorrect"

        quiz_history.append({
            "number": question_number,
            "question": question,
            "correct_answer": correct_answer,
            "user_answer": user_answer,
            "result": result
        })

        if mode == "fixed":
            if question_number >= num_questions:
                break
        else:
            continue_playing = input("Play again?: ").strip().lower()
            if continue_playing != "yes":
                break

    # Summary
    print("\nMath quiz Completed!")
    percentage = (score / question_number) * 100
    print(f"You got {score} out of {question_number} correct. ({percentage:.1f}%)")

    # Option to see history
    show_history = input("\nWould you like to see your quiz history? (yes/no): ").strip().lower()
    if show_history == "yes":
        print("\nQuiz History:")
        for item in quiz_history:
            print(f"Q{item['number']}: {item['question']}")
            if item['result'] == "Correct":
                print(f"✅✅ Correct! Your answer: {item['user_answer']}\n")
            else:
                print(f"❌❌ Incorrect. Your answer: {item['user_answer']}, Correct answer: {item['correct_answer']}\n❌❌")


if __name__ == "__main__":
    main()
