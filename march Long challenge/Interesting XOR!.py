'''
You are given an integer C. Let d be the smallest integer such that 2d is strictly greater than C.

Consider all pairs of non-negative integers (A,B) such that A,B<2d and A⊕B=C (⊕ denotes the bitwise XOR operation). Find the maximum value of A⋅B over all these pairs.
'''


def DecimalToBinary(num,str1):
    if num > 1:
        str1 = DecimalToBinary(num // 2,str1)
    # print(num % 2, end='')
    str1=str1+str(num % 2)
    return str1

def binaryToDecimal(n):
    return int(n, 2)


# Driver Code
if __name__ == '__main__':
    # str1 = DecimalToBinary(dec_val,str1)
    # print(str1,binaryToDecimal(str1))
    t= int(input())
    # t=1
    for i in range(t):
        str1 = ""
        c = int(input())
        # c=13
        str1 = DecimalToBinary(c,str1)
        # print(str1)
        a="1"
        b="0"

        for i in range(1,len(str1)):
            if int(str1[i]) == 1:
                a = a + "0"
                b = b + "1"
            elif int(str1[i]) == 0:
                a = a + "1"
                b = b + "1"
            else:
                print("errror")

        # print(a,b)
        a = binaryToDecimal(a)
        b = binaryToDecimal(b)
        # print(a,b)
        print(a*b)