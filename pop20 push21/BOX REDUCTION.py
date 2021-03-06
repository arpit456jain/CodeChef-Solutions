n=int(input())
lst = []
for i in range(2*n):
    box = (input())
    lst.append(box)
print(lst)
lst2 = []
for i in lst:
    try :
        lst.append(int(i))
    except:
        pass
print(lst2)