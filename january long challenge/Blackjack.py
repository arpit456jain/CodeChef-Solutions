t=int(input())
for i in range(t):
    n,l,u = map(int,input().split())
    # print(n,l,u)
    arr = [int(x) for x in input().split()]
    # print("array is",arr)
    flag=False
    a=0
    b=0
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]+arr[j] >=l and arr[i]+arr[j] <=u:
                a=arr[i]
                b=arr[j]
                # print(a,b,i,j)
                flag=True
                break
        if flag == True:
            break
    # else:
        # print(-1)

    if flag == False:
        print(-1)
    elif sum(arr[0:2])>=l and sum(arr[0:2])<=u:
        # print(sum(arr[0:2]),l,u)
        # print("tst")
        print(0)
    elif (arr[0] == a and arr[1] == b) or (arr[1]==a and arr[0]==b):
        print(0)
    else:
        # print("swap required")
        if arr[0] == a or arr[1]==a:
            print(1)
        elif arr[0] == b or arr[1] == b:
            print(1)
        else:print(2)