import numpy as np

person_dtype = np.dtype({
    'names': ['name', 'age', 'a', 'b', 'c'],
    'formats': ['S64', 'i', 'i', 'i', 'f']
})

person = np.array([('abc', 13, 98, 98, 99.3),
                   ('edf', 14, 97, 80, 100)],
                  dtype=person_dtype)

print(person[:]['age'])
a = person[:]['a']
print(a)
print('a 的平均值:', np.mean(a))
