import unittest

class PseudoBank:
    # replace this with real bank API
    def __init__(self, Account):
        self.Account = Account
        self.account = dict()
    def checkPinValid(self, cardNum, pin):
        # for now, returns always true
        return True
    def getBalance(self, cardNum):
        if cardNum not in self.account:
            return False 
        return self.account[cardNum].getBalance()
    def doDeposit(self, cardNum, money):
        if cardNum not in self.account:
            return False 
        self.account[cardNum].doDeposit(money) 

    def doWidthdraw(self, cardNum, money):
        if cardNum not in self.account:
            return False
        self.account[cardNum].doWidthdraw(money)
    def addAccount(self, cardNum, pin):
        self.account[cardNum] = self.Account(cardNum, pin)
        
class PseudoAccount:
    def __init__(self, cardNum, pin):
        self.cardNum = cardNum 
        self.pin = pin
        self.balance = 0
    def getBalance(self):
        return self.balance
    def doDeposit(self, money):
        self.balance += money 
    def doWidthdraw(self, money):
        if money > self.balance:
            return False
        self.balance -= money
        return True 
        
# Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw
class ATMController:
    def __init__(self, Bank):
        self.bank = Bank
        self.cardNum = -1
    def insertCard(self, cardNum):
        self.cardNum = cardNum
    def checkPinValid(self, pin):
        if self.cardNum < 0:
            return False
        return self.bank.checkPinValid(self.cardNum, pin)
    def seeBalance(self):
       return self.bank.getBalance(self.cardNum)
    def doDeposit(self, money):
        self.bank.doDeposit(self.cardNum, money)
    def doWidthdraw(self, money):
        return self.bank.doWidthdraw(self.cardNum, money)


class TestController(unittest.TestCase):
    def test1(self):
        b = PseudoBank(PseudoAccount)
        c1 = "1234"
        p1 = "1234"
        b.addAccount(c1, p1)

        controller = ATMController(b)
        controller.insertCard(c1)
        self.assertEqual(controller.seeBalance(), 0)
        controller.doDeposit(10000)
        self.assertEqual(controller.seeBalance(), 10000)
        controller.doDeposit(10000)
        self.assertEqual(controller.seeBalance(), 20000)
        controller.doWidthdraw(10000)
        self.assertEqual(controller.seeBalance(), 10000)
        controller.doWidthdraw(10000)
        self.assertEqual(controller.seeBalance(), 0)
        

if __name__ == "__main__":
    unittest.main()