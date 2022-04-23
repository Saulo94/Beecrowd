x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
dist = (((x1-x2) * (x1-x2)) + ((y1-y2) * (y1-y2))) ** (1 / 2)

print("{0:.4f}".format(dist))
