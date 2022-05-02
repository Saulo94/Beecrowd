nota = int(input())

if nota == 0:
    print("E")
elif 0 < nota <= 35:
    print("D")
elif 35 < nota <= 60:
    print("C")
elif 60 < nota <= 85:
    print("B")
else:
    print("A")
