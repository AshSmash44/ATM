accoutNum = input("please input your account number: ")
password = input("please enter your password: ")

class atm:
    def __init__(self,accountNum,password,money):
        self.accountNum = accountNum
        self.password = password
        self.money = money
    def amount(self,money):
        return self.money
    def withdraw(self):
        print("all money withdrawn brrrrrrrrr [ERROR COULD NOT PRINT MONEY] there you go!")
