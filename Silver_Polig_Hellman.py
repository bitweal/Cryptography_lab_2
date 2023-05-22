import math

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

def calculate_x0(beta, n, prime):
    x0 = beta ** (n//prime)
    return x0 % (n+1)

def calculate_x(alpha, beta, prime, power, n, x_prev, r_table):
    suma = 0
    for i in range(1,power):
        alpha_power = 0
        for pj,xi  in enumerate(x_prev):
            if pj == 0:
                alpha_power += xi * -1
            else:
                alpha_power += xi * -1 * prime**pj
        print('alpha_power: ', alpha_power)
        print('alpha: ',pow(alpha, alpha_power, n+1))
        x = ((beta * pow(alpha, alpha_power, n+1))**(n//(prime**(i+1)))) % (n+1)
        print('x: ', x)
        x = r_table.index(x)
        x_prev.append(x) 
        suma += x     

    return suma

def solve_congruences(congruences):
    m = 1
    for modulus, _ in congruences:
        m *= modulus
    x = 0
    for modulus, residue in congruences:
        mi = m // modulus
        mi_inverse = pow(mi, -1, modulus)
        x += residue * mi * mi_inverse
    
    return x % m

def silver_polig_hellman(alpha, beta, n):
    prime_factors, powers = canonical_decomposition(n)
    print('canonical_decomposition - ', prime_factors, ' - ', powers)
    r_table = calculate_r_table(alpha, n, prime_factors)
    print('calculate_r_table - ', r_table)
    congruences = []
    
    for i, prime in enumerate(prime_factors):
        x0 = calculate_x0(beta, n, prime)
        x0 = r_table[i].index(x0)
        print('calculate_x0 - ', x0)
        x_prev = [x0]
        x = calculate_x(alpha, beta, prime, powers[i], n, x_prev, r_table[i])
        print('calculate_x - ', x)
        suma_x = x0 + x
    
    return solve_congruences(congruences)

n = int(input('Enter p: '))
alpha = int(input('Enter alpha: '))
beta = int(input('Enter beta: '))

x = silver_polig_hellman(alpha, beta, n)
if x is not None:
    print(f"Дискретний логарифм числа {beta} з основою {alpha} = {x}")
else:
    print(f"Дискретного логарифму не знайдено")