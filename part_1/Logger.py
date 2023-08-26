class Logger(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance
s = Logger()
print("Создаем первый объект", s)
s1 = Logger()
print("Создаем второй объект", s1) 
print (f"Являютсля ли объекты одинаковыми ? - {s is s1}")