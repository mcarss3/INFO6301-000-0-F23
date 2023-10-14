#Final Project "BankAccount" by Mike Carss for Tech6301 001 0 F3

    #1.	Create class BankAccount.
class BankAccount(object):
    
    #Needed for a unique number to persist between BankAccount calls
    totalAccounts=0

    #2. The constructor arguments should be named (username), accountType (checking 
    #   or saving), and balance (zero by default).
    def __init__(self, name, accountType, balance = 0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        
    #   Adds to the total accounts created so the account number is unique      
        BankAccount.totalAccounts+=1
        
    #   Generate a "unique" account with some purely decorative leading zeros, a unique 
    #   number and the first intial of the name, plus some more decoration
        self.accountNumber = str("0000-"+str(BankAccount.totalAccounts)+name[0]+"-00"+str(BankAccount.totalAccounts))
 
    #3. Generate an ID for the new account and create a new file containing all user 
    #   transactions. The specified file naming format requires including the user's 
    #   name, account type, and user ID. Following this naming format:
        self.filename=str(self.accountNumber)+"_"+self.accountType+"_"+self.name+".txt"
        
    #4. Function for depositing money into acct. Transaction stored in statement file.
    #   (Negative numbers probably shouldn't be allowed here)
    def deposit(self, transaction):
        if transaction > 0:
            self.balance += transaction
            self.commitTransaction("+"+str(transaction)+"\n")
    
    #   Reusable function to write transactions
    def commitTransaction(self, transaction):
        f=open(self.filename, 'a')
        f.write(transaction)

    #5. Function for withdrawing money from acct. Transaction stored in statement file.
    #   Balance can't go below 0
    def withdraw(self, transaction):
        if transaction > 0 and transaction <= self.balance:
            self.balance -= transaction
            self.commitTransaction("-"+str(transaction)+"\n")
    
    #6. Function for gettng acct balance
    def checkBalance(self):
        return self.balance
    
    #7.A Function for retrieving user ID (I Guess this means accountNumber?)
    def checkAccountNumber(self):
        return self.accountNumber
    
    #7.B Function for retrieving username (I guess this means name?)
    def checkUser(self):
        return self.name
    
    #7.C Function for retrieving account type 
    def checkAccountType(self):
        return self.accountType
    
    #8 Function to retrieve transaction history from statement file.
    def checkTransactions(self):
        
        transactions=[]
        
        f=open(self.filename, 'r')
        transactions=f.readlines()
        
        return transactions
    
    #9 Create multiple objects and apply different transactions
 
    
    #  Create some accounts to interact with
account1 = BankAccount("Mike", "Savings", )
account2 = BankAccount("Sarah", "Checking")
account3 = BankAccount("Ashley", "Savings")


    #  Create some transactions for those accounts
account1.deposit(500000)
account1.withdraw(10000)
account2.deposit(100)
account3.deposit(5)

    #  This should not work
account2.withdraw(2069)


    #  Grab some transaction info
transactions1= account1.checkTransactions()
transactions2= account2.checkTransactions()
transactions3= account3.checkTransactions()
    
    #output the account info to test
print("UserID:" +account1.checkAccountNumber())
print("Name:" +account1.checkUser())
print("Balance:" +str(account1.checkBalance()))

print("UserID:" +account2.checkAccountNumber())
print("Name:" +account2.checkUser())
print("Balance:" +str(account2.checkBalance()))

print("UserID:" +account3.checkAccountNumber())
print("Name:" +account3.checkUser())
print("Balance:" +str(account3.checkBalance()))

    #output the transactions to test
print("Account1 Transactions:")
for x in transactions1:
    print(x.strip())
    
print("Account2 Transactions:")
for x in transactions2:
    print(x.strip())
    
print("Account3 Transactions:")
for x in transactions3:
    print(x.strip())

  


