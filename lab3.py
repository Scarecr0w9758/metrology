# Реализовать программу, которая должна находить все
# значения из заданного пользователем диапазона,
# которые не встречаются
# в качестве значений элементов массива p.
# Разделить На 4 ФУНКЦИИ:
# 1) вввод начала и конца диапазона 
# 2) берём один элемент массива и он сравнивает себя в диапазоне
# 3) запуск проги
# 4) функция которая вызовет много функций№2

def setInterval(start_interval, end_interval):
    start_interval = int(input("Введите начало диапазона: "))
    end_interval = int(input("Введите конец диапазона: "))
    return (start_interval,end_interval)

def checkOne(element, array,interval):
    if element not in array and element in interval:
        return True
    else:
        return False

def getCheckedArray(array,interval):
    returned_array=[]
    for elem in array:
        if (checkOne(elem,array,interval)):
            returned_array.append(elem)
    return returned_array

def main(array,start,end):
    return getCheckedArray(array,setInterval(start,end))
    
p_array=[]
start=0
end=0

print("Числа, входящие в диапазон которые не присутствуют в массиве: ", main(p_array,start,end))


