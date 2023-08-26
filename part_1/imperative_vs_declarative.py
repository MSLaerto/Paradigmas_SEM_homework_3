# Поиск максимального значения в массиве . Декларативный стиль обращается к функции max(arr) , императивный стиль "вручную" перебирает все элементы в массиве
# и математически проверяет их . 
#
# Предпочтительнее декларативный стиль , так как его написание и выполнение быстрее (приблизительно 1.25с vs 3.41с на миллион выполнений)


import time as t 

array = [3, 6, 11, 2, 5, 3, 2, 1, 8, 3, 7, 9,3, 6, 11, 2, 5, 3, 2, 1, 8, 3, 7, 9,3, 6, 11, 2, 5, 3, 2, 1, 8, 3, 7, 9,3, 6, 11, 2, 5, 3, 2, 1, 28, 3, 7, 9,3, 6, 11, 2, 5, 3, 2, 1, 8, 3, 7, 9]


def imperative_max(array):
    max = array[0] 
    for i in range (0 , len(array)):
        if max < array[i]:
            max = array[i]
    return max

def declarative_max(array):
    return max(array)
print(imperative_max(array))
print(declarative_max(array))


start = t.time()
for i in range (1000000):
    imperative_max(array)
end = t.time()
print(1*(end-start))

start = t.time()
for i in range(1000000):
    declarative_max(array)
end = t.time()
print(1*(end-start))