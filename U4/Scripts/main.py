#Global Variables
a = "Text"
b = 1
c = [1, 2, 3, 4]
d = {1: "One"}
e = True

def CreateLogEvent(n):
    """
    Author: Darius Pasoch
    Date: 26/10/26
    params: n not defined | all types accepted

    descript: This function creates a log event for the application
    """

    print("==== LOGS ====")
    print("==== DUMMY DATA ====")

    print(type(n))

    return f" \n ==== LOGs ==== \n ==== DUMMY DATA ==== \n Type of n: {type(n)} \n "

def a():
    print('a')
    return ' \n a'