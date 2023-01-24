'''
# 方案1
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

# 方案2

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

import sqlite3, os, importlib, sys
from library.Reflection import Reflection

class Wrapper:
    def __init__(self) -> None:
        self.__list = []
        self.__symbol = ""
    
    def __updateSymbol(self, k):
        d = {
            # 等于, 不等于
            # 大于, 大于等于
            # 小于, 小于等于
            "eq": "=", "ne": "<>",
            "gt": ">", "ge": ">=",
            "lt": "<", "le": "<=",

            # 范围
            "between": "BETWEEN", "notBetween": "NOT BETWEEN",

            # 匹配
            "like": "LIKE", "notLike": "NOT LIKE",

            # null
            "isNull": "IS NULL", "isNotNull": "IS NOT NULL",

            # 或, 且
            "or": "OR", "and": "AND", 
        }
        self.__symbol = d.get(k)

    def __handler(self, k, v):
        self.__list.append(f"{k}{self.__symbol}{v}")

    # 等于
    def eq(self, k, v):
        self.__updateSymbol("eq")
        self.__handler(k, v)
        return self
    
    # 不等于
    def ne(self, k, v):
        self.__updateSymbol("ne")
        self.__handler(k, v)
        return self
    
    # 大于
    def gt(self, k, v):
        self.__updateSymbol("gt")
        self.__handler(k, v)
        return self
    
    # 大于等于
    def ge(self, k, v):
        self.__updateSymbol("ge")
        self.__handler(k, v)
        return self
    
    # 小于
    def lt(self, k, v):
        self.__updateSymbol("lt")
        self.__handler(k, v)
        return self
    
    # 小于等于
    def le(self, k, v):
        self.__updateSymbol("le")
        self.__handler(k, v)
        return self
    
    # 范围
    def between(self, k, v1, v2):
        self.__updateSymbol("between")
        self.__list.append(f"{k} {self.__symbol} {v1} and {v2}")
        return self
    def notBetween(self, k, v1, v2):
        self.__updateSymbol("notBetween")
        self.__list.append(f"{k} {self.__symbol} {v1} and {v2}")
        return self
    
    # 匹配
    def like(self, k, v, mode=0):
        if mode==0: v = f"{v}%"
        if mode==1: v = f"%{v}"
        if mode==2: v = f"%{v}%"
        self.__updateSymbol("like")
        self.__list.append(f"{k} {self.__symbol} {v}")
        return self
    def notLike(self, k, v, mode=0):
        if mode==0: v = f"{v}%"
        if mode==1: v = f"%{v}"
        if mode==2: v = f"%{v}%"
        self.__updateSymbol("notLike")
        self.__list.append(f"{k} {self.__symbol} {v}")
        return self
    
    # NULL
    def isNull(self, k):
        self.__updateSymbol("isNull")
        self.__list.append(f"{k} {self.__symbol}")
        return self
    def isNotNull(self, k):
        self.__updateSymbol("isNull")
        self.__list.append(f"{k} {self.__symbol}")
        return self

    # 或
    def _or(self): 
        self.__updateSymbol("or")
        self.__list.append(self.__symbol)
        return self

    # 且
    def _and(self): 
        self.__updateSymbol("and")
        self.__list.append(self.__symbol)
        return self
    
    
    def result(self):
        l = self.__list
        if len(l) == 0: return ""

        where = " ".join(l)
        self.__list = []
        return f"where {where}"

class POJOMeta:
    def __init__(self) -> None:
        # 表格名(不填的话为类名)
        self.tableName: str = ""

        # 是否为临时表(断开链接即销毁)
        self.isTempTable: bool = False

        # 字段
        self.fields = {}
    
    def __repr__(self) -> str:
        return str(self.__dict__)
    
class POJOField:
    @staticmethod
    def charField(max_length=255):
        return f"VARCHAR({max_length})"

    @staticmethod
    def integerField():
        return "INT"

    @staticmethod
    def tinyInt(val):
        return f"TinyInt({val})"

class POJO:
    def __init__(self) -> None:
        self._meta = POJOMeta()
        self.metaInit()

    def __repr__(self) -> str:
        return str(self.__dict__)
    
    def metaInit(self):
        # 加载表格名称
        self._meta.tableName = self.__class__.__name__

        # 加载字段属性
        r = Reflection(self)
        fields = r.public.get("variable")
        self._meta.fields.update(fields)
        for i in fields: r.setAttribute(i, None)
    
    def get(): pass
    def save(): pass
    def remove(): pass

class SqliteUtil:
    def __init__(self, databaseName: str, modelsPath: str = None) -> None:
        self.databaseName = databaseName
        self.modelsPath = modelsPath

        self.init()
    
    def init(self):
        '''初始化'''
        print("="*15)
        print("SqliteUtil v1.0")
        print("="*15)

        # 数据库名称
        self.databaseName = self.__handlerDatabaseName(self.databaseName)

        # 数据库是否为刚刚创建
        dbExists = True
        if not os.path.exists(self.databaseName):
            print("检测到数据库不存在, 正在自动创建中...")
            dbExists = False

        # 数据库连接
        self.conn: sqlite3.Connection = sqlite3.connect(self.databaseName)

        # 数据库不存在: 导入module, 初始化数据表
        if not dbExists:
            self.__generateTable()

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

    def __generateTable(self): 
        '''生成表格'''
        # 获取models包下的所有文件名称
        l = os.listdir(self.modelsPath)

        # 添加models包路径到环境变量(sys.path)里
        sys.path.append(self.modelsPath)

        # 导入models包下的所有py文件
        self.models = {}
        for i in l:
            # 如果后缀不是py, 那就直接跳过
            if i[-3:] != ".py": continue

            # 获取插件名称
            pluginName = i.split(".")[0]

            # 导入文件, 并解析models
            r = Reflection(importlib.import_module(pluginName))
            cla = r.obj
            models = r.public.get("class")

            # 删除POJO父类(TODO: 这里还要删除, 不是POJO子类的类)
            try: models.pop("POJO")
            except: models = {}
            
            # 加载
            self.models[pluginName] = {
                "class": cla,
                "models": models
            }
        
        # 根据models生成SQL语句
        for i in self.models:
            m: dict = self.models.get(i)["models"]

            for j in m:
                tableName = j
                pojo: POJO = m.get(j)
                sql = self.create(pojo())
                print(f"正在生成数据表 -> {tableName} -> {sql}")

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

    def close(self):
        self.conn.close()

    def create(self, pojo: POJO):
        kvList = []
        for i in pojo._meta.fields:
            kvList.append(f"{i} {pojo._meta.fields.get(i)}")
        sql = f"CREATE TABLE {pojo._meta.tableName} ({', '.join(kvList)})"

        return sql

    def insert(self, pojo: POJO):
        fields = pojo._meta.fields

        keys = []
        values = []
        for key in fields.keys():
            # 获取字段的value
            value = pojo.__dict__.get(key)

            # 如果value为空就直接下一轮
            if value == None: continue
            
            # 如果是字符串就加上双引号, 反之就str()
            if type(value) == str: value = f"'{value}'"
            else: value = str(value)

            keys.append(key)
            values.append(value)
        return f"INSERT INTO ({', '.join(keys)}) VALUES ({', '.join(values)})"
    
    def delete(self, pojo: POJO, wrapper: Wrapper=None):
        sql = f"DELETE FROM {pojo._meta.tableName}"
        if wrapper ==None: return sql
        return f"{sql} {wrapper.result()}"

    def update(self, pojo: POJO, wrapper: Wrapper=None):
        # 1.0 -> sql = f"update {pojo._meta.tableName} set " + ", ".join([f"{x}={pojo.__dict__[x]}" for x in pojo.__dict__])
        # 2.0 -> sql = f"update {pojo._meta.tableName} set " + ", ".join([f"{x}={pojo.__dict__[x]}" for x in pojo._meta.fields])
        
        sql = f"UPDATE {pojo._meta.tableName} SET "
        l = []
        for key in pojo._meta.fields:
            # 获取字段的value
            value = pojo.__dict__.get(key)

            # 如果value为空就直接下一轮
            if value == None: continue

            # 如果是字符串就加上双引号, 反之就str()
            if type(value) == str: value = f"'{value}'"
            else: value = str(value)

            l.append(f"{key}={value}")
        sql += ", ".join(l)

        if wrapper ==None: return sql
        return f"{sql} {wrapper.result()}"
    
    def select(self, pojo: POJO, wrapper: Wrapper=None):
        sql = f"SELECT * FROM {pojo._meta.tableName}"

        if wrapper == None: return sql
        return f"{sql} {wrapper.result()}"
