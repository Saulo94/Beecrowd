quat_bandeja = int(input())
quat_copos = 0
for i in range(quat_bandeja):
    bandeja = list(map(int, input().split()))
    if bandeja[0] > bandeja[1]:
        quat_copos += bandeja[1]
print(quat_copos)
