n=int(input()) 
arr=[] 
for i in range(n): 
    s=input() 
    for i in s: 
        if i in ['a','e','i','o','u','A','E','I','O','U']: 
            break 
    else: 
        arr.append(s) 
if len(arr)==0: 
    print("No string found") 
else: 
    print("Strings without vowels:") 
    for i in arr: 
        print(i)

                                 