import datetime
open('accounts.txt','r')
open('balances.txt','r')
open('transactions.txt','r')


def getAccountslist():  #Get account list from file into a readable list.
    with open('accounts.txt', 'r') as f1:
        accountFile=f1.read()
        accountList=accountFile.split('\n')
        return accountList

def saveAccountslist(accountsList): #Save new account list from program into file by adding a newline between every account.
    with open('accounts.txt', 'w') as f2:
        f2.write('\n'.join(accountsList))


def getBalanceslist():  #Get balances list from file into a readable list.
    with open('balances.txt', 'r') as f3:
        balancesFile=f3.read()
        balancesList=balancesFile.split('\n')
        return balancesList
        
def saveBalanceslist(balancesList): #Save new account list from program into file by adding a newline between every balance.
    with open('balances.txt', 'w') as f4:
        f4.write('\n'.join(balancesList))

def loggWithdrawal(account,amount):
    with open('transactions.txt', 'a') as f5:
        timeNow=datetime.datetime.now()
        f5.write(f'{timeNow} > account = {account} > withdrawal > {amount} kr\n')    

def loggDeposit(account,amount):
    with open ('transactions.txt', 'a') as f5:
        timeNow=datetime.datetime.now()
        f5.write(f'{timeNow} > account = {account} > deposit > {amount} kr\n')
      
accountsList=getAccountslist()  #Reading account list from file into program.
balancesList=getBalanceslist()  #Reading balance list from file into program.

num1 = 'none'
while num1 != 3:    #While-loop to get back to main menu.
    print('****HUVUDMENY****\n1. Skapa konto\n2. Administrera konto\n3. Avsluta\nAnge menyval>')
    num1 = input()
    while num1.isnumeric() != True:
        print('Integers only.')
        num1 = input()
    num1 = int(num1) 
    if num1 == 1:
        newAccount=None
        newAccount=input('Ange kontonummer> ')
        while newAccount.isnumeric() != True:
            print('Integers only.') 
            newAccount = input()
        if accountsList == ['']:            #If-statement necessary to put the first account in index 0 in the list.
            accountsList[0] = newAccount
            balancesList[0] = str(0)
            saveAccountslist(accountsList)  #Saving new account list into file.
            saveBalanceslist(balancesList)  #Saving new balances list into file.
        else:
            while newAccount in accountsList:     #While-loop to check if the account already exists.
                print('Kontonummer finns redan, försök igen.')
                newAccount=input('Ange kontonummer>')
            accountsList += [newAccount]
            balancesList += str(0)
            saveAccountslist(accountsList)  #Saving new account list into file.
            saveBalanceslist(balancesList)  #Saving new balances list into file.
            print(f'Ditt kontonummer är {newAccount}.')
    if num1 == 2:
        login = input('login(kontonummer)>')
        while login not in accountsList and login.isnumeric() != True:
            print('Konto finns inte. Försök igen.')
        print('OK')
        accountIndex = accountsList.index(login)
        num2 = 'none'
        while num2 != 4:
            print('****KONTOMENY****\n1. Ta ut pengar\n2. Sätt in pengar\n3. Visa saldo\n4. Avsluta')
            num2 = input()
            while num2.isnumeric() != true:
                print('Integers only.')
                num2 = input()
            num2=int(num2)
            if num2 == 1:
                withdrawal = int(input('Ange belopp du vill ta ut>'))
                balance = int(balancesList[accountIndex])
                if withdrawal > balance:
                    print('Du kan inte ta ut så mycket.')
                else:
                    balancesList[accountIndex] = str(balance-withdrawal)
                    saveBalanceslist(balancesList)
                    loggWithdrawal(login,withdrawal)
                    print('Uttag klart.')
            elif num2 == 2:
                deposit = int(input('Ange belopp du vill sätta in>'))
                balance = int(balancesList[accountIndex])
                balancesList[accountIndex] = str(balance+deposit)
                saveBalanceslist(balancesList)
                loggDeposit(login,deposit)
                print('Insättning klar.')
            elif num2 == 3:
                print(f'Ditt saldo är: {balancesList[accountIndex]} kr')
            elif num2 == 4:
                print('utloggad.')
    if num1 == 3:
        print('session avslutad.')


                    
                        
            
                
                

      
