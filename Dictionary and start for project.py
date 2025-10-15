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
    input == Block
    ...
    return schedule

#parameters: a dictionary called schedule
#returns: a schedule with a changed, preexisting class
def change_class(schedule):
    input == Block
    ...
    return schedule

#parameters: a dictionary called schedule
#returns: a schedule with a removed class
def drop_class(schedule):
    Block == ""
    ...
    return schedule

#main function
def main():
    print("Welcome to Mrs. Carroll's office.")
    mod = input("Which mod would you like to edit?").lower()
    valid_actions3 = ["mod 1","mod 2","mod 3","mod 4","mod 5","mod 6","mod 7"]
    user_choice = input("What would you like to do?").lower()
    valid_actions = ["add","drop","change","exit"]
    while user_choice not in valid_actions:
        print("Error. Please pick add, drop, change, or exit.")
        user_choice = input("What would you like to do?").lower()
    user_choice2 = input("Which class would you like to edit?").lower()
    valid_actions = ["a block","b block","c block"]
    while user_choice not in valid_actions:
        print("Error. Please pick a block, b block, or c block.")
        user_choice2 = input("Which class would you like to edit?").lower()
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