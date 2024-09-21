
def is_prime(func):
    def wrapper(*args):
        fn_sum = sum(args)
        count = 0
        for x in range(2, fn_sum - 1):
            if (fn_sum % x == 0):
                count += 1
        if (count <= 0):
            return f'Простое \n {fn_sum}'
        else:
            return f'Составное \n {fn_sum}'
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)