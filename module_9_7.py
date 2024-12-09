def is_prime(func):
    def wrapper(*args):
        bool_ = True
        sum_ = func(*args)
        if sum_ <= 1:
            print("Ошибка")
        else:
            for i in range(2, sum_):
                if sum_ % i == 0:
                    bool_ = False
                    break
            if bool_:
                print("Простое")
            else:
                print("Сложное")
        return sum_
    return wrapper

@is_prime
def sum_three(*args, **kwargs):
    return sum(args)



result = sum_three(2, 3, 6)
print(result)
