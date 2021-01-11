def mysol():
    import math
    t = int(input())
    for i in range(t):

        lst = [int(x) for x in input().split()]
        N = lst[0]
        K = lst[1]
        x = lst[2]
        y = lst[3]
        if x == y:
            print(N, N)
        elif y < x:
            # print("x is not eqal to y")
            coordinates = []
            req_point = K % 4
            no_of_loop = int(math.ceil(K / 4))
            for j in range(no_of_loop):
                # print(x,y)
                coordinates.append((x, y))
                # first line

                dif = N - x
                print("diff for first line is", dif)
                x = x + dif
                y = y + dif
                # print(x,y)
                coordinates.append((x, y))
                # second line

                dif = N - y
                print("diff for 2nd line is", dif)
                x = x - dif
                y = y + dif
                # print(x,y)
                coordinates.append((x, y))
                # 3rd line

                dif = x
                # print("diff for 3rd line is", dif)
                x = x - dif
                y = y - dif
                coordinates.append((x, y))
                # print(x,y)
                # fourth line

                dif = y
                # print("diff for fourth line is", dif)
                y = y - dif
                x = x + dif
                # coordinates.append((x,y))
                # print(x,y)

            # print(coordinates)

            print(*coordinates[req_point])
        elif y > x:
            coordinates = []
            req_point = K % 4
            no_of_loop = int(math.ceil(K / 4))

            for j in range(no_of_loop):
                coordinates.append((x, y))
                # first line

                dif = N - y
                print("diff for first line is", dif)
                x = x + dif
                y = y + dif
                print(x, y)
                coordinates.append((x, y))
                # second line

                dif = N - x
                print("diff for 2nd line is", dif)
                x = x + dif
                y = y - dif
                print(x, y)
                coordinates.append((x, y))
                # 3rd line
                dif = y
                print("diff for 3rd line is", dif)
                x = x - dif
                y = y - dif
                coordinates.append((x, y))
                print(x, y)
                # fourth line

                dif = x
                print("diff for fourth line is", dif)
                y = y + dif
                x = x - dif
                # coordinates.append((x,y))
                print(x, y)

            print(coordinates)

            print(*coordinates[req_point])


def sudipsol():
    for t in range(int(input())):
        n, k, x, y = map(int, input().split())
        if x == y:
            print(n, n)
        else:
            d = []
            if x < y:
                d = [[x + n - y, n], [n, n - y + x], [y - x, 0], [0, y - x]]
            else:
                d = [[n, y + n - x], [y + n - x, n], [0, x - y], [x - y, 0]]
            t = d[(k - 1) % 4]
            print(t[0], t[1])

sudipsol()