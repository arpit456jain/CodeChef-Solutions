'''
Dinesh is very fond of sweets recently his aunt Riya gifted him an array a of sweets of size N. The ith sweet is of the type a[i]. His mother told him that he can choose one type of sweet in a day and eat at most 2 sweets of that type. Since he has to eat all the sweets as quickly as possible because his cousins are arriving. Find out the minimum number of days in which he can eat all the sweets gifted by his aunt Riya.


'''
n = int(input())
array = [int(x) for x in input().split()]
array.sort()

type = array[0]

hash_map={}
i=0
while(i<len(array)):
    if array[i] in hash_map.keys():
        hash_map[array[i]]+=1
    else:
        hash_map[array[i]] = 1
    i+=1

# print(hash_map)
no_of_days =0
for i,j in hash_map.items():
    if j%2==0:
        no_of_days = no_of_days + j//2
    else:
        no_of_days = no_of_days + j//2 + 1
print(no_of_days)