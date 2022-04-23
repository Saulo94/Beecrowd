hora_i, min_i, hora_f, min_f = map(int, input().split())

t1 = hora_i * 60 + min_i
if hora_f <= hora_i and min_f <= min_i:
    t = 24 * 60 - t1 + hora_f * 60 + min_f
else:
    t = hora_f * 60 + min_f - t1
h = int(t / 60)
m = int(t % 60)

print("O JOGO DUROU", h, "HORA(S) E", m, "MINUTO(S)")
