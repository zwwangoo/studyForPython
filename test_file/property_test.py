class Student(object):
    """
    属性函数(property)
    - 将类方法转换为只读属性
    - 重新实现一个属性的setter和getter方法
    @property本身又创建了另一个装饰器setter，负责把一个setter方法变成属性赋值
    """
    @property
    def birth(self):
        return self._birth
    
    @birth.setter
    def birth(self, value):
        self._birth = value
    
    @property
    def age(self):
        return 2018 - self._birth


if __name__ == "__main__":
    stu = Student()
    stu.birth = 1994
    print(stu.birth)
    print(stu.age)