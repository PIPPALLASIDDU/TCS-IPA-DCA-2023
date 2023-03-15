class Doner:
    def __init__(self,did,nm,num,bg,pdm,af):
        self.didi=did
        self.name=nm
        self.number=num
        self.bldgrp=bg
        self.prevdonmnt=pdm
        self.awayfm=af

class BloodBank:
    def __init__(self,nm,ltd):
        self.name=nm
        self.dnrlist=ltd

    def getListofAvailableDonors(self):
        donorsbg=[dnr.bldgrp for dnr in self.dnrlist]
        don_dict={}
        for bg in donorsbg:
            don_dict[bg]=0
        for dnr in self.dnrlist:
            if dnr.awayfm<50:
                if 12-dnr.prevdonmnt>=4:
                    don_dict[dnr.bldgrp]+=1
        
        return don_dict
        

    def getAndUpdateDonor(self,bg,rd):
        don_dict=self.getListofAvailableDonors()
        if rd>=don_dict[bg]:
            print("Donor count not available")
            for dnr in self.dnrlist:
                if dnr.bldgrp==bg:
                    dnr.prevdonmnt=12
        else:
            print("Donor count available")
            cnt=0
            for dnr in self.dnrlist:
                if dnr.bldgrp==bg:
                    cnt+=1
                    dnr.prevdonmnt=12
                if cnt==rd:
                    break
        
            


n=int(input())
arr=[]
months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov"]
for i in range(n):
    did=int(input())
    nm=input() 
    num=input()
    bg=input()
    pdm=input()
    mon=months.index(pdm) + 1
    af=int(input())
    obj=Doner(did, nm, num, bg, mon, af)
    arr.append(obj)

bldbnk=BloodBank("cheeranjivi Blood bank", arr)
bg=input()
dcnt=int(input())
don_dict=bldbnk.getListofAvailableDonors()
for k,v in sorted(don_dict.items(),key=lambda x:x[0]):
    print(k,v)
bldbnk.getAndUpdateDonor(bg,dcnt)
don_dict=bldbnk.getListofAvailableDonors()
for k,v in sorted(don_dict.items(),key=lambda x:x[0]):
    print(k,v)