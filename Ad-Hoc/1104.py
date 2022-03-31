A, B = input().split()

while A != '0' and B != '0':
    cartasA, cartasB = set(input().split()), set(input().split())
    print(min(len(cartasB - cartasA), len(cartasA - cartasB)))
    A, B = input().split()