#Создайте класс Coffee с методом cost(), возвращающим стоимость кофе. Реализуйте декораторы Sugar и Milk, которые добавляют сахар и молоко к кофе, соответственно.
#Создайте объект кофе и последовательно примените к нему декораторы, затем выведите общую стоимость.

class Coffee:
   price = 50
   def cost(price):
      return price
class Sugar(Coffee):
    def AddSugar(self):
        Coffee.price += 10
        return Coffee 
class Milk(Coffee):
   def AddMilk(self):
        Coffee.price += 15
        return Coffee 

print("Стоимость кофе 50 , сахара 10 , молока 15")    
Coffee1 = Coffee
print(Coffee1.price)
Coffee1 = Milk.AddMilk(Sugar.AddSugar(Coffee1))
print(Coffee1.price)