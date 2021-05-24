class Bank:
    location="Mombasa"
    def __init__(self,name,deposite,balance,account):
        self.name=name
        self.deposite=deposite
        self.balance=balance
        self.account=account
    def balance(self):
        return f"Hello class, my balance is {self.balance}"
    def current_balance(self):
         return f"Hello my name is {self.name} and my current balance is {500000-self.balance}"

class Account:
    def __init__(self,name,phonenumber,balance):
        self.name=name
        self.phonenumber=phonenumber
        self.balance=balance
        self.borrow=0
    def showbalance(self):
        return f"Hello, {self.name},your balance is {self.balance}"

    def deposite(self,amount):
        if amount<0:

            return f"cannot add any amount"
        else:
             self.balance +=amount
             return self.showbalance()
             
    def withdraw(self,amount):
        if amount>self.balance:
            return f"your balance is {self.balance} you cannot withdraw {amount}"
        else:
               self.balance-=amount
               return self.showbalance()
    def add_laon(self,amount):
        return f"my amount is {amount}"
    def replayloan(self,amount):
        return f"my amount is"
       



