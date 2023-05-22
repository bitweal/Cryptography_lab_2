def discrete_logarithm_enumer(alpha, beta, p):
    for x in range(p - 1):
        if pow(alpha, x, p) == beta:
            return x
    return None

p = int(input('Enter p: '))
alpha = int(input('Enter alpha: '))
beta = int(input('Enter beta: '))

result = discrete_logarithm_enumer(alpha, beta, p)

if result is not None:
    print(f"Дискретний логарифм числа {beta} з основою {alpha} = {result}")
else:
    print(f"Дискретного логарифму не знайдено")
