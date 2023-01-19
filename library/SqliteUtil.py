import sqlite3
from Reflection import Reflection, ReflectionUtil, types

class SQL:
    def __init__(self, sql):
        self.raw = sql

    @staticmethod
    def createTable(tableName: str, **kwargs):
        return SQL(f"CREATE TABLE {tableName} ({', '.join([f'{i} {kwargs.get(i)}' for i in kwargs])})")

    @staticmethod
    def insert(tableName: str, **kwargs):
        return SQL("")

    @staticmethod
    def delete(tableName: str, **kwargs):
        return SQL("")

    @staticmethod
    def update(tableName: str, **kwargs):
        return SQL("")

    @staticmethod
    def select(tableName: str, **kwargs):
        return SQL("")


class Wrapper:
    __sql = "where"

    def eq(self, k, v):
        self.__sql += f" {k}={v}"
        return self
    
    def conn_or(self): 
        self.__sql += " or"
        return self

    def conn_and(self): 
        self.__sql += " and"
        return self

    
    def result(self):
        return self.__sql



class SqliteUtil:
    def __init__(self, databaseName: str, module: types.ModuleType) -> None:
        # 数据库名称
        self.databaseName = self.__handlerDatabaseName(databaseName)

        # 数据库连接
        self.conn = sqlite3.connect(self.databaseName)

        # 配置
        self.config = self.__config()

    def __handlerDatabaseName(self, databaseName: str) -> str:
        '''处理数据库名'''
        if not databaseName.endswith(".db") or not databaseName.endswith(".sqlite3"):
            return databaseName + ".sqlite3"
        return databaseName

    def __config(self) -> dict:
        '''加载配置'''
        return {
            "global_flag_name": "status",
            "use_flag": False
        }

    def __generateTable(self, cla): 
        r = Reflection(cla)

    def execute(self, sql: str, isReturn=False):
        '''执行SQL'''
        cursor = self.conn.cursor()
        cursor.execute(sql)
        if isReturn:
            result = cursor.fetchall()
            cursor.close()
            return result

        cursor.close()
        return True

    def commit(self):
        '''提交'''
        self.conn.commit()

    
    def insert(self, pojo):
        pass
    
    def delete(self, tableName: str, wrapper: Wrapper=None):
        pass

    def update(self, pojo, wrapper: Wrapper=None):
        pass
    
    def select(self, tableName, wrapper: Wrapper=None):
        if wrapper == None: return f"select * from {tableName}"

        return f"select * from {tableName} {wrapper.result()}"
    
    
class POJO:
    def __init__(self) -> None:
        self.config = {
            # 表格名(不填的话为类名)
            "tableName": "",

            # 是否为临时表(断开链接即销毁)
            "isTemp": "",
        }

    @staticmethod
    def charField(max_length=255):
        return f"VARCHAR({max_length})"

    @staticmethod
    def integerField():
        return "INT"

    @staticmethod
    def tinyInt(val):
        return f"TinyInt({val})"

    def get(): pass
    def save(): pass
    def remove(): pass

class t_user(POJO):
    def __init__(self) -> None:
        super().__init__()
    
    username = POJO.charField(20)
    password = POJO.charField(20)
    age = POJO.integerField()
    sex = POJO.tinyInt(1)

# 方案1
'''
# 连接数据库(如果数据库不存在, 则根据models.py中的POJO子类, 自动转化为数据库表格)
su = SqliteUtil(r"../data/db", "models.py")

# 增
u = t_user()
u.username = "admin"
u.password = "admin"
su.insert(u)

# 删
su.delete("t_user", Wrapper().eq("username", "admin").conn_and().eq("password", "root"))

# 改
u.age = 114
su.update(u, Wrapper())

# 查
su.select("t_user", Wrapper().eq("username", "admin").conn_or().eq("password", "admin"))
'''

# 方案2
'''
# 连接数据库(如果数据库不存在, 则根据models.py中的POJO子类, 自动转化为数据库表格)
su = SqliteUtil(r"../data/db", "models.py")

user = t_user()

# 增
user.username = "admin"
user.password = "admin"
user.save()

# 删
user.remove(Wrapper().eq("username", "admin").conn_and().eq("password", "root"))

# 改
user.age = 114
user.save(features='id')
user.save(features='username')

# 查
su.get(Wrapper().eq("username", "admin").conn_or().eq("password", "admin"))
'''

if __name__ == "__main__":
    # 连接数据库(如果数据库不存在, 则根据models.py中的POJO子类, 自动转化为数据库表格)
    su = SqliteUtil(r"../data/db", "models.py")

    # 增
    u = t_user()
    u.username = "admin"
    u.password = "admin"
    su.insert(u)

    # 删
    su.delete("t_user", Wrapper().eq("username", "admin").conn_and().eq("password", "root"))

    # 改
    u.age = 114
    su.update(u, Wrapper())
    
    # 查
    su.select("t_user", Wrapper().eq("username", "admin").conn_or().eq("password", "admin"))
