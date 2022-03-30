h1, m1, h2, m2 = list(map(int, input().split()))

while [h1, m1, h2, m2] != [0] * 4:
    minutes1 = 60 * h1 + m1
    minutes2 = 60 * h2 + m2
    if minutes2 <= minutes1:
        minutes = minutes2 + 24 * 60 - minutes1
    else:
        minutes = minutes2 - minutes1
    print(minutes)

    h1, m1, h2, m2 = list(map(int, input().split()))