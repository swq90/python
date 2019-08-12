##元类对类创建和对象实例化有更多控制权，可用于创建单例
#控制类创建和初始化，元类会覆盖 __new__,__init__
#单例模式1

import sqlite3


class MetaSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton , cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

# class Logger(metaclass=MetaSingleton):
#     pass
#
#
# logger1 = Logger()
# logger2 = Logger()
# print(logger1, logger2)


db1 = Database().connect()
db2 = Database().connect()

print('DB1',db1)
print('DB2',db2)