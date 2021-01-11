
t=int(input())
for i in range(t):
    lst1= [int(x) for x in input().split()]
    lst2= [int(x) for x in input().split()]
    no_of_problem_per_day = lst1[1]
    total_no_of_prob = sum(lst2)
    no_of_days_possible = total_no_of_prob//no_of_problem_per_day
    # print(lst1, lst2,total_no_of_prob,no_of_days_possible)
    if no_of_days_possible>=lst1[2]:
        print(lst1[2])
    else:
        print(no_of_days_possible)