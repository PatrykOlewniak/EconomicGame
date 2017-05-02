from datetime import datetime



class IncomeCalculations:
    secondsInMonth = 2629744
    actualTime = datetime.now()


    def secondsCountFromDateToNow(self, startDate):
        """seconds count from begining to now"""
        actualTime=datetime.now()
        return (actualTime - startDate).total_seconds()

    def incomeInPeriod(self,salaryPerMonth,shift,startTime,endTime):
        """income in input period
            if endTime before now - calculate the income between dates
            but if endTime in future - calculates with time to now
        :return: income from startTime to endTime if endTime in the past, else : to now
        """
        secondsInMonth = 2629744
        _salaryPerSec=(salaryPerMonth*(shift/8))/secondsInMonth

        if (endTime>datetime.now()):
            return  (_salaryPerSec* self.secondsCountFromDateToNow(startTime))
        else:
            return(_salaryPerSec * (endTime-startTime).total_seconds())

    def secondsCountFromDateToDate(self,FirstDate,SecondDate):
        """
        :param FirstDate: format datetime (year-mm-dd-...)
        :param SecondDate: format datetime (year-mm-dd-...)
        :return: seconds from date to date, if secondDate before FirstDate then return negative count
        """
        """seconds count from dateA to DateB"""
        return ((SecondDate- FirstDate).total_seconds())