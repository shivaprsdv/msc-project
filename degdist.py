import sys
f = open(sys.argv[-1], "r")
g = [[int(x) for x in l.split(" ")] for l in f.readlines()]
f.close()
n = max(max(l[0] for l in g), max(l[1] for l in g))

for i in range(1, n + 1):
    k1 = k2 = 0
    for j in range(len(g)):
        if g[j][0] == i or g[j][1] == i:
            if g[j][2] == 1:
                k1 += 1
            else:
                k2 += 1
    print i, k1, k2