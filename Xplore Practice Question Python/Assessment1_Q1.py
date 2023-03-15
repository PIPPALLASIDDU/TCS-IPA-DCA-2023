def validstr(s): 
    arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'," "] 
    for i in s.lower(): 
        if i not in arr: 
            return False 
    return True 
n=int(input()) 
valid=0 
invalid=0 
for i in range(n): 
    if validstr(input()): 
        valid+=1 
    else: 
        invalid+=1 
print(f"Count Of Valid Strings= {valid}") 
print(f"Count Of Invalid Strings= {invalid}")