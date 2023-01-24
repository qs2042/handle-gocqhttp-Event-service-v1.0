from library.SqliteUtil import POJO, POJOField

class t_user(POJO):
    def __init__(self) -> None:
        self.id = POJOField.integerField()
        self.username = POJOField.charField(20)
        self.password = POJOField.charField(20)
        self.age = POJOField.integerField()
        self.sex = POJOField.tinyInt(1)
        super().__init__()

class t_lv(POJO):
    def __init__(self) -> None:
        self.userId = POJOField.integerField()
        self.lv = POJOField.integerField()
        super().__init__()