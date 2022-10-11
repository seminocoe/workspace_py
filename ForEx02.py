i, j = 0, 0

for i in range(2, 10, 1):
    for j in range(2, 10, 1):
        print("%2d x %2d = %2d   " %(j, i, i*j), end="")
    print("")