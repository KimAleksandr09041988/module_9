def apply_all_func(int_list, *functions):
    dict_ = {}
    for function_ in functions:
        dict_[function_.__name__] = function_(int_list)
    return dict_

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))