def fib_seq(n):
    ans = [0,1]
    i=0
    while ans[-1] < n:
        ans.append(ans[i] + ans[i+1])
        i += 1
    return ans

def productFib(prod):
    root = math.ceil(prod**(1/2))
    seq = fib_seq(root)
    if prod == 1:
        return [1, 1, True]
    if seq[-1]*seq[-2] == prod:
        return [seq[-2],seq[-1], True]
    if seq[-1]*seq[-2] < prod:
        return [seq[-1],seq[-1]+seq[-2], False]
    return [seq[-2], seq[-1], False]


def productFib(prod):
    a,b = 0,1
    while prod > a*b:
        a,b = b, a+b
    return [a,b,prod == a*b]




