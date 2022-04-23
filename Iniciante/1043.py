a, b, c = map(float, input().split())

if (abs(b - c) < a < b + c) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b):
    print("Perimetro = {:.1f}".format(a + b + c))
else:
    print("Area = {:.1f}".format((a + b) * (c / 2)))
