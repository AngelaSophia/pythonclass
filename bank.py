from datetime import  datetime
# class Bank:
#     location="Mombasa"
#     def __init__(self,name,deposit,balance,account):
#         self.name=name
#         self.deposite=deposit
#         self.balance=balance
#         self.account=account
#         self.statement=[]

#     def balance(self):
#         return f"Hello class, my balance is {self.balance}"
#     def current_balance(self):
#          return f"Hello my name is {self.name} and my current balance is {500000-self.balance}"

class Account:
    def __init__(self,name,phonenumber):
        self.name=name
        self.phonenumber=phonenumber
        self.balance=0
        self.borrow=0
        self.statement=[]
        self.loan=0
    def showbalance(self):
        return f"Hello, {self.name},your balance is {self.balance}"

    def deposit(self,amount):
        try:
            10 + amount
        except TypeError:
                return f"The amount must be in figures"
        if amount<0:

            return f"cannot add any amount"
        else:
             self.balance +=amount
             now=datetime.now()
             transaction={
                 "amount":amount,
                 "time":now,
                 "narration":"you deposited"
             }
             self.statement.append(transaction)
             return self.showbalance()
    # def show_statement(self):
    #          return self.statement
             
    def withdraw(self,amount):
        try:
            50 - amount
        except TypeError:
                return f"the amount must be in figures"
        if amount>self.balance:
            return f"your balance is {self.balance} you cannot withdraw {amount}"
        else:
               self.balance-=amount
               now=datetime.now()
               transaction={
                 "amount":amount,
                 "time":now,
                 "narration":"you withdrew"
             }
               self.statement.append(transaction)
               return self.showbalance()
    def add_laon(self,amount):
        return f"my amount is {amount}"
    def repayloan(self,amount):
        return f"my amount is"
       
    def show_statement(self):
        for transaction in self.statement:
            amount=transaction["amount"]
            narration=transaction["narration"]
            time=transaction["time"]
            date=time.strftime("%d/%m/%y")
            print(f"{date} : {narration} {amount}")

    def borrow(self,amount):
        try:
            40 + amount
        except TypeError:
            return f"the amount must be in figures"
        if amount < 0:
            return "no amount given"
        elif self.loan > 0:
            return "you have an excisting loan"
        elif amount <0.1* self.balance:
            return "you did not qualify"
        
        else: 
            loan=amount*1.05
            self.loan=loan
            self.balance += amount
            now=datetime.now()
            borrow_transaction={
                "amount":amount,
                "time":now,
                "narration":"you borrowed"
             }
            self.statement.append(borrow_transaction)
            return self.showbalance()
        

    def repay (self,amount):
        try:
            10 + amount
        except TypeError:
                return f"the amount must be in figures"
        if amount <0:
            return f"you can not take another loan{self.loan}"
        elif amount < self.loan:
            self.loan-=amount
            return f"you can take loan {self.loan}"
        else:
            diff=amount-self.loan
            self.loan=0
            self.deposit(diff)
            now=datetime.now()
            repay_transaction={
                 "amount":amount,
                 "time":now,
                 "narration":"you withdrew"
             }
            self.statement.append(repay_transaction)
            return self.showbalance()
    def show_statement(self):
        for transaction in self.statement:
            amount=transaction["amount"]
            narration=transaction["narration"]
            time=transaction["time"]
            date=time.strftime("%d/%m/%y")
            print(f"{date} : {narration} {amount}")      

    def transfer(self,account,amount):
        try:
            10 + amount
        except TypeError:
            return f"the a mount must be in figures"
        # if  amount >0:
        #     return "the money should be transfered"
        fee = amount*0.05
        total=amount + fee
        if total> self.balance:
            return f"your balance is {self.balance} and you need at least {total} for this transfer"
        else:
            self.balance -= total
            account.deposit(amount)
            return f"you have transfered the money to another account"

class Mobile_Money_Account(Account):
    def __init__(self,name,phonenumber,service_provider):
        Account. __init__(self,name,phonenumber)
        self.service_provider=service_provider
    def buy_airtime(self,amount):
        try:
            10 + amount
        except TypeError:
            return f"you have bought airtime"
        if amount >0:
            return f" {self.name}your amount {amount} is too low"
        elif self.balance < amount:
            return f"your {self.balance} is not surficient to buy airtime"
        else:
                self.balance-=amount
                return f"you have bought airtime of {amount},your new balance is {self.balance}"

           
            
# Syntax Error and Excemptions this is the wrong syntax //use of try catch method

        



            

            


