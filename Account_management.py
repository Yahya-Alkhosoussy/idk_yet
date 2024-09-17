import Utility as u



def create_account():

    first_name = input("What is your first name: ")

    last_name = input("What is your last name: ")

    age = int(input("What is your age: "))

    password = input("What would you like your password to be? \n")

    done = False

    while done != True:

        try:

            account_type = int(input("Input 1 for Credit Account and 2 for Debit Account: \n"))

            done = True

        except ValueError:

            print("Invalid input, please type a number!")

    u.make_account(first_name=first_name, last_name=last_name, age=age, password=password, Account_type=account_type)