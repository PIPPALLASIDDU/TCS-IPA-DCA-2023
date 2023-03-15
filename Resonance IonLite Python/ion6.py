class city:
    def __init__(self,cid,snm,ct,cb,ab,vb,avb):
        self.cid=cid
        self.sname=snm 
        self.city=ct 
        self.cbeds=cb 
        self.avbeds=ab 
        self.vebeds=vb 
        self.avvebeds=avb 

class CovBedsAnalysis:
    def __init__(self,nm,clt):
        self.name=nm
        self.citylist=clt

    def get_StateWiseAvlblBedStats(self):
        d={}
        for obj in self.citylist:
            if d.get(obj.sname):
                d[obj.sname][0]+=obj.avbeds
                d[obj.sname][1]+=obj.avvebeds
            else:
                d[obj.sname]=[obj.avbeds,obj.avvebeds]
        res=sorted(d.items(),key=lambda x:x[0])
        for k,v in res:
            print(k,v[0],v[1])

    def get_CitesWithMoreThanAvgOccupiedbeds(self,state):
        ct=[]
        cavg,vavg=0,0
        cnt=0
        for obj in self.citylist:
            if obj.sname==state:
                ct.append(obj)
                cnt+=1
                cavg+=(obj.cbeds-obj.avbeds)
                vavg+=(obj.vebeds-obj.avvebeds)

        cavg=cavg/cnt
        vavg=vavg/cnt 
        for obj in ct:
            if cavg<(obj.cbeds-obj.avbeds) and vavg<(obj.vebeds-obj.avvebeds):
                cnt=0
                print(obj.city,(obj.cbeds-obj.avbeds),(obj.vebeds-obj.avvebeds))
        if cnt!=0:
            print("No city available")

n=int(input())
arr=[]
for i in range(n):
    cid=int(input()) 
    snm=input()
    ct=input()
    cb=int(input())
    ab=int(input())
    vb=int(input())
    avb=int(input())
    obj=city(cid, snm, ct, cb, ab, vb, avb)
    arr.append(obj)
st=input()
cobj=CovBedsAnalysis("covid", arr)
cobj.get_StateWiseAvlblBedStats()
cobj.get_CitesWithMoreThanAvgOccupiedbeds(st)
