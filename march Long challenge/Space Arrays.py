t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    c=0
    for i in range(0,len(arr)):
        # print(arr[i],"at",i+1)
        if arr[i]>(i+1):
            c=-1
            break
        else:
            c=c+(i+1-arr[i])
    if c==-1:
        print("Second")
    elif c%2==0:
        print("Second")
    else:
        print('First')