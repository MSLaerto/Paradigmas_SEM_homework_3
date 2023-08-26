#Создайте класс ElectricSocket, который имеет метод supply_electricity(voltage). Реализуйте класс USPlugAdapter, 
#который адаптирует розетку стандарта США к европейскому стандарту. Создайте объекты и продемонстрируйте передачу электроэнергии через адаптер.

class ElectricSocet:
    def supply_electricity(self , US_voltage , US_ampers):
        print(f"Текущее напряжение : {US_voltage} B , сила тока : {US_ampers} А, частота : 50 Гц")
        USPlugAdapter.Adapter(US_voltage , US_ampers)


class USPlugAdapter(ElectricSocet):
    def Adapter(US_ampers,US_voltage):
        EU_ampers = US_ampers*US_voltage/220
        print(f"Новое напряжение   : 220 B , сила тока : {round(EU_ampers , 3)} А, частота : 60 Гц\n")
        
US_electricity = ElectricSocet()


US_electricity.supply_electricity(110, 6)
US_electricity.supply_electricity(127, 5)
US_electricity.supply_electricity(114, 12)
US_electricity.supply_electricity(110, 35)