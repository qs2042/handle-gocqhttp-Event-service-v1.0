


#====================================
# SqliteUtil
#====================================
# 连接数据库
from library.SqliteUtil import SqliteUtil, Wrapper
su = SqliteUtil(r"data/db", r"data/models")

# 创建实体类 并 创建实体类实例
from data.models import R
user = R.t_user()
lv = R.t_lv()

# 增(id=1, username=admin, password=admin, age=null)
user.username = "admin"
user.password = "admin"
insert = su.insert(user)

# 删(false)
delete = su.delete(
    user, 
    Wrapper()
        .eq("username", "admin")
        ._and()
        .eq("password", "root")
)

# 改(True)
user.age = 114
update = su.update(
    user, 
    Wrapper()
        .eq("id", "1")
)

# 查(id=1, username=admin, password=admin, age=114)
select = su.select(
    user, 
    Wrapper()
        .eq("username", "root")
        ._or()
        .eq("password", "root")
        ._or()
        .between("age", 10, 200)
)


print(f"""
test: 增删改查
{insert}
{delete}
{update}
{select}

""")

print(su.execute(insert, True))
su.commit()

su.close()


