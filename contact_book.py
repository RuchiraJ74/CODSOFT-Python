import sys

def initial_contactbook():
    rows, cols = int(input("Please enter initial number of contacts : ")), 5

    contact_book = []
    print(contact_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order ONLY : " % (i+1))
        print("NOTE : * indicates mandatory fields")
        print("--------------------------------------------------------------------------")
        temp = []

        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter name* : ")))

                if temp[j] == '' or temp[j] == '':
                    sys.exit("Name is a mandatory field. Process exiting due to blank field...")

            if j == 1:
                temp.append(int(input("Enter number* : ")))

            if j == 2:
                temp.append(str(input("Enter e-mail address : ")))
                if temp[j] == '' or temp[j] == '':
                    temp[j] = None

            if j == 3:
                temp.append(str(input("Enter date of birth(dd/mm/yy) : ")))
                if temp[j] == '' or temp[j] == '':
                    temp[j] = None

            if j == 4:
                temp.append(str(input("Enter category(Family/Friends/Work/Others) : ")))
                if temp[j] == '' or temp[j] == '':
                    temp[j] = None

        contact_book.append(temp)

    print(contact_book)
    return contact_book

def menu():
    print("-------------------------------------------------------------------------------")
    print("SMARTPHONE DIRECTORY", flush=False)
    print("-------------------------------------------------------------------------------")
    print("---You can now perform the following operations on this contactbook---\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit contactbook")

    choice = int(input("Please enter your choice : "))
    return choice

def add_contact(cb):
    dip = []
    for i in range(len(cb[0])):
        if i == 0:
            dip.append(str(input("Enter name : ")))

        if i == 1:
            dip.append(str(input("Enter number : ")))

        if i == 2:
            dip.append(str(input("Enter e-mail address : ")))

        if i == 3:
            dip.append(str(input("Enter date of birth(dd/mm/yy) : ")))

        if i == 4:
            dip.append(str(input("Enter category(Family/Friends/Work/Others) : ")))

    cb.append(dip)
    return cb

def remove_existing(cb):
    query = str(input("Please enter the name of the contact you want to remove : "))

    temp = 0

    for i in range(len(cb)):
        if query == cb[i][0]:
            temp += 1
            print(cb.pop(i))
            print("This query has been removed.")
            return cb
        
    if temp == 0:
        print("Sorry, you have entered an invalid query.\nPlease recheck and try again later.")
        return cb
    
def delete_all(cb):
    return cb.clear()

def search_existing(cb):
    choice = int(input("Enter search criteria\n\n1. Name\n2. Number\n3. Email-id\n4. DOB\n5. Category(Family/Friends/Work/Others)\nPlease enter criteria : "))
    temp = []
    check = -1

    if choice == 1:
        query = str(input("Please enter the name of the contact you want to search : "))
        for i in range(len(cb)):
            if query == cb[i][0]:
                check = i
                temp.append(cb[i])

    elif choice == 2:
        query = int(input("Please enter the number of the contact you want to search : "))
        for i in range(len(cb)):
            if query == cb[i][1]:
                check = i
                temp.append(cb[i])

    elif choice == 3:
        query = str(input("Please enter the e-mail ID of the contact you want to search : "))
        for i in range(len(cb)):
            if query == cb[i][2]:
                check = i
                temp.append(cb[i])

    elif choice == 4:
        query = str(input("Please enter the DOB of the contact you want to search(in dd/mm/yy format ONLY) : "))
        for i in range(len(cb)):
            if query == cb[i][3]:
                check = i
                temp.append(cb[i])

    elif choice == 5:
        query = str(input("Please enter the category of the contact you want to search(Family/Friends/Work/Others) : "))
        for i in range(len(cb)):
            if query == cb[i][4]:
                check = i
                temp.append(cb[i])

    else:
        print("Invalid search criteria.")
        return -1
    
    if check == -1:
        return -1
    else:
        display_all(temp)
        return check
    
def display_all(cb):
    if not cb:
        print("List is empty : []")

    else:
        for i in range(len(cb)):
            print(cb[i])

def thanks():
    print("~~~Thank you for visiting. Please visit again!~~~")
    sys.exit("Goodbye, have a great day!")

print("---------------------------------------------------------------------------")
print("Hello dear user, welcome to the Smartphone Directory System.")
print("---------------------------------------------------------------------------")

ch = 1
cb = initial_contactbook()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        cb = add_contact(cb)

    elif ch == 2:
        cb = remove_existing(cb)

    elif ch == 3:
        cb = delete_all(cb)

    elif ch == 4:
        d = search_existing(cb)
        if d == -1:
            print("This contact does not exist. Please try again.")

    elif ch == 5:
        display_all(cb)

    else:
        thanks()