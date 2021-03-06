def maxSubArraySum(a, size):
    ##Your code here
    max_so_far = a[0]
    max_ending_here = 0
    for i in a:
        max_ending_here=max_ending_here+i
        if max_so_far<max_ending_here:
            max_so_far=max_ending_here
        if max_ending_here<0:
            max_ending_here=0
    return max_so_far



n = int(input())
array = [int(x) for x in input().split()]

#use sliding window tech for both end
# case 1 mid = n//2
mid = n//2
cur_sum=0
max_sum =array[0]

sum1 = maxSubArraySum(array[0:mid],len(array[0:mid]))
    # print(sum1)

sum2 = maxSubArraySum(array[mid:],len(array[mid:]))
    # print(sum2)

total = sum1 + sum2

mid = n//2 - 10
max_sum1=total
while(mid<n//2 + 10):
    try:
        cur_sum=0
        max_sum =array[0]

        sum1 = maxSubArraySum(array[0:mid],len(array[0:mid]))
        # print(sum1)

        sum2 = maxSubArraySum(array[mid:],len(array[mid:]))
        # print(sum2)

        total = sum1 + sum2

        if total>=max_sum1:
            max_sum1=total
    except:
        pass
    mid+=1

print(max_sum1)