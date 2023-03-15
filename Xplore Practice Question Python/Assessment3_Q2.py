class Account: 
    def __init__(self,cnm,p,bal,wam,at): 
        self.cnum=cnm 
        self.pin=p 
        self.balance=bal 
        self.wamount=wam 
        self.actype=at 
        
    def setwamt(self,amt): 
        self.balance-=amt 
        self.wamount=amt 
        print(self.cnum,round(self.balance,1),round(self.wamount,1)) 
        
        
class ATM: 
    def __init__(self,bnm,alt): 
        self.branchnm=bnm 
        self.actlt=alt 
        
    def withdraw(self,card,pn,wamt): 
        arr=self.actlt 
        for ac in arr: 
            if ac.cnum==card: 
                if ac.pin==pn: 
                    ac.setwamt(wamt) 
                    break 
        else: print("No account Exists") 
        
    def cdbal(self,ty): 
        arr=self.actlt 
        d={} 
        for ac in arr: 
            if ac.actype.upper()==ty.upper(): 
                d[ac.cnum]=ac.balance 
        if len(d)==0: 
            print("No match Found") 
        else: 
            x=sorted(d.items(),key=lambda x:x[1]) 
            for k,v in x: 
                print(k,round(v,1)) 
                
                
n=int(input()) 
arr=[] 
for i in range(n): 
    c=int(input()) 
    p=int(input()) 
    b=float(input()) 
    wam=float(input()) 
    ac=input() 
    obj=Account(c,p,b,wam,ac) 
    arr.append(obj) 
    
atm=ATM("mtm",arr) 
cnm=int(input()) 
pn=int(input()) 
wamt=float(input()) 
atm.withdraw(cnm,pn,wamt) 
ty=input() 
atm.cdbal(ty)