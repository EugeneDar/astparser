class Result:
    def __init__(self, a, b, c, size):
        self.a = a
        self.b = b
        self.c = c
        self.size = size


f = open("../test/results.txt", "r")

min_size = 10 ** 1
max_size = 10 ** 3

g_if = []
g_loop = []
g_linear = []

while True:
    line = f.readline()
    if not line:
        f.close()
        break

    args = line.split(' ')
    res = Result(float(args[0]), float(args[1]), float(args[2]), float(args[3]))
    if min_size <= res.size < max_size:
        g_if.append(res.a)
        g_loop.append(res.b)
        g_linear.append(res.c)

g_if.sort()
g_loop.sort()
g_linear.sort()

for i in range(len(g_if)):
    print('(' + str(g_linear[i]) + ', ' + str((i + 1) / len(g_if)) + ') ', end='')
