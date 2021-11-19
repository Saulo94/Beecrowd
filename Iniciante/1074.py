for i in range(int(input())):
    n = int(input())
    if n == 0:
        print("NULL")
        continue
    if n % 2 == 0:
        palavra = "EVEN"
    else:
        palavra = "ODD"
    if n > 0:
        palavra += " POSITIVE"
    else:
        palavra += " NEGATIVE"
    print(palavra)