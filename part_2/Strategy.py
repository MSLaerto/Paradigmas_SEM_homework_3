#Реализуйте паттерн Стратегия на языке Python для сортировки списка чисел. Создайте класс SortStrategy, имеющий метод sort(numbers),
#и несколько конкретных стратегий для различных методов сортировки (например, пузырьковая сортировка, сортировка выбором).


class Strategy:
    def sort(self) -> None:
        pass

class SortStrategy(Strategy):
    def sort(self , numbers) -> str:
        return sorted(numbers)

class SelectionSort(Strategy):
    def sort(self,alist):
        for i in range(0, len(alist) - 1):
            smallest = i
            for j in range(i + 1, len(alist)):
                if alist[j] < alist[smallest]:
                    smallest = j
            alist[i], alist[smallest] = alist[smallest], alist[i]
        return alist    

class BubbleSort(Strategy):
    def sort(self , nums):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True
        return nums            

numbers = [17, 63, 95, 13, 74, 31, 33, 42, 68, 66]

class Sorter:
    strategy: Strategy 
    def __init__(self, strategy: Strategy = None) -> None:
        self.strategy = strategy
   
    def Choser(self):
        if self.strategy == SortStrategy :
            print(SortStrategy.sort(self , numbers))
        elif self.strategy == SelectionSort :
            print(SelectionSort.sort(self , numbers))
        elif self.strategy == BubbleSort :
            print(BubbleSort.sort(self , numbers))
        else: 
            print("Такой сортировки нет")      

s1 = Sorter(SortStrategy)
Sorter.Choser(s1)
s2 = Sorter(SelectionSort)
Sorter.Choser(s2)
s3 = Sorter(BubbleSort)
Sorter.Choser(s3)