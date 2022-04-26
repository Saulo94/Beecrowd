val1, val2 = map(int, input().split())

while True:
    print(val1 * val2 * 2)
    try:
        val1, val2 = map(int, input().split())
    except EOFError:
        break
