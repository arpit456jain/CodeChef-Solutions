'''
Alisha has a string of length n. Each character is either 'a', 'b' or 'c'. She has to select two characters s[i] and s[j] such that s[i] != s[j] and i,j are valid indexes. She has to find the maximum value of the absolute difference between i and j i.e abs(i-j) .

Since Alisha is busy with her Semester exams help her find the maximum distance where distance is the maximum value of absolute difference between i and j i.e abs(i-j) .
'''
def sol2(str1):
    max_dis = 0
    lenofstr = len(str1)
    i = 0
    while (i < lenofstr - 1):
        j = i + 1
        # print(i,j,str1[i],str1[j])
        while (j < lenofstr and str1[j] != str1[i] ):
            j += 1
        # print(i,j)
        if j - i -1 >= max_dis:
            max_dis = j - i -1
        i += 1
    # print(max_dis)
    return max_dis

def sol1(str1):
    max_dis = 0
    lenofstr = len(str1)
    for i in range(0,lenofstr):
        for j in range(i,lenofstr):
            if str1[i] != str1[j]:
                if j-i >= max_dis:
                    max_dis=j-i
    # print(max_dis)
    return max_dis

str1 = input()
# ans = sol1(str1)
# print(ans)
ans = sol2(str1)
print(ans)

