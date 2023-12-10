import string
import random

len = int(input("Enter the Length for Password : "))
print("---Select from the following list in which form you want the password---\n")
print("1. Digits\n")
print("2. Letters\n")
print("3. Special Characters\n")
print("4. Exit\n")

characterList = ""
while(True):
    choice = int(input("Enter Your Choice 1, 2, 3, 4 : "))

    if(choice == 1):
        characterList += string.digits

    elif(choice == 2):
        characterList += string.ascii_letters

    elif(choice == 3):
        characterList += string.punctuation

    elif(choice == 4):
        break

    else:
        print("Please pick a valid option !")

password = []
for i in range(len):
    randomchar = random.choice(characterList)
    password.append(randomchar)
print("Your random Password is " + "".join(password))
