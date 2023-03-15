def searchMyString(arr,s): 
    f=-1 
    if s in arr: 
        for i in range(len(arr)): 
            if s==arr[i]: 
                return i 
        else: return f 
        
n=int(input()) 
arr=[] 
for i in range(n): 
    arr.append(input()) 
    
s=input() 
r=searchMyString(arr,s) 
if r==-1: 
    print("String not found") 
else: 
    print("Position of the searched string is:{}".format(r))