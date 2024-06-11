def print_params(a=1, b='string', c=True):
    print(f'a: {a}\n b: {b}\n c: {c}')
    print()


value_list = [4, False, 'abc']
value_dict = {'a': 52, 'b': 'bac', 'c': False}
value_list_2 = [True, None]

#task_1
print_params()
print_params(4)
print_params('str', False, 4)
print_params((1, 2), 25, [1, 2, 3])


#task_2
print_params(*value_list)
print_params(**value_dict)

#task_3
print_params(*value_list_2, 42)