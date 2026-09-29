class bankaccount:

    def __init__(self,owner,balance):
        self.owner=owner;
        self.balance=balance;

    def deposit(self,amount):
        self.balance=self.balance+amount;

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount;
        else:
            print("insufficient balance");

    def showbalance(self):
        print("your balance is ",self.balance);



account1=bankaccount("ashutosh",1000);
account1.deposit(500);
account1.withdraw(200);
account1.showbalance();