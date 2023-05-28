import random

class Device ():
    def __init__(self, screenSize="13'3"):
        self.screenSize=screenSize
    def getScreenSize(self):
        return self.screenSize
    
class Computer(Device):
    def __init__(self):
        self.isOn = False
    def On(self):
        print("Устройство включено")
        self.isOn = True
        return self.isOn
    def Off(self):
        print("Устройство отключено")
        self.isOn = False
        return self.isOn


class LapTop (Computer):
    def __init__(self,isTouchable=True,name="blank-name"):
        self.isTouchable=isTouchable
        self.deviceName=name
    def getName(self):
        return self.deviceName

class UltraBook(LapTop):
    def __init__(self,weight="400kg",price='9999$'):
        self.weight=weight
        self.price=price
    def getChars(self):
        return {
        "weight" : self.weight,
        "price" : self.price}

class SmartPhone(Computer):
    def __init__(self, ChargerType):
        self.ChargerType = ChargerType
    def getChargerType(self):
        return self.ChargerType

class SmartWatch(SmartPhone):
    def __init__(self,batterySize='400mAh'):
        self.batterySize=batterySize
    def getBatterySize(self):
        return self.batterySize

class RepairDevice():
    def __init__(self, LapTop = [], SmartPhone=[]):
        if (LapTop or SmartPhone):
            self.ComputerAmount= len(LapTop) if isinstance(LapTop[0], Computer) else len(SmartPhone)
        else:
            raise Exception("Пустой список!")
    def getAmount(self):
        return self.ComputerAmount


LapTop_arr=[LapTop() for _ in range(random.randint(1,50))]
repairing=RepairDevice(LapTop_arr)
myWatch=SmartWatch('200mAh')
myUltraBook=UltraBook('700g','500$')

print(f"Характеристики моего ультрабука:\n\
Вес: {myUltraBook.getChars()['weight']}, Цена: {myUltraBook.getChars()['price']}")
print(f"Размер батареи моих часов: {myWatch.getBatterySize()}")


print("Количество ремонтируемых ноутбуков в данный момент: "+ str(repairing.getAmount()))