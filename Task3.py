n=input().split()
m=int(input())
for i in range(len(n)):
    if int(i)==m:
        continue
    print(n[i])