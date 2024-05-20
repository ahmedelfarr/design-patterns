class singleton(object):
    def __new__(cls):
        if not hasattr(cls , 'instance'):
            cls.instance = super(singleton , cls).__new__(cls)
        return cls.instance
s = singleton()
print("object created",s)

s1 = singleton()
print("object created",s1)
