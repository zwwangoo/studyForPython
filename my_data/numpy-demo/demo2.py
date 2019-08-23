import numpy as np

person_dtype = np.dtype({
    'names': ['name', 'chinese', 'english', 'math', 'total'],
    'formats': ['S64', 'i', 'i', 'i', 'i']
})
persons = np.array([('zf', 66, 65, 30, 0),
                    ('gy', 95, 85, 98, 0),
                    ('zy', 93, 92, 96, 0),
                    ('hz', 90, 88, 77, 0),
                    ('dw', 80, 90, 90, 0)
                    ], dtype=person_dtype)

name = persons[:]['name']
chinese = persons[:]['chinese']
english = persons[:]['english']
math = persons[:]['math']
persons[:]['total'] = chinese + english + math


def printf(li):
    print(np.mean(li), end='|')
    print(np.amin(li), end='|')
    print(np.amax(li), end='|')
    print(np.std(li), end='|')
    print(np.var(li))


print('学科名称|平均成绩|最小成绩|最大成绩|成绩方差|成绩标准差')
print('语文', end='|')
printf(chinese)
print('英语', end='|')
printf(english)
print('数学', end='|')
printf(math)

print(np.sort(persons, order='total'))
