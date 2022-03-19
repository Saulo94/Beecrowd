co = list(int(i) for i in input().split())

lp = []
it = 1
while not (co[0] == 0 and co[1] == 0 and co[2] == 0 and co[3] == 0):
    print("Teste {0}".format(it))
    qd = 0
    qm = int(input())

    for i in range(qm):
        cm = list(int(i) for i in input().split())
        if ((cm[0] <= co[2]) and (cm[0] >= co[0])) and ((cm[1] <= co[1]) and (cm[1] >= co[3])):
            qd += 1
    print(qd)
    it += 1

    co = list(int(i) for i in input().split())