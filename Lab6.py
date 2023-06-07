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
    def __init__(self,isTouchable=True,name="blank",isRepaired=False):
        self.isTouchable=isTouchable
        self.deviceName=name
        self.isRepaired=isRepaired
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
        self.LapTopArr=LapTop
        if (LapTop or SmartPhone):
            self.ComputerAmount= len(LapTop) if isinstance(LapTop[0], Computer) else len(SmartPhone)
        else:
            raise Exception("Пустой список!")
    def getAmount(self):
        return self.ComputerAmount
    def deleteLapTopByIndex(LapTop,index):
        return LapTop.pop(index)
    def SetLapTopStatus(self,isRepaired=False):
        deviceName=input ("Введите название ноутбука: ")
        print("Количество компьютеров в ремонте: ", self.ComputerAmount)
        for i in range(len(self.LapTopArr)):
            if (self.LapTopArr[i].deviceName.lower()==deviceName.lower()):
                self.LapTopArr[i].isRepaired=isRepaired
                print(f'Новый статус ноутбука "{self.LapTopArr[i].deviceName}": ', "Отремонтирован " if self.LapTopArr[i].isRepaired else "Нуждается в ремонте")
                if (isRepaired==True):
                    self.ComputerAmount= self.ComputerAmount - 1
                return self.ComputerAmount;
    def showRepairedLapTops(self):
        self.repairedArray=[]	
        for i in range (len(self.LapTopArr)):
            if (self.LapTopArr[i].isRepaired):
                self.repairedArray.append(self.LapTopArr[i])
        return len(self.repairedArray)


LapTop_arr=[LapTop() for _ in range(random.randint(1,50))]
LapTop_arr.append(LapTop(name="LapTop17"))
repairing=RepairDevice(LapTop_arr)
myWatch=SmartWatch('200mAh')
myUltraBook=UltraBook('700g','500$')

print(f"Характеристики моего ультрабука:\n\
Вес: {myUltraBook.getChars()['weight']}, Цена: {myUltraBook.getChars()['price']}")
print(f"Размер батареи моих часов: {myWatch.getBatterySize()}")

repairing.SetLapTopStatus(isRepaired=True)
print("Количество отремонтированных ноутбуков в данный момент: ",repairing.showRepairedLapTops())
print("Количество ремонтируемых ноутбуков в данный момент: "+ str(repairing.getAmount()))