class Bug(object):
    legs = 0 # 类属性
    distance = 0

    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def walk(self):
        # self.distance += 1
        Bug.distance += 1

    def ToString(self):
        return self.name + " has " + str(self.legs) + " legs" + \
            " and taken " + str(self.distance) + " steps."

bug = Bug("clarence", 2)
print(bug.ToString())