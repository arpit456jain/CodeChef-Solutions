def sol1():
    t=int(input())
    for i in range(t):
        lst1= [int(x) for x in input().split()]
        lst2= [int(x) for x in input().split()]
        lst3= [int(x) for x in input().split()]

        ans = lst2.copy()
        ans.append(0)
        res=lst2[0]^lst2[0]
        res2=0
        for i in lst2:
            res = res^i
            res2=i&lst3[0]
            for i in lst3:
                res2=i&res2
                ans.append(res2)
            ans.append(res)

        #yaha combination ka logic sochna hai kyui loop nahi chla skte
        ans=set(ans)
        ans = list(ans)
        # print(ans)
        print(len(ans))

def sol2():
    t = int(input())
    for i in range(t):
        lst1 = [int(x) for x in input().split()]
        lst2 = [int(x) for x in input().split()]
        lst3 = [int(x) for x in input().split()]

        ans = lst2.copy()
        ans.append(0)

      # case 1
      #   agr vo sare cards set 1 me se le
        res =0
        for i in lst2:
            res = res|i
            ans.append(res)
        # case 2
        # agr vo sare cards set 2 me s le
        res=0
        for i in lst3:
            res=res&i
            ans.append(res)

        # yaha combination ka logic sochn
        # a hai kyui loop nahi chla skte
        res = 0

        lenofa = len(lst2)
        lenofb = len(lst3)
        i=0
        while i<min(lenofa,lenofb):
            res = res|lst2[i]
            ans.append(res)
            res = res&lst3[i]
            ans.append(res)
            i+=1
        if lenofa>lenofb:
            while(i<lenofa):
                res = res | lst2[i]
                i+=1
        if lenofb>lenofa:
            while (i<lenofb):
                res = res & lst3[i]
                i+=1
        ans = set(ans)
        ans = list(ans)
        print(ans)
        print(len(ans))

sol2()