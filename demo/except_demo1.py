"""
即使在try语句块内执行return、break等逻辑跳转指令，解释器也会确保finally被执行
"""
def test(value):
    try:
        result = 1 / value
        print('right')
        return result
    except Exception as exc:
        print('error')
        return 'except Exception'
    finally:
        print('finally')


test(1)
test(0)
