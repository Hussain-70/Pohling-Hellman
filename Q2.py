
def CRT(vector):
    M = 1
    for num, mod in vector.items():
        M = M * mod
    ans = 0
    for num, mod in vector.items():
        m = (int(M / mod)) % mod
        ans = ans + (num * inverse(m, mod) * (int(M / mod)))
    return ans % M

def inverse(a, n):
    t = 0
    a = a % n
    newt = 1
    r = n
    newr = a
    while newr != 0:
        quotient = int(r / newr)
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if t < 0:
        t = t + n
    return t


def findDiscreteLog(a, B, p):
    primes = prime_factors(p - 1)
    CRT_vector = {}
    for prime, power in primes.items():
        exp = 1
        x_list = []
        B_sub = B
        while exp <= power:
            q = int((p - 1) / pow(prime, exp))
            Bpow = pow(B_sub, q, p)
            apow = pow(a, int((p - 1) / prime), p)
            k = 0
            found = False
            while not found:
                if pow(apow, k, p) == Bpow:
                    x_list.append(k)
                    # Note that this only checks up to q - 1
                    found = True
                if not found:
                    k = k + 1
            B_sub = (B_sub * pow(inverse(a, p), k * pow(prime, exp - 1))) % p
            exp = exp + 1
        exp = 0
        ans_mod_prime = 0
        while exp < power:
            ans_mod_prime = ans_mod_prime + (pow(prime, exp) * x_list[exp])
            exp = exp + 1
        CRT_vector[ans_mod_prime % pow(prime, power)] = pow(prime, power)
    return CRT(CRT_vector)

def prime_factors(n):
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            try:
                factors[i] = factors[i] + 1
            except KeyError:
                factors[i] = 1
    if n > 1:
        try:
            factors[n] = factors[n] + 1
        except KeyError:
            factors[n] = 1
    return factors

if __name__ == '__main__':
    alpha = int(input("Enter the base: "));
    beta = int(input("Enter the beta value: "));
    prime = int(input("Enter the prime number: "));
    print('The answer is: '+ str(findDiscreteLog(alpha, beta, prime)))
