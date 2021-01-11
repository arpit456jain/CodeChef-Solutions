
t = int(input())
for i in range(t):
    lst1= [int(x) for x in input().split()]
    lst2= [int(x) for x in input().split()]
    lst3= [int(x) for x in input().split()]
    lst2.sort()
    n2=len(lst2)
    n3=len(lst3)
    lst3.sort()
    c=0
    j = min(n2,n3)
    i=0
    flag=False
    # print(j,"max loop")
    while i<j:
        print(i)
        if sum(lst2)>sum(lst3):
            flag=True
            break
        print("before swapping ",lst2,lst3)
        temp = lst2[i]
        lst2[i]=lst3[n3-1-i]
        lst3[n3-1-i] = temp
        print("after swpping",lst2,lst3)
        c=c+1
        i=i+1
    if flag==True or sum(lst2)>sum(lst3):
        print(c)
    else:
        print(-1)