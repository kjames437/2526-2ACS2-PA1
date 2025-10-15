'''
Continuation of classwork, graded on completion/effort.

Write a program that allows people to add, drop, and change a mod schedule.

Add functionality to loop this 7 times or whatever for d and e blocks and give an option 
to make and diplay a full year schedule

'''

mod1 = {
    "A_Block": "",
    "B_Block": "",
    "C_Block": "",
    "D_Block": "",
    "E_Block": ""}

mod2 = {
    "A_Block": "",
    "B_Block": "",
    "C_Block": "",
    "D_Block": "",
    "E_Block": ""}

mod3 = {
    "A_Block": "",
    "B_Block": "",
    "C_Block": "",
    "D_Block": "",
    "E_Block": ""}

mod4 = {
    "A_Block": "",
    "B_Block": "",
    "C_Block": "",
    "D_Block": "",
    "E_Block": ""}

mod5 = {
    "A_Block": "",
    "B_Block": "",
    "C_Block": "",
    "D_Block": "",
    "E_Block": ""}

mod6 = {
    "A_Block": "",
    "B_Block": "",
    "C_Block": "",
    "D_Block": "",
    "E_Block": ""}

mod7 = {
    "A_Block": "",
    "B_Block": "",
    "C_Block": "",
    "D_Block": "",
    "E_Block": ""}

#parameters: a dictionary called schedule
#returns: a schedule with an added class
def add_class(schedule):
    input("Please enter the class you would like to add:")
    input == A_Block
    ...
    return schedule

#parameters: a dictionary called schedule
#returns: a schedule with a changed, preexisting class
def change_class(schedule):
    ...
    return schedule

#parameters: a dictionary called schedule
#returns: a schedule with a removed class
def drop_class(schedule):
    .pop
    ...
    return schedule

#main function
def main():
    print("Welcome to Mrs. Carroll's office.")
    user_choice = input("What would you like to do?").lower()
    valid_actions = ["add","drop","change","exit"]
    while user_choice not in valid_actions:
        print("Error. Please pick add, drop, change, or exit.")
        user_choice = input("What would you like to do?").lower()
    while user_choice != "exit":
        if user_choice == "add":
            mod2 = add_class(mod2)
        elif user_choice == "drop":
            mod2 = drop_class(mod2)
        else:
            mod2 = change_class(mod2)
        user_choice = input("Anything else? ")
        while user_choice not in valid_actions:
            print("Error. Please pick add, drop, change, or exit.")
            user_choice = input("Anything else? ").lower()
    print("Thanks for stopping by!")

main()