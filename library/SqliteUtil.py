import sqlite3
from Reflection import Reflection, ReflectionUtil

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


class SqliteUtil:
    def __init__(self, databaseName: str) -> None:
        self.databaseName = databaseName

        self.handlerDatabaseName(self.databaseName)
        self.conn = sqlite3.connect(self.databaseName)

    def handlerDatabaseName(self, databaseName):
        if not databaseName.endswith(".db") or not databaseName.endswith(".sqlite3"):
            self.databaseName += ".sqlite3"

    def execute(self, sql: str, isReturn=False):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        if isReturn:
            result = cursor.fetchall()
            cursor.close()
            return result

        cursor.close()
        return True

    def commit(self):
        self.conn.commit()


class t_user:
    username:str
    password:str
    age:int
    sex:bool = False

    def meta():
        tableName = ""

'''
# 连接数据库
su = SqliteUtil(r"../data/db")

# 创建表格
su.load(t_user)

# 查数据

'''


if __name__ == "__main__":
    s = SqliteUtil(r"../data/db")

    # 创建表格
    SQL.createTable("t_user", username="TEXT", password="TEXT", age="INT")

    # 查数据
    SQL.select("t_user")
