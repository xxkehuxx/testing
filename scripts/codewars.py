# maximum consecutive sum
#
def prime(n):
    if n <= 1:
        return False
    if n >= 2:
        for i in range(2, int(n ** 0.5) + 1):
            if not (n % i):
                return False
        return True


def prime_maxlength_chain(n):
    primes = [i for i in range(int(n)) if prime(i)]

    new = [primes[i:j] for i in range(len(primes)) for j in range(int(len(primes))) if
           sum(primes[i:j]) < n and prime(sum(primes[i:j]))]
    ans = sorted([[len(i), sum(i)] for i in new])
    if ans[-1][0] == ans[-2][0]:
        return [ans[-2][1], ans[-1][1]]
    return [ans[-1][1]]


# find outlier
#
def find_outlier(integers):
    evens = []
    odds = []
    for i in integers:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    if len(evens) < len(odds):
        return evens[0]
    return odds[0]


# next
#
def prime(n):
    if n <= 1:
        return False
    if n >= 2:
        for i in range(2, int(n ** 0.5) + 1):
            if not (n % i):
                return False
        return True


def prev_prime(n):
    n = n - 1
    while not prime(n):
        n = n - 1
    return n


def find_even(n):
    num = 0
    for i in str(n):
        if int(i) in [2, 4, 6, 8, 0]:
            num = num + 1
        pass
    return num


def get_primes_list(n):
    if n < 2:
        return []
    primes = [2]
    for i in range(3, n):
        sqroot = i ** 0.5
        for p in primes:
            if i % p == 0:
                break
            if p > sqroot:
                primes.append(i)
                break
    return primes


def f(n):
    primes = get_primes_list(n)
    evens = sorted([(find_even(i), i) for i in primes])
    return evens[-1][1]


#
#
n = '0.66'


def decompose(n):
    ans = []
    if n == '0':
        return (ans)

    if n.find('/') > 0:
        parts = n.rsplit('/')
        n = int(parts[0]) / int(parts[1])
    else:
        n = float(n)

    if (n >= 1) and (n % 1 == 0):
        return [str(n)]

    den = 2
    ostat = n
    while sum(ans) != n:
        if ostat >= 1 / den:
            ostat -= 1 / den
            ans.append(1 / den)
            den += 1
        else:
            den += 1
    return ["1/" + str(int(1 / i)) for i in ans]


#
#
#


def prime(n):
    if n <= 1:
        return False
    if n >= 2:
        for i in range(2, int(n ** 0.5) + 1):
            if not (n % i):
                return False
        return True


import re

eq = "-x^2+3x+4"
derivative(eq)

def derivative(eq):
    if eq.find('x') == -1:
        return '0'


    minusparts =[]
    plusparts = eq.split('+')
    for part in plusparts:
        if part.find('-') > -1:
            minusparts.append(part.split('-'))
            plusparts.remove(part)


    minusparts = [item for sublist in minusparts for item in sublist if item != '']
    for i in minusparts:
        if i.find('^') > -1:
            power = i[i.find('^') + 1]
            add_koef =[i[0] if i[0].isdigit() else 1]
            deriv_power = '-' + str(add_koef*int(power)) + 'x^' + str(int(power)-1)
        if (i.find('x') > -1) and (i.find('^') == -1):
            koef = '-' + i[i.find('x')-1]
            deriv_koef = koef
        pass

    for i in plusparts:
        if i.find('^') > -1:
            power_plus = i[i.find('^') + 1]
            deriv_power = power + 'x^' + str(int(power) - 1)
        if (i.find('x') > -1) and (i.find('^') == -1):
            koef_plus = i[i.find('x')-1]
            deriv_koef = koef_plus
        pass


    if (eq.find('^') == -1) and (eq.find('x') > -1):
        ans = deriv_koef
    else:
        ans = deriv_power +'+'+ deriv_koef


    ans = ans.replace('^1', '')
    ans = ans.replace('1x', 'x')
    return ans