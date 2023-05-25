import threading
import time
from enumeration import discrete_logarithm_enumer
from Silver_Polig_Hellman import silver_polig_hellman

def timeit_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print("The function {} was executed in {:.2f} seconds".format(func.__name__, execution_time))
        return result
    return wrapper

@timeit_decorator
def run_function1(alpha, beta, p):
    global result1
    result1 = discrete_logarithm_enumer(alpha, beta, p)

@timeit_decorator
def run_function2(alpha, beta, p):
    global result2
    result2 = silver_polig_hellman(alpha, beta, p)

for i in range(1,3):
    print(f'Задача {i} типу')

    p = int(input('Enter p: '))
    alpha = int(input('Enter alpha: '))
    beta = int(input('Enter beta: '))

    thread1 = threading.Thread(target=run_function1(alpha, beta, p))
    if result1 is not None:
        print(f"Дискретний логарифм числа {beta} з основою {alpha} = {result1}, перебором")
    else:
        print(f"Дискретного логарифму не знайдено")

    thread2 = threading.Thread(target=run_function2(alpha, beta, p))

    if result2 is not None:
        print(f"Дискретний логарифм числа {beta} з основою {alpha} = {result2}, за алгоритмом Сiльвера-Полiга-Геллмана")
    else:
        print(f"Дискретного логарифму не знайдено")

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()