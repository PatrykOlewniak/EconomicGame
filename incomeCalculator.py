from datetime import datetime

secondsInMonth=2629744
actualTime=datetime.now()

class IncomeCalculations:


    def totalAmount(self,incomeList):
        """zwraca sume zarobkow. Jako wejscie wymaga listy w formie [salaryPerMonth,startTime,EndTime]"""
        totalIncome=0
        for k in incomeList:
            totalIncome+=self.incomeInPeriod(k[0],k[1],k[2])
        return totalIncome

    def secondsCountFromDateToNow(self, startDate):
        """Sekundy od startu do teraz"""
        actualTime=datetime.now()
        return (actualTime - startDate).total_seconds()

    def incomeInPeriod(self,salaryPerMonth,shift,startTime,endTime):
        """Zarobek do danej daty. Jesli data w przyszlosci to zwraca do teraz"""
        secondsInMonth = 2629744
        _salaryPerSec=(salaryPerMonth*(shift/8))/secondsInMonth

        if (endTime>datetime.now()): #unikniecie formatowania
            return  (_salaryPerSec* self.secondsCountFromDateToNow(startTime))
        else:
            return(_salaryPerSec * (endTime-startTime).total_seconds())

    def secondsCountFromDateToDate(self,FirstDate,SecondDate):
        """Zwraca liczbe sekund od daty A do daty B"""
        return ((SecondDate- FirstDate).total_seconds())



