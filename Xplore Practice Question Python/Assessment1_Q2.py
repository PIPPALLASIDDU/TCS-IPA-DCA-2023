class Employee: 
    def __init__(self,nm,des,sal,otc,ots=False): 
        self.name=nm 
        self.desg=des 
        self.sal=sal 
        self.otc=otc 
        self.ots=ots 
        
class Organization: 
    def __init__(self,lt): 
        self.elt=lt 
        
    def checkots(self,ott): 
        for e in self.elt: 
            if sum(e.otc.values())>=ott:
                e.ots=True
                print(e.name, e.ots)
            else:
                print(e.name, e.ots)
            
    def bonus(self,rph): 
        bon=0 
        for e in self.elt: 
            if e.ots: 
                bon+=sum(e.otc.values()) 
                
        return bon*rph 
        
n=int(input()) 
arr=[] 
for i in range(n): 
    nm=input() 
    de=input() 
    sal=int(input()) 
    m=int(input()) 
    d={} 
    for j in range(m): 
        k=input() 
        v=int(input()) 
        d[k]=v 
    obj=Employee(nm,de,sal,d) 
    arr.append(obj) 
    
org=Organization(arr) 
ott=int(input()) 
org.checkots(ott)
rph=int(input()) 
print(org.bonus(rph))