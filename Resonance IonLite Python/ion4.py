n=int(input())
prime=[]
nprime=[]
for _ in range(n):
    num=int(input())
    for i in range(2,num):
        if num%i==0:
            nprime.append(num)
            break
    else:
        prime.append(num)
if n%2==0:
  print(0)
else:
  print(1)
res=[prime,nprime]
print(res)