"""
用装饰器代替配置文件，实现路由注册
"""


class App(object):
    def __init__(self):
        self.routers = {}

    def route(self, url):
        def register(fn):
            self.routers[url] = fn
            return fn

        return register


app = App()


@app.route("/")
def index(): pass

@app.route("/help")
def help(): pass


print(app.routers)
