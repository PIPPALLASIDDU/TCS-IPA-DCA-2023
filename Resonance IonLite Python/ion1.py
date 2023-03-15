class Account:
    def __init__(self,actno,actnm,actbal):
        self.actno=actno
        self.actnm=actnm
        self.actbal=actbal

class AccountDemo:
    def __init__(self):
        pass
    def depositAmnt(self,actobj,amt):
        actobj.actbal+=amt
        print(actobj.actbal)

    def withdrawAmt(self,actobj,amt):
        actobj.actbal-=amt
        if actobj.actbal<1000:
            actobj.actbal-=amt
            print("No Adequate balance")
        else:    
            print(actobj.actbal)

if __name__ == '__main__':
    acno=int(input())
    acname=input()
    acntbal=int(input())
    depamnt=int(input())
    withamnt=int(input())
    acnt=Account(acno,acname,acntbal)
    acntdemoobj=AccountDemo()
    acntdemoobj.depositAmnt(acnt, depamnt)
    acntdemoobj.withdrawAmt(acnt, withamnt)
