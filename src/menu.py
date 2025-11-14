from account_operations import *

def menu():
    while True:
        print("\n Bank Managemnt System")
        print("1. Craete account")
        print("2. View Accounts")
        print("3. Deposit Amount")
        print("4. Withdraw Amount")
        print("5. Check Balance ")
        print("6. Exit")

        choice=input("Enter Your Choice: ")

        if choice=='1':
            create_account()
        elif choice=='2':
            view_accounts() 
        elif choice=='3':
            deposit_money()
        elif choice=='4':
            withdraw_money()
        elif choice=='5':
            check_balance()
        elif choice=='6':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")
