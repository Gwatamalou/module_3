def sum_element(args, summ = 0):
    for i in args:

        if isinstance(i, int):
            summ += i

        elif isinstance(i, str):
            summ += len(i)

        elif isinstance(i, dict):
            summ = sum_element(list(i.items()), summ)

        else:
            summ = sum_element(i, summ)
    return summ


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(sum_element(data_structure))
