def func(data):
    print(data)
    print(id(data))
    # data.append('23')  # append 和 += 都不会创建新对象，
    # data += ['23']
    data = data + ['23']  # 这种写法，左边的data已经是一个新建的局部变量对象了,
    print(id(data))
    print(data)


if __name__ == '__main__':

    data = [12, 45, 89]
    func(data)
    print(data)
    print(id(data))
