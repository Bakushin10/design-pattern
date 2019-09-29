"""
only one instance may exist at any given time
"""

class MySingleton(object):
    _instance = None
    def __new__(self):
        if not self._instance:
            self._instance = super(MySingleton, self).__new__(self)
            self.y = 10
        return self._instance

class Singleton_Lazy(object):
    __instance = None
    _num = 0
    def __init__(self):
        if not Singleton_Lazy.__instance:
            print("I have already got an instance")
        else:
            print("I do not yet have an instance")
    
    def getValue(self):
        self._num += 1
    
    @property
    def setnum(self, num):
        self._num = num	

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton_Lazy()
        return cls.__instance

class Singleton_Strict(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton_Strict, cls).__new__(cls)
        return cls.instance


sl = Singleton_Lazy()
sl2 = Singleton_Lazy()

print("{}, {}".format(sl.getInstance(), sl2.getInstance()))

ss = Singleton_Strict()
ss2 = Singleton_Strict()

print("{} {}".format(ss, ss2))

print("{}".format("*"*10))



x = MySingleton()
print(x.y)
x.y = 20
z = MySingleton()
print(z.y)