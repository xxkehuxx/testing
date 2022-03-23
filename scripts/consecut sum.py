class PrimeFactorizer:
    def __init__(self, z):
        self.z=z
        self.factor = factor

    def primes(self,n):
        p=[]
        for a in range(2,n+1):
            if (self.is_prime(a)): p.append(a)
        return p

    def is_prime(self,number):
        for n in range(2,number):
            if not number%n : return False
        return True

    def factor(self):
        p=self.primes(self.z)
        fact={}
        if self.z in p:
            fact[self.z]=1
        else:
            for n in p:
                while self.z%n==0 and (self.z/n not in p):
                    if n not in fact: fact[n]=1
                    else: fact[n]+=1
                    self.z/=n
                if self.z%n==0 and (self.z/n in p):
                    if n in fact: fact[n]+=1+(self.z/n==n)
                    else:
                        fact[n]=1
                        fact[self.z/n]=1+(z/n==n)
                    break
        return print(fact)


PrimeFactorizer(100,2).factor