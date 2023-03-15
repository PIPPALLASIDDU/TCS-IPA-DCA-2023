class Book: 
    def __init__(self,bid,nm,aut): 
        self.bid=bid 
        self.name=nm 
        self.author=aut 
        
        
class Library: 
    def __init__(self,blt,ad): 
        self.booklist=blt 
        self.address=ad 
        
        
    def cntbook(self): 
        arr=self.booklist 
        d={} 
        for b in arr: 
            nm=b.author.upper() 
            if nm in d.keys(): 
                d[nm]+=1 
            else: 
                d[nm]=1 
                
        for k,v in d.items(): 
            print(k,v) 
            
    def booklt(libs,cty): 
        arr=[] 
        for l in libs: 
            ar=[] 
            if l.address['city'].upper()==cty.upper(): 
                ar.extend(l.booklist) 
                arr.extend(list(sorted(ar,key=lambda x:x.bid,reverse=True))) 

        if len(arr)==0: 
            return None 
        return arr 
        
libs=int(input()) 
liblt=[] 
for i in range(libs): 
    n=int(input()) 
    blt=[] 
    for j in range(n): 
        bid=input() 
        nm=input() 
        aut=input() 
        obj=Book(bid,nm,aut) 
        blt.append(obj) 
    ad={} 
    ad['street']=input() 
    ad['area']=input() 
    ad['city']=input() 
    ad['state']=input() 
    ad['zip']=input() 
    obj=Library(blt,ad) 
    liblt.append(obj)


c=input() 
liblt[0].cntbook() 
x=booklt(liblt,c) 
if x is None: 
    print("No Book Found") 
else: 
    print([b.name for b in x])