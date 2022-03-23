import math


def decompose(n):
    ef = []
    if len(n) < 2:
        return ef
    if n.find('.') > -1:
        n = float(n)
        nr = int(n * 1000)
        dr = 1000
    else:
        parts = n.rsplit('/')
        n = int(parts[0])/int(parts[1])
        nr = int(parts[0])
        dr = int(parts[1])

    if nr%dr == 0:
        return [str(math.ceil(nr/dr))]
    while nr != 0:
        x = math.ceil(dr/nr)
        ef.append(x)
        nr = x * nr - dr
        dr = dr * x
    ans = ['1/' + str(i) if i != 1 else '1' for i in ef]
    return ans


n = 0.989