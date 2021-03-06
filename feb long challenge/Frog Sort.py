import  math

t=int(input())
for i in range(t):
    n=int(input())
    wt = [int(x) for x in input().split()]
    ht = [int(x) for x in input().split()]
    my_dict={}
    s=0
    for i in range(1,n+1):
        my_dict[i] = wt.index(i)

    for i in range(2,n+1):
        t1=my_dict[i]
        t2=my_dict[i-1]
        t=0
        if t1<=t2:
            t = math.ceil((t2+1-t1)/ht[t1])
        s+=t
        my_dict[i]+=t*(ht[t1])

    print(s)