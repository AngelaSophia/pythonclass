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


