def getbalancefromfile(accountNumber):
    with open('accounts.txt','r') as f:
        data = f.readlines()
        for line in data:
            if line.__contains__(str(accountNumber)):
                accountInfo=line
                balance=int(accountInfo.split(" ")[1])
                return balance
                    
def updateBalanceinFile(accountNumber, newBalance):
    with open('accounts.txt','r') as f:
        data = f.read()
        data = data.replace (f'{accountNumber} {oldBalance}', f'{accountNumber} {newBalance}')
        with open('accounts.txt','w') as f:
            f.write(data)