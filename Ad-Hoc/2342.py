d = {"+": int.__add__, "*": int.__mul__}
numero = int(input())
num1, ope, num2 = input().split()

res = d[ope](int(num1), int(num2))

print("OVERFLOW" if res > numero else "OK")
