x1, y1, x2, y2 = list(map(int, input().split()))

while [x1, y1, x2, y2] != [0] * 4:
    steps = 0
    if x1 != x2 and y1 != y2:
        dif_x = x2 - x1
        dif_y = y2 - y1
        dist_max = min(abs(dif_x), abs(dif_y))
        x1 += dist_max if dif_x > 0 else -dist_max
        y1 += dist_max if dif_y > 0 else -dist_max
        steps += 1

    if x2 - x1 != 0 or y2 - y1 != 0:
        steps += 1
    print(steps)

    x1, y1, x2, y2 = list(map(int, input().split()))