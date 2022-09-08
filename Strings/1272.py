qt_casos = int(input())

for _ in range(qt_casos):
    nova_palavra = "".join([palavra[0] for palavra in input().split()])

    print(nova_palavra)
