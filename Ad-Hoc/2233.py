red, green, blue = int(input(), 16), int(input(), 16), int(input(), 16)

quat_total = (((red // green) * green) ** 2) // (green ** 2)
quat_total += (quat_total * ((((green // blue) * blue) ** 2) // (blue ** 2))) + 1

print(hex(quat_total)[2:])
