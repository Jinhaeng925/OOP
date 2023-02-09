from datetime import date
today = date.today()


class StudentClass:

    def __init__(self):
        self.__studentID = 0
        self.__studentName = ""
        self.__studentDOB = "1999-09-25"
        self.__studentClassification = ['F', 'S', 'Jr', 'Sr']

    def calc_studentAge(self):
        Age = today - self.__studentDOB
        print(Age)
