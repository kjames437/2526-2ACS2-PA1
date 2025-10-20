'''
This is a schedular app where people can add, drop or change classes

I am proud of the add, drop and change functions

If I had more time I would add e block seasons

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
def add_class(mod, block):
    block = input("Please enter the name of the class you would like to add:")
    #update the class in schedule variables
    [mod] = block
    return mod

#parameters: a dictionary called schedule
#returns: a schedule with a changed, preexisting class
def change_class(mod, block):
    block = input("Please enter the class name you would like to change your class to:")
    ...
    return mod

#parameters: a dictionary called schedule
#returns: a schedule with a removed class
def drop_class(mod, block):
    Block = ""
    ...
    return mod

#main function
def main():
    print("Welcome to Mrs. Carroll's office.")
    mod = input("Which mod would you like to edit?").lower() #gets which mod to change
    if mod == "1":
        mod = mod1
    elif mod == "2":
        mod = mod2
    elif mod == "3":
        mod = mod2
    elif mod == "4":
        mod = mod2
    elif mod == "5":
        mod = mod2
    elif mod == "6":
        mod = mod2
    elif mod == "7":
        mod = mod2
    valid_actions3 = ["mod 1","mod 2","mod 3","mod 4","mod 5","mod 6","mod 7"]
    user_choice = input("What would you like to do? Please enter add, drop, change or exit:").lower()
    valid_actions = ["add","drop","change","exit"]
    while user_choice not in valid_actions:
        print("Error. Please pick add, drop, change, or exit.")
        user_choice = input("What would you like to do? Please enter add, drop, change or exit:").lower()
    user_choice2 = input("Which block would you like to edit? Please enter a block, b block or c block:").lower() #gets which block to edit
    valid_actions = ["a block","b block","c block"]
    while user_choice2 not in valid_actions:
        print("Error. Please pick a block, b block, or c block.")
        user_choice2 = input("Which block would you like to edit? Please enter a block, b block or c block:").lower()
    while user_choice != "exit": #user choice 2 only with blocks
        if user_choice2 == "add":
            mod = add_class(mod, user_choice2)
        elif user_choice2 == "drop":
            mod = drop_class(mod)
        elif user_choice2 == "change":
            mod = change_class(mod)
        user_choice4 = input("Anything else? Please pick add, drop, change or exit ")
        valid_actions2 = ["add","drop","change","exit"]
        while user_choice4 not in valid_actions2:
            print("Error. Please pick add, drop, change, or exit.")
        if user_choice4 == "exit":
            user_choice3 = input("Would you like to add a d block? Please say yes or no:")
            if user_choice3 == "yes":
                    d_blockF = input("Please type your d block choice for fall:")
                    d_blockF == mod1 ["D_Block"]
                    d_blockF == mod2 ["D_Block"]
                    d_blockW = input("Please type your d block choice for winter:")
                    d_blockW == mod3 ["D_Block"]
                    d_blockW == mod4 ["D_Block"]
                    d_blockW == mod5 ["D_Block"]
                    d_blockS = input("Please type your d block choice for spring:")
                    d_blockS == mod6 ["D_Block"]
                    d_blockS == mod7 ["D_Block"]
            if user_choice3 == "no":
                if user_choice4 == "exit":
                    user_choice5 = input("Would you like to add an e block? Please say yes or no:")
                    if input == "yes":
                        e_block = input("Please enter your e block choice:")
                        e_block == mod1 ["E_Block"]
                        e_block == mod2 ["E_Block"]
                        e_block == mod3 ["E_Block"]
                        e_block == mod4 ["E_Block"]
                        e_block == mod5 ["E_Block"]
                        e_block == mod6 ["E_Block"]
                        print("Thanks for stopping by, Here is your schedule!")
                        print(mod1)
                        print(mod2)
                        print(mod3)
                        print(mod4)
                        print(mod5)
                        print(mod6)
                        print(mod7)
                    if user_choice5 == "no":
                        print("Thanks for stopping by, Here is your schedule!")
                        print(mod1)
                        print(mod2)
                        print(mod3)
                        print(mod4)
                        print(mod5)
                        print(mod6)
                        print(mod7)

main()