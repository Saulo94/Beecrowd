qt = int(input())
qp = []
ip = -1
while qt != 0:
    li = list(int(i) for i in input().split())
    qp.append(0)
    ip += 1
    i = 0
    while i < qt:
        if i == (qt - 1):
            if ((li[i] > li[0]) and (li[i] > li[i-1])) or ((li[i] < li[0]) and (li[i] < li[i-1])):
                qp[ip] += 1
        elif ((li[i] > li[i+1]) and (li[i] > li[i-1])) or ((li[i] < li[i+1]) and (li[i] < li[i-1])):
            qp[ip] += 1
        i += 1
    qt = int(input())
for i in qp:
    print(i)