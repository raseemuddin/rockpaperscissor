import random

user_input = input("enter rock,paper,scissor : ")

actions_array = ["rock","paper","scissor"]
computer_input = random.choice(actions_array)

if (user_input == computer_input):
    print("match draw")
elif (computer_input == "rock" and user_input == "paper"):
    print("computer input is rock and you win")
elif (computer_input == "rock" and user_input == "scissor"):
    print("computer input is rock and you loose")
elif (computer_input == "scissor" and user_input == "paper"):
    print("computer input is scissor and you loose")
elif (computer_input == "scissor" and user_input == "rock"):
    print("computer input is scissor and you win")
elif (computer_input == "paper" and user_input == "rock"):
    print("computer input is paper and you loose")
elif (computer_input == "paper" and user_input == "scissor"):
    print("computer input is paper and you win")                 