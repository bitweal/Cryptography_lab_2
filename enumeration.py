import threading

def time_limit_decorator(limit_minutes):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = [None] 

            def target():
                result[0] = func(*args, **kwargs)

            thread = threading.Thread(target=target)
            thread.start()
            thread.join(limit_minutes * 60) 

            if thread.is_alive():
                print('Функція перевищила ліміт часу')
                thread.join() 

            return result[0]

        return wrapper

    return decorator

@time_limit_decorator(5)
def discrete_logarithm_enumer(alpha, beta, p):
    for x in range(p - 1):
        if pow(alpha, x, p) == beta:
            return x
    return None

#p = int(input('Enter p: '))
#alpha = int(input('Enter alpha: '))
#beta = int(input('Enter beta: '))

#result = discrete_logarithm_enumer(alpha, beta, p)

#if result is not None:
#    print(f"Дискретний логарифм числа {beta} з основою {alpha} = {result}")
#else:
#    print(f"Дискретного логарифму не знайдено")
