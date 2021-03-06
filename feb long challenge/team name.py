t = int(input())
for s in range(t):
    n = int(input())
    funny_names = [str(x) for x in input().split()]
    # print(funny_names)
    hash_map = {}
    for i in funny_names:
        hash_map[i] = 1
    not_funny_words = []
    for i in range(0,n):
        name1 = funny_names[i]
        for j in range(i+1,n):
            name2 = funny_names[j]
            # print(name1,name2)
            name1 = funny_names[j][0] + name1[1:]
            name2 = funny_names[i][0] + name2[1:]
            # print(name1,name2)
            not_funny_words.append(name1)
            not_funny_words.append(name2)


    not_funny_words = list((set(not_funny_words)))
    # print(not_funny_words)
    # print(len(not_funny_words))

    new_list=[]
    for i in not_funny_words:
        if i in funny_names:
            pass
            # print(i,"to be del from",not_funny_words)
        else:
            new_list.append(i)
    # print(not_funny_words)
    # print(hash_map)
    # check on swapping
    c=0
    res = []
    not_funny_words[:]=new_list[:]
    for i in range(0,len(not_funny_words)):
        for j in range(i+1,len(not_funny_words)):
            name1 = not_funny_words[i]
            name2 = not_funny_words[j]
            # print(name1,name2)
            name1 = not_funny_words[j][0] + name1[1:]
            name2 = not_funny_words[i][0] + name2[1:]
            try:
                if hash_map[name1] == 1 and hash_map[name2] == 1:
                    lst = []
                    lst.append(name2)
                    lst.append(name1)
                    res.append(lst)
            except:
                pass

    print(len(res)*2)