class SimpleBuilder(object):

    def __init__(self):
        pass

    def add(self, num1 = 2, num2 = 4):
        return num1 + num2

if __name__ == "__main__":
    s = SimpleBuilder()
    print(s.add(1,2))