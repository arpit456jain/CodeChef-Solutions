def binaryToDecimal(str1):
    num=0
    j=0
    for i in range(len(str1)-1,-1,-1):
        bitvalue = int(str1[i]) * int(math.pow(2,j))
        j=j+1
        num = num + bitvalue
        # print(bitvalue)
    # print(num)
    return  num
import math
hash_map={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p'}
t=int(input())
for i in range(t):

    n=int(input())
    str1 = input()
    no_of_iterations=n//4
    ans=""
    # print(hash_map)
    for i in range(0,n,4):
        j=i+4
        # print(i,j,str1[i:j])
        res=binaryToDecimal(str1[i:j])
        char=hash_map[res]
        # print(res,char)
        ans = ans+char
    print(ans)