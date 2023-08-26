class Person:
    def __init__(self , name , age) -> None:
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Меня зовут {self.name} и мне {self.age} лет")

Person1 = Person("Толик" , 28)
Person2 = Person("Джо" , 80)
Person3 = Person("Боба" , 14)

Person1.introduce()
Person2.introduce()
Person3.introduce()