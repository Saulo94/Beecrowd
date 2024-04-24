# lista de números
nums = list(map(int, input().split()))

# número inicial
num_inicial = nums.pop(0)

for num in nums:
    if num > 0:
        print((2 * num_inicial + num - 1) * num // 2)
        break
