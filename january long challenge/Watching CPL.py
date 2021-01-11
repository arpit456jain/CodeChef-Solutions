
def solution1():
    t=int(input())
    for i in range(t):
        lst1= [int(x) for x in input().split()]
        lst2= [int(x) for x in input().split()]

        K = lst1[1]
        N = lst1[0]

        lst2.sort()
        print(lst2)
        h1=0
        h2=0
        sumofboxes=sum(lst2)
        #agr boxes ka sum 2*h se km hota hai to possible hi nhi hai
        if sumofboxes<2*K:
            print(-1)
            continue
        else:
            # sum to chalo req height se jyada hai
            try:
                #hm try krege unko arrange krne ki agr koi problem hoti hai to it means arrangement
                # is not possible
                pi=0 #popped value

                #sabse phle hm 1 by 1 bigger boxes ko rakhege 1 ke upr 1 2 jgah
                # y loop tb tk chlega jb tk kisi 1 ki height greater than or equal to na ho jai
                while(h1<K and h2<K):
                    pi1 =lst2.pop()
                    pi2 =lst2.pop()

                    h1 = h1 + pi1
                    h2 = h2 + pi2

                #y vo height hai jaha at least 1 h greater than or equal hai or pi1 pi2 vo last poped values
                print("after 1st while",h1,h2,pi1,pi2,lst2)

                #if 1 ki height equal ho gai to baki boxes 2nd wale m rakhte jaige
                if h1>K and h2>K:
                    pass
                elif h1 == K or h2 == K:
                    # print("1st case if any one will become equal", h1, h2)
                    if h1 == K:
                        while(h2<K):
                            h2 = h2 + lst2.pop()
                    else:
                        while h1<K:
                            h1 = h1 + lst2.pop()



                elif h1>K and h2>=K:
                    # print("h1 is grater and h2 is equal",h1,h2,lst2)
                    pass
                elif h2>K and h1>=K:
                    # print("h2 is greater and h1 is equal",h1,h2,lst2)
                    pass
              # if 1 ki height K se bdi ho jati hai to hm last dono boxes hta ke perfect height ka box fit
                # krenge
                elif h1>K and h2<K:
                    # print("h1 is greater and h2 is smaller",h1,h2,lst2)
                    h1 = h1 - pi1
                    h2 = h2 - pi2

                    lst2.append(pi1)
                    lst2.append(pi2)
                    lst2.sort()
                    # print("after removing last 2 boxes", h1, h2, lst2)

                    for i in lst2:
                        if h1+i >= K:
                            # print(i,"can be added")
                            h1 = h1 + i
                            lst2.remove(i)
                            break
                    # print(lst2,h1)
                    while(h2<K):
                        h2 = h2 + lst2.pop()
                    # print(h2)
                elif h2>K and h1<K:
                    # print("h2 is greater and h1 is smaller",h1,h2,lst2)
                    h1 = h1 - pi1
                    h2 = h2 - pi2
                    lst2.append(pi1)
                    lst2.append(pi2)
                    lst2.sort()
                    # print(lst2)
                    for i in lst2:
                        if h2+i >= K:
                            h2 = h2 + i
                            lst2.remove(i)
                            break
                    # print(lst2,h2)
                    while(h1<K):
                        h1 = h1 + lst2.pop()
                    # print(h1)

                else:
                    pass
                ans = lst1[0] - len(lst2)
                # print("final ans",lst2,ans)
                print(ans)
            except:
                # raise Exception("list got empty")
                print(-1)



def allcombination(a_list):
    all_combinations = []
    for r in range(len(a_list) + 1):
        combinations_object = combinations(a_list, r)
        combinations_list = list(combinations_object)
        all_combinations += combinations_list
    return all_combinations


from itertools import combinations
def rSubset(arr, r):
    # return list of all subsets of length r
    # to deal with duplicate subsets use
    # set(list(combinations(arr, r)))
    return list(combinations(arr, r))
def solution2():
    t=int(input())
    for i in range(t):

        n,k = map(int,input().split())
        heights = [int(x) for x in input().split()]
        heights.sort()
        print(n,k,heights)

        #pehele sare sub arrays find kr lo jo ki sum>= k hai phr unme se usko choose kro jiski
        # length bhi min hai
        lst=[]
        flag=False
        try:

            for i in range(1,len(heights)+1):
                combinations=rSubset(heights, i)
                # print(combinations)
                for i in combinations:
                    if sum(i)>=k:
                        flag = True
                        lst.append(i)
                if flag==True:
                    break
            # print(lst)

            min_sum =sum(lst[0])
            min_l = len(lst[0])
            min_subarray = lst[0]
            # print("1st one",min_sum,min_subarray)
            for i in lst:
                # print(i,sum(i))
                if sum(i)<min_sum and len(i)<=min_l:
                    min_sum=sum(i)
                    min_subarray=i
            # print("min sum",min_sum,"and min array",min_subarray)
            for i in min_subarray:
                heights.remove(i)
            # print(heights)

            h2=0
            while(h2<k):
                h2 = h2 + heights.pop()

            print(n-len(heights))
        except:
            print(-1)
# solution2()
# solution1()

# Returns true if there exists a subset
# with given sum in arr[]

def isSubsetSum(arr, n, sum):
    # The value of subset[i%2][j] will be true
    # if there exists a subset of sum j in
    # arr[0, 1, ...., i-1]
    subset = [[False for j in range(sum + 1)] for i in range(3)]

    for i in range(n + 1):
        for j in range(sum + 1):
            # A subset with sum 0 is always possible
            if (j == 0):
                subset[i % 2][j] = True

            # If there exists no element no sum
            # is possible
            elif (i == 0):
                subset[i % 2][j] = False
            elif (arr[i - 1] <= j):
                subset[i % 2][j] = subset[(i + 1) % 2][j - arr[i - 1]] or subset[(i + 1)
                                                                                 % 2][j]
            else:
                subset[i % 2][j] = subset[(i + 1) % 2][j]

    return subset[n % 2][sum]

def solution3():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        heights = [int(x) for x in input().split()]
        heights.sort()
        # print(n, k, heights)

        sumofh = 0
        i=n-1
        tower = []
        ans=-1
        if sum(heights)<2*k:
            ans = -1
        elif sum(heights) == 2*k:
            ans = len(heights)
        else:

            while(i!=0 and sumofh< 2*k):
                pi = heights.pop()
                sumofh = sumofh + pi
                tower.append(pi)
                i=i-1
            # print(heights,sumofh,tower)
            diff = sumofh-2*k
            for i in range(diff+1):
                if (isSubsetSum(tower, len(tower), k+i) == True):
                    ans = n - len(heights)
                    break
            # elif(isSubsetSum(tower, len(tower), sumofh//2) == True):
            #     # print("found")
            #     ans = n - len(heights)
            else:
                # print("No subset with given sum")
                #now grab next element
                try:
                    pi = heights.pop()
                    sumofh = sumofh+pi
                    diff = sumofh - 2 * k
                    for i in range(diff + 1):
                        if (isSubsetSum(tower, len(tower), k + i) == True):
                            ans = n - len(heights)
                            break

                    # print(ans)
                except:
                    ans = -1
        print(ans)

# solution3()

def solution4():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        heights = [int(x) for x in input().split()]
        heights.sort()
        heights[:] = heights[::-1]
        # print(n, k, heights)
        sumofh = sum(heights)

        if sumofh < 2*k:
            print(-1)
        else:

            sa=0
            t=0
            i=0
            while i<n:
                sa=sa+heights[i]

                if(sa>=k):
                    break
                for j in range(i+1,n):
                    if heights[j] >= (k-sa):
                        t=1
                if t==1:
                    sa=sa+heights[j]
                    heights[j],heights[i+1] = heights[i+1],heights[j]
                i=i+1
            # print(sa)


            sb=0
            m=0
            # print(i)
            while(i<n):
                sb = sb + heights[i]

                if sb>=k:
                    break
                for j in range(i+1,n-1):
                    if heights[j] >= (k-sb):
                        m=1
                if m==1:
                    sb += heights[j]
                    # print("j is",j)
                    heights[j] , heights[j+1] =heights[j],heights[j+1]
                if m !=1:
                    for j in range(i+1,n):
                        if heights[m] < k-sb:
                            break
                    heights[m],heights[i+1]=heights[i+1],heights[m]
                i=i+1
        # print(sb)
        # print("i is at",i)
        print(i+1)
# solution4()

def solution5():
    print("this is solution 5")
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        heights = [int(x) for x in input().split()]
        h1=[]
        heights.sort()
        # print(n,k,heights)
        sum1=0
        h1.append(heights[n-1])
        sum1 = heights[n-1]
        z=-1
        p=0
        # print(h1[0])
        for i in range(n-2,-1,-1):
            # print(i)
            h2=[]
            # print("in starting",h1,h2)
            sum1=sum1+heights[i]
            # print("initial sum",sum1)
            for l in h1:
                p = l
                # print("p is",p)
                h2.append(p)
                h2.append(heights[i])
                h2.append(p+heights[i])
                if ((p+heights[i])>=k) and ((sum1-p-heights[i])>=k):
                    # print(p+heights[i],sum1-p-heights[i],k)
                    # print("1st breaking")
                    z=n-i
                    break                   
                if heights[i]>=k and (sum1-heights[i])>=k:
                    z=n-i
                    # print("2nd break")
                    break
            if z!=-1:
                break
            # print(h1,h2)
            h1=h2.copy()
        # print("final ans is",z)
        print(z)
solution5()