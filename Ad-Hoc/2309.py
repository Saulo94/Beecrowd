dicionario = {'4': 0, '5': 1, '6': 2, '7': 3, '12': 4, '11': 5, '13': 6, '1': 7, '2': 8, '3': 9}

part_adalberto, part_bernadete = 0, 0
for _ in range(int(input())):
    rodadas = input().split()
    pont_adalberto, pont_bernadete = 0, 0
    
    if dicionario[rodadas[0]] >= dicionario[rodadas[3]]:
        pont_adalberto += 1
    else:
        pont_bernadete += 1
    
    if dicionario[rodadas[1]] >= dicionario[rodadas[4]]:
        pont_adalberto += 1
    else:
        pont_bernadete += 1
    
    if dicionario[rodadas[2]] >= dicionario[rodadas[5]]:
        pont_adalberto += 1
    else:
        pont_bernadete += 1
    
    if pont_adalberto > pont_bernadete:
        part_adalberto += 1
    else:
        part_bernadete += 1

print(part_adalberto, part_bernadete)
