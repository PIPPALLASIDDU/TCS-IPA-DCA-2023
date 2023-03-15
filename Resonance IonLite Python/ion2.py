n=int(input())
for i in range(n):
  s=input()
  if s.upper()==s[::-1].upper():
    print(s)
              