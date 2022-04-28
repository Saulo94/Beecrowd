a, g, ra, rg = list(map(float, input().split()))

va = a / ra
vg = g / rg

print("{0}".format("G" if vg <= va else "A"))
