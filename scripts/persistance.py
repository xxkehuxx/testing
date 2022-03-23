def razdel(i):
    ans = [int(i) for i in str(i)]
    prod = 1
    for i in ans:
        prod *= i
    return prod

def persistence(n):
    c = 0
    while n >= 10:
        n = razdel(n)
        c += 1
    return c


x = 'man i need a taxi up to ubud'
import string
def high(x):
    parts = x.split()
    al = string.ascii_lowercase
    scores = []
    ans=[]
    for index, part in enumerate(parts):
        for let in part:
            scores.append((al.index(let)+1,index))
    for x in range(len(parts)):
        ans.append(sum(int(value) for value,key in scores if key == x))
    ind = ans.index(sorted(ans)[-1])
    return parts[ind]




