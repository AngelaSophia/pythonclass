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
    def showbalance(self):
        return f"Hello, {self.name},your balance is {self.balance}"

    def deposit(self,amount):
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
    def replayloan(self,amount):
        return f"my amount is"
       
    def show_statement(self):
        for transaction in self.statement:
            amount=transaction["amount"]
            narration=transaction["narration"]
            time=transaction["time"]
            date=time.strftime("%d/%m/%y")
            print(f"{date} : {narration} {amount}")
            


