from datetime import date, datetime
class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    def get_age(self):
        return datetime.now().year - self.birthday.year

    # 将age变为属性描述符
    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value


if __name__ == "__main__":
    user = User("bobby", date(year=1987, month=1, day=1))
    # print("in {} file".format(__file__))
    # print(user.get_age())
    print(user.age)





























