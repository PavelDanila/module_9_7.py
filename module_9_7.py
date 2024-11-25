def is_prime(func):
    def wrapper(a, b, c):
        result_1 = func(a, b, c)
        if result_1 > 1:
            for n in range(2, result_1 - 1):
                if result_1 % n == 0:
                    print('Составное')
                    break
            else:
                print('Простое')
        else:
            print('Это не простое и не составное число')
        return result_1
    return wrapper

@is_prime
def sum_three(a, b, c):
    sum = int(a +b +c)
    return sum

result = sum_three(2, 3, 6)
print(result)
