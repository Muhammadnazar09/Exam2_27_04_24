list1=input().split()
i=0
while i<len(list1):
    list1[i-1]=list1[i]
    print(list1[i])
    i+=1