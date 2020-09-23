class Account:

	def __init__(self,accountNumber, balance):
		self.accountNumber = accountNumber
		self.balance = balance
	
	def AddAccountToFile(self):
		with open('accounts.txt','a') as f:
			f.write(f'{self.accountNumber} {self.balance}\n')
			print(f'Account {self.accountNumber} created successfully.')
	
	def GetbalanceFromfile
	
newAccount=input('desired account Number?')
newAccount = Account(newAccount, 0)
newAccount.AddAccountToFile()

	