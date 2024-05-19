num_inicial = int(input())

for i, num in [(i, num_inicial * (2 ** i)) for i in range(10)]:
    print(f"N[{i}] = {num}")
