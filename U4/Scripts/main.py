logs = {"Key": "value"}

def CreateLogEvent(logs):
    """
    Author: Darius Pasoch
    Date: 26/10/26
    params: logs | Dict

    descript: This function creates a log event for the application
    """

    # print("==== LOGS ====")
    # print("==== DUMMY DATA ====")

    # print(type(n))

    # return f" \n ==== LOGs ==== \n ==== DUMMY DATA ==== \n Type of n: {type(n)} \n "

    logs["New Key"] = "New Value"
    return logs

def a():
    # print('a')
    return ' \n a'