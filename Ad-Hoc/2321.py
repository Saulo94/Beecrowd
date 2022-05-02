c1_x1, c1_y1, c1_x2, c1_y2 = map(int, input().split())
c2_x1, c2_y1, c2_x2, c2_y2 = map(int, input().split())

colidiu = 1 if c1_x2 < c2_x1 or c1_x1 > c2_x2 or c1_y1 > c2_y2 or c1_y2 < c2_y1 else 0

print(colidiu)
