a, b, c = map(float, input().split())
d = (b * b) - (4 * a * c)

if d > 0 and a != 0:
    print("R1 = {0:.5f}\n"
          "R2 = {1:.5f}".format(
        (-b + (d ** (1 / 2))) / (2 * a),
        (-b - (d ** (1 / 2))) / (2 * a)
    ))
else:
    print("Impossivel calcular")
