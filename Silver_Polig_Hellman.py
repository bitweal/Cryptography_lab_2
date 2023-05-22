def canonical_decomposition(n):
    prime_factors = []
    powers = []
    
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            prime_factors.append(i)
            power = 0
            while n % i == 0:
                n //= i
                power += 1
            powers.append(power)
    
    if n > 1:
        prime_factors.append(n)
        powers.append(1)
    
    return prime_factors, powers

def calculate_r_table(alpha, n, prime_factors):
    r_table = []
    for prime in prime_factors:
        r_row = []
        for j in range(prime):
            r = (alpha ** (n * j // prime)) % (n+1)
            r_row.append(r)
        r_table.append(r_row)
    return r_table