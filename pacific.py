from colorama import *

#data base of registered users
user_bank = [
    {
        'name': 'Juan',
        'last_name': 'Lopez',
        'account_number': '12',
        'balance': 1500.00,
        'password': '12'
    },
    {
        'name': 'Maria',
        'last_name': 'Perez',
        'account_number': '13',
        'balance': 2500.00,
        'password': '5678'
    },
    {
        'name': 'Elsa',
        'last_name': 'Pato',
        'account_number': '465475445',
        'balance': 24500.00,
        'password': '7658'
    },
    {
        'name': 'Miriam',
        'last_name': 'Esquivel',
        'account_number': '458965789',
        'balance': 574544.00,
        'password': '8585'
    },
]

#beggining image using colorama
def show_message_of_bank():
    print(Fore.RED+Style.BRIGHT+("██████╗░░█████╗░░█████╗░██╗███████╗██╗░█████╗░   ░██████╗████████╗░█████╗░███╗░░██╗██████╗░░█████╗░██████╗░████████╗"))
    print(Fore.BLUE+"██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██║██╔══██╗   ██╔════╝╚══██╔══╝██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝")
    print(Fore.WHITE+"██████╔╝███████║██║░░╚═╝██║█████╗░░██║██║░░╚═╝   ╚█████╗░░░░██║░░░███████║██╔██╗██║██║░░██║███████║██████╔╝░░░██║░░░")
    print(Fore.RED+"██╔═══╝░██╔══██║██║░░██╗██║██╔══╝░░██║██║░░██╗   ░╚═══██╗░░░██║░░░██╔══██║██║╚████║██║░░██║██╔══██║██╔══██╗░░░██║░░░")
    print(Fore.BLUE+"██║░░░░░██║░░██║╚█████╔╝██║██║░░░░░██║╚█████╔╝   ██████╔╝░░░██║░░░██║░░██║██║░╚███║██████╔╝██║░░██║██║░░██║░░░██║░░░")
    print(Fore.WHITE+"╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝╚═╝░░░░░╚═╝░╚════╝░   ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░")
    print()
    print(Style.RESET_ALL)

#definitive login menu
def show_login_menu1():
    show_message_of_bank()
    print(Fore.CYAN+Style.BRIGHT+"Welcome to the banking system")
    print(Fore.WHITE+Style.BRIGHT+"1. Log in")
    print(Fore.WHITE+Style.BRIGHT+"2. Register")
    print(Fore.WHITE+Style.BRIGHT+"3. Exit")
    print(Style.RESET_ALL)

#login
def login():
    for tries in range(3):
        print()
        print (Fore.YELLOW+Style.BRIGHT+"Type your account number: ", end=Fore.GREEN+Style.BRIGHT+"")
        account_number = input()
        print()
        print (Fore.YELLOW+Style.BRIGHT+"Type your password: ", end=Fore.GREEN+Style.BRIGHT+"")
        password = input()
        print(Style.RESET_ALL)

        for user in user_bank:
            if user['account_number'] == account_number and user['password'] == password:
                print(Fore.GREEN+Style.BRIGHT+"░██╗░░░░░░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗    ░░██╗██████╗░")
                print(Fore.GREEN+Style.BRIGHT+"░██║░░██╗░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝    ░██╔╝╚════██╗")
                print(Fore.GREEN+Style.BRIGHT+"░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░    ██╔╝░░█████╔╝")
                print(Fore.GREEN+Style.BRIGHT+"░░████╔═████║░██╔══╝░░██║░░░░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░    ╚██╗░░╚═══██╗")
                print(Fore.GREEN+Style.BRIGHT+"░░╚██╔╝░╚██╔╝░███████╗███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗    ░╚██╗██████╔╝")
                print(Fore.GREEN+Style.BRIGHT+"░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝    ░░╚═╝╚═════╝░")
                print(Fore.GREEN+Style.BRIGHT+"Login successful")
                print(Style.RESET_ALL)
                return user #returns the user in case of a login succesful
        print(Fore.RED+Style.BRIGHT+"░██╗░░░░░░░██╗░█████╗░██████╗░███╗░░██╗██╗███╗░░██╗░██████╗░    ██╗██╗░░██╗")
        print(Fore.RED+Style.BRIGHT+"░██║░░██╗░░██║██╔══██╗██╔══██╗████╗░██║██║████╗░██║██╔════╝░    ╚═╝╚█║░██╔╝")
        print(Fore.RED+Style.BRIGHT+"░╚██╗████╗██╔╝███████║██████╔╝██╔██╗██║██║██╔██╗██║██║░░██╗░    ░░░░╚╝██╔╝░")
        print(Fore.RED+Style.BRIGHT+"░░████╔═████║░██╔══██║██╔══██╗██║╚████║██║██║╚████║██║░░╚██╗    ░░░░░░╚██╗░")
        print(Fore.RED+Style.BRIGHT+"░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║██║░╚███║██║██║░╚███║╚██████╔╝    ██╗░░░░╚██╗")
        print(Fore.RED+Style.BRIGHT+"░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░╚══╝░╚═════╝░    ╚═╝░░░░░╚═╝")
        print(Fore.RED+Style.BRIGHT+"Incorrect account number or password, PRESS ENTER TO TRY AGAIN OR TYPE 1 TO GO BACK TO THE MAIN MENU")
        print(Fore.RED+Style.BRIGHT+"You'll only have 3 attemps")
        print()

        wrong_login=input()
        if wrong_login=='1':
            return False
    print(Style.RESET_ALL)
    print(Fore.RED + Style.BRIGHT + "You have exceeded the maximum number of login attempts.")
    print(Style.RESET_ALL)
    
    #return False
   
#register users 
def register_user():
    print()
    print(Fore.YELLOW + Style.BRIGHT + "Type your user's name: ", end=Fore.GREEN + Style.BRIGHT +"")
    name = input()
    print()
    print(Fore.YELLOW + Style.BRIGHT + "Enter user's last name: ", end=Fore.GREEN+Style.BRIGHT+"")
    last_name = input()
    print()
    while True:
        print(Fore.YELLOW + Style.BRIGHT + "ENTER USER'S ACCOUNT NUMBER")
        print(Fore.YELLOW + Style.BRIGHT + "Account number must be at least 5 digits and contain only numbers :", end=Fore.GREEN+Style.BRIGHT+"")
        account_number = input()
        if any(user['account_number']== account_number for user in user_bank):
            print(Fore.RED + Style.BRIGHT + "This account number is already in use. Please try another.")
            print()
            continue
        #the account number must be only number
        if not account_number.isdigit() or len(account_number) < 5:
            print(Fore.RED + Style.BRIGHT + "Account number must be at least 5 digits and contain only numbers.")
        else:
            break
    print()
    while True:
        print(Fore.YELLOW + Style.BRIGHT + "Enter user's account password ")
        print(Fore.YELLOW + Style.BRIGHT + "Password must be at least 8 characters long:", end=Fore.GREEN+Style.BRIGHT+"")

        password = input()
        if len(password) >= 8:
            break
        else:
            print("Password must be at least 8 characters long.")
            print()
    while True:
        print()
        print(Fore.YELLOW + Style.BRIGHT + "Enter user's initial balance: ", end=Fore.GREEN+Style.BRIGHT+"")
        #avoid the user enter numbers in letters
        try:
            balance = float(input())
            if balance <= 0:  
                    raise ValueError("The amount must be greater than 0.")
            else:
                break
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Initial balance must be a number.")
            print()
    print(Style.RESET_ALL)
    print()
    new_user = {
        'name': name,
        'last_name': last_name,
        'account_number': account_number,
        'balance': balance,
        'password': password
    }
    user_bank.append(new_user)
    print(Fore.GREEN+Style.BRIGHT+"User successfully registered")
    print(Style.RESET_ALL)
   
#actions menu 
def actions_menu():
    print('---------------------------------')
    print()
    print(Fore.CYAN+Style.BRIGHT+"YOU CAN PERFORME THE NEXT ACTIONS")
    print(Fore.CYAN+Style.BRIGHT+"* Type only the number *")
    print(Style.RESET_ALL)
    print(Fore.WHITE+Style.BRIGHT+"1. Check balance")
    print(Fore.WHITE+Style.BRIGHT+"2. Deposit to other accounts")
    print(Fore.WHITE+Style.BRIGHT+"3. Withdraw money")
    print(Fore.WHITE+Style.BRIGHT+"4. Exit")
    print(Style.RESET_ALL)

#check balance 
def check_balance(user):
    print('---------------------------------')
    print()
    print(Fore.YELLOW + Style.BRIGHT + f"Account Number: {Fore.GREEN + Style.BRIGHT + user['account_number']}")
    print(Fore.YELLOW + Style.BRIGHT + f"Balance: {Fore.GREEN + Style.BRIGHT + str(user['balance'])}")
    print(Style.RESET_ALL)

#deposit to other accounts 
def deposit_to_account(user):
    while True:
        while True:
            print(Fore.YELLOW + Style.BRIGHT + "Enter recipient's account number: ", end=Fore.GREEN + Style.BRIGHT + "")
            recipient_account_number = input()
            if not recipient_account_number.isdigit():
                print(Fore.RED + Style.BRIGHT + "Account number must be only numbers.")
                print()
            else:
                break
        print()
        while True:
            print(Fore.YELLOW + Style.BRIGHT + "Enter amount to deposit: ", end=Fore.GREEN + Style.BRIGHT + "")
            try:
                amount = float(input())
                if amount <= 0:  
                    raise ValueError("The amount must be greater than 0.")
                else:
                    if user['balance'] < amount:
                        print(Fore.RED + Style.BRIGHT + "Insufficient funds for this transaction.")
                        print(Fore.RED+Style.BRIGHT+"██╗███╗░░██╗░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░░░███████╗████████╗███████╗")
                        print(Fore.RED+Style.BRIGHT+"██║████╗░██║██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██╔════╝")
                        print(Fore.RED+Style.BRIGHT+"██║██╔██╗██║██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░░░░██║░░░█████╗░░")
                        print(Fore.RED+Style.BRIGHT+"██║██║╚████║██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░")
                        print(Fore.RED+Style.BRIGHT+"██║██║░╚███║╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░███████╗███████╗░░░██║░░░███████╗")
                        print(Fore.RED+Style.BRIGHT+"╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝░░░╚═╝░░░╚══════╝")
                        print(Style.RESET_ALL)
                        print(Fore.RED+Style.BRIGHT+"PRESS ENTER TO CONTINUE")
                    else:
                        break
            except ValueError:
                print(Fore.RED + Style.BRIGHT + "Amount must be a number.")
                print()
                continue
            
        # Pedir contraseña para confirmación
        print()
        for tries in range(3):
            print(Fore.YELLOW + Style.BRIGHT + "Enter your password for verification: ", end=Fore.GREEN + Style.BRIGHT + "")
            password = input()
            if password != user['password']:
                print(Fore.RED+Style.BRIGHT+"██╗███╗░░██╗░█████╗░░█████╗░██████╗░██████╗░███████╗░█████╗░████████╗   ██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░")
                print(Fore.RED+Style.BRIGHT+"██║████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝   ██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗")
                print(Fore.RED+Style.BRIGHT+"██║██╔██╗██║██║░░╚═╝██║░░██║██████╔╝██████╔╝█████╗░░██║░░╚═╝░░░██║░░░   ██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║")
                print(Fore.RED+Style.BRIGHT+"██║██║╚████║██║░░██╗██║░░██║██╔══██╗██╔══██╗██╔══╝░░██║░░██╗░░░██║░░░   ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║")
                print(Fore.RED+Style.BRIGHT+"██║██║░╚███║╚█████╔╝╚█████╔╝██║░░██║██║░░██║███████╗╚█████╔╝░░░██║░░░   ██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝")
                print(Fore.RED+Style.BRIGHT+"╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░░░░╚═╝░░░   ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░")
                print(Style.RESET_ALL)
                print(Fore.RED+Style.BRIGHT+"Incorrect account number or password, PRESS ENTER TO TRY AGAIN OR TYPE 1 TO GO BACK TO THE MAIN MENU")
                print(Fore.RED+Style.BRIGHT+"You'll only have 3 attemps")
                print(Style.RESET_ALL)
                wrong_login=input()
                if wrong_login=='1':
                    print()
                    break
                else:
                    continue

            recipient_found = False
            for recipient in user_bank:
                if recipient['account_number'] == recipient_account_number:
                    recipient_found = True
                    recipient['balance'] += amount
                    print(Fore.GREEN+Style.BRIGHT+"░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░░░███████╗████████╗███████╗")
                    print(Fore.GREEN+Style.BRIGHT+"██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██╔════╝")
                    print(Fore.GREEN+Style.BRIGHT+"██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░░░░██║░░░█████╗░░")
                    print(Fore.GREEN+Style.BRIGHT+"██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░")
                    print(Fore.GREEN+Style.BRIGHT+"╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░███████╗███████╗░░░██║░░░███████╗")
                    print(Fore.GREEN+Style.BRIGHT+" ╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝░░░╚═╝░░░╚══════╝")
                    print(Style.RESET_ALL)
                    user['balance'] -= amount  # Restar el monto del saldo del remitente
                    print(Fore.GREEN + Style.BRIGHT + "Deposit successful. Your new balance is: $" + str(user['balance']))
                    break  # Salir del bucle una vez que el depósito ha sido realizado
            if not recipient_found:
                print(Fore.RED + Style.BRIGHT + "Recipient account not found.")
                print()
                print(Fore.RED+Style.BRIGHT+"██╗███╗░░██╗░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░░░███████╗████████╗███████╗")
                print(Fore.RED+Style.BRIGHT+"██║████╗░██║██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██╔════╝")
                print(Fore.RED+Style.BRIGHT+"██║██╔██╗██║██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░░░░██║░░░█████╗░░")
                print(Fore.RED+Style.BRIGHT+"██║██║╚████║██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░")
                print(Fore.RED+Style.BRIGHT+"██║██║░╚███║╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░███████╗███████╗░░░██║░░░███████╗")
                print(Fore.RED+Style.BRIGHT+"╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝░░░╚═╝░░░╚══════╝")
                print(Style.RESET_ALL)
                print(Fore.RED+Style.BRIGHT+"PRESS ENTER TO CONTINUE")
                wrong_amount=input()
                break
            return True
        print(Style.RESET_ALL)
        print(Fore.RED + Style.BRIGHT + "You have exceeded the maximum number of attempts.")
        print(Style.RESET_ALL)
        return False

#withdraw money 
def withdraw_from_account(user):
    while True:
        print(Fore.YELLOW + Style.BRIGHT + "Enter amount to withdraw: ", end=Fore.GREEN + Style.BRIGHT + "")
        try:
            amount = float(input())
            if amount <= 0:  
                    raise ValueError("The amount must be greater than 0.")
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Initial balance must be a number.")
            continue

        # ask password for confirmation 
        print(Fore.YELLOW + Style.BRIGHT + "Enter your password for verification: ", end=Fore.GREEN + Style.BRIGHT + "")
        password = input()
        if password != user['password']:
            print()
            print(Fore.RED + Style.BRIGHT + "Incorrect password")
            print(Fore.RED+Style.BRIGHT+"██╗███╗░░██╗░█████╗░░█████╗░██████╗░██████╗░███████╗░█████╗░████████╗   ██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░")
            print(Fore.RED+Style.BRIGHT+"██║████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝   ██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗")
            print(Fore.RED+Style.BRIGHT+"██║██╔██╗██║██║░░╚═╝██║░░██║██████╔╝██████╔╝█████╗░░██║░░╚═╝░░░██║░░░   ██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║")
            print(Fore.RED+Style.BRIGHT+"██║██║╚████║██║░░██╗██║░░██║██╔══██╗██╔══██╗██╔══╝░░██║░░██╗░░░██║░░░   ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║")
            print(Fore.RED+Style.BRIGHT+"██║██║░╚███║╚█████╔╝╚█████╔╝██║░░██║██║░░██║███████╗╚█████╔╝░░░██║░░░   ██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝")
            print(Fore.RED+Style.BRIGHT+"╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░░░░╚═╝░░░   ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░")
            print(Style.RESET_ALL)
            print(Fore.RED+Style.BRIGHT+"PRESS ENTER TO CONTINUE")
            wrong_amount=input()
            if wrong_amount=='1':
                return  # get out of the function if is incorrect

        if user['balance'] >= amount:
            user['balance'] -= amount
            print(Fore.GREEN + Style.BRIGHT + "Withdrawal successful. Your new balance is: $"+ str(user['balance']))
            print()
            print(Fore.GREEN+Style.BRIGHT+"░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░░░███████╗████████╗███████╗")
            print(Fore.GREEN+Style.BRIGHT+"██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██╔════╝")
            print(Fore.GREEN+Style.BRIGHT+"██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░░░░██║░░░█████╗░░")
            print(Fore.GREEN+Style.BRIGHT+"██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░")
            print(Fore.GREEN+Style.BRIGHT+"╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░███████╗███████╗░░░██║░░░███████╗")
            print(Fore.GREEN+Style.BRIGHT+" ╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝░░░╚═╝░░░╚══════╝")
            print(Style.RESET_ALL)
            break # get out of the function with the complete withdrawal
        else:
            print(Fore.RED + Style.BRIGHT + "Insufficient funds")
            print(Fore.RED+Style.BRIGHT+"██╗███╗░░██╗░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░░░███████╗████████╗███████╗")
            print(Fore.RED+Style.BRIGHT+"██║████╗░██║██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██╔════╝")
            print(Fore.RED+Style.BRIGHT+"██║██╔██╗██║██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░░░░██║░░░█████╗░░")
            print(Fore.RED+Style.BRIGHT+"██║██║╚████║██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░")
            print(Fore.RED+Style.BRIGHT+"██║██║░╚███║╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░███████╗███████╗░░░██║░░░███████╗")
            print(Fore.RED+Style.BRIGHT+"╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝░░░╚═╝░░░╚══════╝")
            print(Style.RESET_ALL)
            print(Fore.RED+Style.BRIGHT+"PRESS ENTER TO CONTINUE")
            wrong_amount=input()
            return # get out of the function if there aren't enough funds

#main.2, this main call the options menu
def main_2(user):
    while True:
        actions_menu()
        option = input(Fore.YELLOW + Style.BRIGHT + "Choose the action to execute: " + Fore.GREEN + Style.BRIGHT)
        print(Style.RESET_ALL)  # Restablece el estilo al default después de la entrada

        if option == "1" or option=='Check balance' or option=='check balance':
            # Llama a la función para chequear el balance del usuario logueado
            check_balance(user)
        elif option == "2" or option=='Deposit' or option=='deposit':
            # Invoca la función para realizar un depósito a otra cuenta. La verificación de contraseña es interna.
            deposit_to_account(user)
        elif option == "3" or option=='Withdraw' or option=='withdraw':
            # Permite al usuario retirar dinero de su cuenta, incluyendo la verificación de contraseña dentro de la función.
            withdraw_from_account(user)
        elif option == "4" or option=='Exit' or option=='exit':
            print(Fore.RED + Style.BRIGHT + "Exiting the system. Goodbye!")
            print(Style.RESET_ALL)  # Asegura que el estilo se resetea después de la salida
            break  # Sale del bucle y termina la sesión
        else:
            print(Fore.RED + Style.BRIGHT + "Invalid option, please type a correct number.")
            print(Style.RESET_ALL)  # Restablece el estilo tras mostrar el mensaje de opción inválida

#main with the options to execute, while true...
def main():
   while True:
        show_login_menu1()
        print(Fore.YELLOW+Style.BRIGHT+"Choose the action to execute: ", end=Fore.GREEN+Style.BRIGHT+"")
        option = input()
        if option == "1" or option=='Login' or option=='login':
            user = login()
            if user:
                main_2(user)
        elif option == "2" or option=='Register' or option=='register':
            if register_user():
                print(Fore.GREEN+Style.BRIGHT+"User successfully registered. Please log in.")
        elif option == "3" or option=='Exit' or option=='exit':
            print(Fore.RED+Style.BRIGHT+"Getting out...")
            return False
        else:
            print(Fore.RED+Style.BRIGHT+"Invalid option please type a correct number")
            print(Style.RESET_ALL)

#this main starts all the code        
main()