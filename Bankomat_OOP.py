import datetime

class Account:

    def __init__(self,accountNumber, balance):
        self._accountNumber = accountNumber
        self._balance = balance

    def AddAccountToFile(self):
        with open('accounts.txt','a') as f:
            f.write(f'{self._accountNumber} {self._balance}\n')
            print(f'Account {self._accountNumber} created successfully.') 
            
    def accountAvailability(self):
        with open('accounts.txt','r') as f:
            if self._accountNumber in f.read():
                return False

    def getBalancefromFile(self):
        with open('accounts.txt','r') as f:
            data = f.readlines()
            for line in data:
                if line.__contains__(self._accountNumber):
                    accountInfo=line
                    balance=int(accountInfo.split(" ")[1])
                    return balance
    
    def updateBalanceinFile(self):
        with open('accounts.txt','r') as f:
            data = f.read()
            data = data.replace (f'{self._accountNumber} {self.getBalancefromFile()}', f'{self._accountNumber} {self._balance}')
            with open('accounts.txt','w') as f:
                f.write(data)
    
    def loggTransaction(self, type, amount):
        if type == 'deposit':
            with open('transactions.txt','a') as f:
                timeNow = datetime.datetime.now()
                f.write(f'{timeNow.strftime("%c")} > account = {self._accountNumber} > deposit > {amount} kr\n')
        elif type == 'withdrawal':
                with open('transactions.txt','a') as f:
                    timeNow = datetime.datetime.now()
                    f.write(f'{timeNow.strftime("%c")} > account = {self._accountNumber} > withdrawal > {amount} kr\n')

    def withdraw(self, amount):
        if self._balance < amount:
            print('Your balance is too low.')
        else:
            self._balance = self._balance - int(amount)
            self.updateBalanceinFile()
            self.loggTransaction('withdrawal', amount)
            print('Withdrawal complete.')

    def deposit(self, amount):
        self._balance = self._balance + int(amount)
        self.updateBalanceinFile()
        self.loggTransaction('deposit', amount)
        print('Deposit complete.')

    def gotoAccountmenu(self):
        while True:
            while True:
                try:
                    entry2 = int(input('****ACCOUNT MENU****\n1. Withdrawal\n2. Deposit\n3. Current balance\n4. Back to main menu\n> '))
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
            if entry2 == 1:
                while True:
                    try:
                        self.withdraw(int(input('Amount to withdraw> ')))
                        break
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")
            if entry2 == 2:
                while True:
                    try:
                        self.deposit(input('Amount to deposit> '))
                        break
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")
            if entry2 == 3:
                    print(f'Your balance is: {self._balance} SEK')
            if entry2 == 4:
                break

def registerAccount():
    accountAvailable = False
    sixdigits = False
    while accountAvailable == False or sixdigits == False:
        desiredAccount = 100000
        while True:
                try:
                    desiredAccount = input('Enter your 6-digit account number> ')
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
        newAccount = Account(desiredAccount, 0)
        accountAvailable = newAccount.accountAvailability() 
        if int(desiredAccount) > 99999 or int(desiredAccount) < 999999:
            sixdigits = True
        if newAccount.accountAvailability() == False:
             print('Account number already in use. Try again.')
             del newAccount
    newAccount.AddAccountToFile()

def gotoMainmenu():
    while True:
        while True:
            try:
                entry = int(input('****MAIN MENU****\n1. Create account\n2. Login\n3. End session\n> '))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
        if entry == 1:
            registerAccount()
        if entry == 2:
            entranceUnlocked = False
            while entranceUnlocked == False:
                while True:
                    try:
                        login = input('login(account number)> ')
                        break
                    except ValueError:
                        print("Account number invalid.")
                with open('accounts.txt','r') as f:
                    if login in f.read():
                        entranceUnlocked = True
                        print('login successfull. Welcome!')
            currentAccount = Account(login, 0)
            currentAccount._balance = currentAccount.getBalancefromFile()
            currentAccount.gotoAccountmenu()
        if entry == 3:
            print('Session ended. Please come again.')
            break

gotoMainmenu()