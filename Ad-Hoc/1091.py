nc = int(input())
re = []
while nc != 0:
    pd = list((int(i) for i in input().split()))
    i = 0
    while i < nc:
        co = list((int(i) for i in input().split()))

        if (co[0] < pd[0]) and (co[1] > pd[1]):
            re.append("NO")
        elif (co[0] > pd[0]) and (co[1] > pd[1]):
            re.append("NE")
        elif (co[0] > pd[0]) and (co[1] < pd[1]):
            re.append("SE")
        elif (co[0] < pd[0]) and (co[1] < pd[1]):
            re.append("SO")
        else:
            re.append("divisa")
        i += 1
    nc = int(input())
for i in re:
    print(i)