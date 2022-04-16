t1, t2, t3 = map(int, input().split())

var1 = t2 - t1
var2 = t3 - t2

if var1 > 0:
    if var2 >= var1:
        print(":)")
    else:
        print(":(")
elif var1 < 0:
    if var2 > var1:
        print(":)")
    else:
        print(":(")
else:
    if var2 > 0:
        print(":)")
    else:
        print(":(")
