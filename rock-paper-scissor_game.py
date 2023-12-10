import random

print("---Rules for playing Rock - Paper - Scissor Game---\n")
print("Rock Vs. Paper -> Paper wins")
print("Paper Vs. Scissor -> Scissor wins")
print("Scissor Vs. Rock -> Rock wins")

while True:

    choice = int(input("Enter your Choice\n1. Rock\n2. Paper\n3. Scissor\n"))

    while choice > 3 or choice < 1 :
        choice = int(input("Please enter a valid choice : "))

    if choice == 1:
        ch_name = 'ROCK'

    elif choice == 2:
        ch_name = 'PAPER'

    else:
        ch_name = 'SCISSOR'

    print("User choice is : ",ch_name,"\n")
    print("Now, it's Computer's turn.")

    comp_choice = random.randint(1,3)

    while comp_choice == choice:
        comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_ch_name = 'rock'

    elif comp_choice == 2:
        comp_ch_name = 'paper'

    else:
        comp_ch_name = 'scissor'

    print("Computer choice is : ",comp_ch_name,"\n")
    print(ch_name,"Vs.",comp_ch_name)

    if choice == comp_choice:
        print("It's a Draw!!",end="")
        result="DRAW"

    if(choice==1 and comp_choice==2):
        print("Paper Wins =>",end="")
        result='paper'
    elif(choice==2 and comp_choice==1):
        print("Paper Wins =>",end="")
        result='PAPER'
    
    if(choice==2 and comp_choice==3):
        print("Scissor Wins =>",end="")
        result='scissor'
    elif(choice==3 and comp_choice==2):
        print("Scissor Wins =>",end="")
        result='SCISSOR'
    
    if(choice==3 and comp_choice==1):
        print("Rock Wins =>",end="")
        result='rock'
    elif(choice==1 and comp_choice==3):
        print("Rock Wins =>",end="")
        result='ROCK'

    if result == 'DRAW':
        print("It's a Tie...\n")
    elif result == ch_name:
        print("<--User Wins-->\n")
    else:
        print("<--Computer Wins-->\n")

    ch=int(input("Do you wish to continue :\n1. Yes\n2. No\n"))
    if ch == 2:
        break

print("~~Thanks For Playing~~")

    