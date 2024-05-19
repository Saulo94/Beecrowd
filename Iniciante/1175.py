lista_nums = [0 for _ in range(20)]

for i in range(20):
    num = int(input())

    lista_nums[19 - i] = (19 - i, num)

print("\n".join([f"N[{i}] = {num}" for i, num in lista_nums]))
