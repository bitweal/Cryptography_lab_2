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
            r = (alpha ** ((n-1) * j // prime)) % (n)
            r_row.append(r)
        r_table.append(r_row)
    return r_table

def calculate_x0(beta, n, prime):
    x0 = beta ** ((n-1)//prime)
    return x0 % n

def calculate_x(alpha, beta, prime, power, n, x_prev, r_table):
    suma = 0
    for i in range(1,power):
        alpha_power = 0
        for pj,xi  in enumerate(x_prev):
            if pj == 0:
                alpha_power += xi * -1
            else:
                alpha_power += xi * -1 * prime**pj
        x = ((beta * pow(alpha, alpha_power, n))**((n-1)//(prime**(i+1)))) % n
        x = r_table.index(x)
        x_prev.append(x) 
        suma += x * prime**i     

    return suma

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - (a // b) * y

def chinese_remainder_theorem(suma_x, module):
    M = 1
    for num in module:
        M = lcm(M, num)

    result = 0

    for a_i, n_i in zip(suma_x, module):
        b_i = M // n_i
        _, b_i_inv, _ = extended_gcd(b_i, n_i)
        result += a_i * b_i * b_i_inv

    return result % M

def silver_polig_hellman(alpha, beta, n):
    prime_factors, powers = canonical_decomposition(n-1)
    r_table = calculate_r_table(alpha, n, prime_factors)
    module = []
    suma_x = []
    for i, prime in enumerate(prime_factors):
        x0 = calculate_x0(beta, n, prime)
        x0 = r_table[i].index(x0)
        x_prev = [x0]
        x = calculate_x(alpha, beta, prime, powers[i], n, x_prev, r_table[i])
        module.append(prime**powers[i])
        suma_x.append(x0 + x)
    
    return chinese_remainder_theorem(suma_x, module)

#n = int(input('Enter p: '))
#alpha = int(input('Enter alpha: '))
#beta = int(input('Enter beta: '))

#x = silver_polig_hellman(alpha, beta, n)
#if x is not None:
#    print(f"Дискретний логарифм числа {beta} з основою {alpha} = {x}")
#else:
#    print(f"Дискретного логарифму не знайдено")