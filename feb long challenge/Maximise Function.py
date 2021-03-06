def Differene(a,b):
    if a>b:
        return a-b
    else:
        return b-a
t=int(input())

for i in range(t):
    n = int(input())
    diff=0
    new_list = []
    arr = [int(x) for x in input().split()]
    arr.sort()
    # print(arr)
    x=0
    y=n-1
    z=n-2
    ans1=0
    ans1 = ans1 + Differene(arr[x],arr[y]) + Differene(arr[x],arr[z]) + Differene(arr[z],arr[y])

    x=0
    y=1
    z=n-1
    ans2=0
    ans2 = ans2+ Differene(arr[x], arr[y]) + Differene(arr[x], arr[z]) + Differene(arr[z], arr[y])

    final_ans = max(ans1,ans2)
    print(final_ans)