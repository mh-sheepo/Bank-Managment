print("Assalamualaikum!\n ")

print('X Bank Ltd.!\n ')

print("\nFor Create Account You Need To Fill This from bellow:\n ")



def Profile():
    Name = input("Full Name:")
    DOB = input("Date Of Birth:")
    Ocopation = input("Ocupation:")
    Name_Of_Company = input("Company's Name:")
    Mobile_Number = input("Phone Number:")
    Salary = input("Salary Amount:")

    print('\n')

    print("Your KYC Data:")


    print('\n')
    print("Name : ", Name)
    print("Date Of Birth : ", DOB)
    print("Ocopation : ", Ocopation)
    print("Name Of Company : ", Name_Of_Company)
    print("Mobile Number : ", Mobile_Number)
    print("Salary : ", Salary)
    print("\n")
    print("Successfully saved!")
    print('\n')


Balance = 0


def deposit():
    balance = 0
    amount = float(input("Enter amount to be Deposited: "))
    balance += amount
    print("\n Amount Deposited:", amount)
    withdraw(amount)


def withdraw(amount):
    balance = amount
    amount = float(input("Enter amount to be Withdrawn: "))
    if balance >= amount:
        balance -= amount
        print("\n You Withdrew:", amount)
    else:
        print("\n Insufficient balance  ")
    display(balance)


def display(balance):
    print("\n Net Available Balance:", balance)


Profile()
print("\n ")
deposit()
print("\n ")
print("Thanks for choosing our banking!")