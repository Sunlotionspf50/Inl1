class account:
    def __init__(self, accountNumber, balance):
        self._accountNumber = accountNumber
        self._balance = balance
    
    def accountAvailability(newAccount):
        with open('accounts.txt','r') as f:
            if newAccount in f.read():
                return False

    def saveAccountTofile():
        with open('accounts.txt','a') as f:
            f.write(f'{newAccount._accountNumber} {newAccount._balance}')
                

    def createAccount():
        accountAvailable = False
        while accountAvailable == False :
            try:
                newAccount = int(input('Enter your 6-digit account number> '))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
            else:
                accountAvailable = accountAvailability(newAccount)
                if accountAvailable == False:
                    print('Account already in use. Try again.')
        newAccount._accountNumber = newAccount
        newAccount._balance = 0
        saveAccountTofile()
        print(f'Account {newAccount} created successfully.')
    
    def login():
        while True:
            try:
                login = int(input('login(account number)> '))
                break
            except ValueError:
                print("Account number invalid.")
            else:
                with open('accounts.txt','r') as f:
                    if login in f.read():
                        print('login successfull. Welcome!')
                        return login
                 
    def gotoMainmenu():
        while True:
            try:
                entry = int(input('****MAIN MENU****\n1. Create account\n2. Login\n3. End session\n> '))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
        if entry == 1:
            createAccount()
        if entry == 2:
            login=login()
            gotoAccountmenu()
        if entry == 3:
            print('Session ended. Please come again.')
            break

    def getbalancefromfile(accountNumber):
        with open('accounts.txt','r') as f:
            data = f.readlines()
            for line in data:
                if line.__contains__('123456'):
                    accountInfo=line
                    balance=int(accountInfo.split(" ")[1])
                    return balance
                    
    def updateBalanceinFile(accountNumber, newBalance):
        with open ('accounts.txt','w')


                

    def gotoAccountmenu(login):
        while True:
            try:
                entry2 = int(input('****ACCOUNT MENU****\n1. Withdrawal\n2. Deposit\n3. Current balance\n4. Back to main menu\n> '))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
        if entry2 == 1:
            while True:
                try:
                    withdrawal = int(input('Amount to withdraw> '))
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
                else:
                    currentBalance = getbalancefromfile(login)

                    if currentBalance < withdrawal:
                        print('Your balance is too low.')
                    else:
                        newbalance = currentBalance - withdrawal
                        login._balance = newbalance
                        updateBalanceinFile(login._balance)

     

