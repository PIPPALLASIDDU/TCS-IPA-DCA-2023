n=int(input())
arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)
num=int(input())
cnt=arr.count(num)
if cnt<2:
    print(0)
else:
    cnt=0
    for i in range(n):
        if arr[i]==num:
            cnt+=1
        if cnt==2:
            print(i)
            break
