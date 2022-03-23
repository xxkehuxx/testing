points = [(20, 20), (40, 40), (45, 35), (21, 21)]
clust_num = 2

import itertools

def cluster(points, n):
    ans = []
    for i in itertools.combinations(points, 2):
        ans.append(((((i[0][0] - i[1][0])**2 + (i[0][1] - i[1][1])**2)**0.5),i))
    av = sum([i[0] for i in ans])/len([i[0] for i in ans])
    ans = sorted(ans)
    return [ans[0][1],ans[1][1]]

