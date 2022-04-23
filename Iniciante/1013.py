a, b, c = map(int, input().split())

m = (a + b + abs(a - b)) / 2
m = int((m + c + abs(c - m)) / 2)

print(m, "eh o maior")
