import time
from a3 import *

f = open("test.txt", "r")
g = open("output.txt", "r")
# print(f.readlines())
m = g.readlines()


def checker(f, m):
    t = time.time()

    for i in f.readlines():

        database = PointDatabase(eval(i)[0])
        n = len(eval(i)[1])

        out = []
        for j in range(n):
            k = database.searchNearby(eval(i)[1][j][0], eval(i)[1][j][1])
            out.append(k)
    print("--- %s seconds ---" % (time.time() - t))
    for j in range(len(out)):
        ur = out[j]

        our = eval(m[0])[j]
        ur.sort()
        our.sort()
        if ur != our:
            print("You fucked up bro", j)
            return

    print("you did it my man")


checker(f, m)

f.close()
g.close()
