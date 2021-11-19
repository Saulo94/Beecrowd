for i in range(int(input())):
    n = [float(x) for x in input().split(" ")]

    print(round((n[0] * 2 + n[1] * 3 + n[2] * 5) / 10, 1))