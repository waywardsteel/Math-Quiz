# functions go here

def yes_no(question):

    # Checks user response to a question is yes / no ***

    while True:

        response = input(question).lower()

        #check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "no":
           return "no"
        else:
            print("please enter yes / no")

def instructions():
    """Prints instructions"""

    print("""
*** Instructions ****

Do a math quiz about addition and subtraction, adding and subtracting numbers under 20.
At the end check how many you got right with your quiz history!
To start type 'fixed' if you want a select amount of questions and press 'enter' / input 'infinite' if wanting unlimited questions
Good Luck!
    """)

# Main routine

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("do you want instruction")

# Display the instructions if the user want to see them...
if want_instructions == "yes":
    instructions()

print ()
print("Program continues")