s=input() 
n=int(input()) 
if len(s)%2==0: 
    mid=(len(s)//2)-1 
else: 
    mid=len(s)//2 
    
if mid+n<len(s): 
    print(s[mid:mid+n]) 
else: 
    print(s[mid:])