from datetime import datetime
import re

def checkdate(date_str, valid_formatlist):
    retDate = False
    for format in valid_formatlist:
        try:
            retDate = datetime.strptime(date_str, format)
            valid = True
            break
        except ValueError:
            continue
    return retDate

def checkwithstrptime(test_str, format):
    res = True
    try:
        res = bool(datetime.strptime(test_str, format))
    except ValueError:
        res = False
    return res

def checkwithregex(test_str, pattern):
    res = re.match(pattern, test_str)    
    return res
    

if __name__ == '__main__':
    test_str = "28021993"
    format_list = ["%Y","%m %Y","%d%m%Y"]
    retDate = checkdate(test_str, format_list)
    print(f"date_str: {test_str} is valid: {bool(retDate)} --> datetime={retDate}")

    retdate2 = checkdate("2020", format_list)

    if retDate and retdate2:
        print(f"Ist {retDate} kleiner als {retdate2}?: ", retDate < retdate2)

    # test_str = '44-01-1997'
    # print("The original string is : ", test_str)
    # isvalid = checkwithstrptime(test_str, "%d-%m-%Y")  #%Y == 4 digits-number
    # print("Does date match format? : ", isvalid)

    # pattern_str = r'^\d{2}-\d{2}-\d{4}$'
    # isvalid = checkwithregex(test_str, pattern_str )
    # print("Does date match format? : ", isvalid, bool(isvalid))
#\b(0[1-9]|1[0-2])[-/](0[1-9]|[12]\d|3[01])[-/](19\d\d|20\d\d)\b