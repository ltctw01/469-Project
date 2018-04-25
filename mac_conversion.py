# CSE 469 Project Task 1, tool b
# mac_conversion

months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
AMPM = ['AM', 'PM']

# module
def timeconversion(timeStr):
    hexStr = timeStr[0:2]
    if hexStr != '0x':
        error()
    else:
        # str = 0x3a81, int() convert to 16 based integer 0x3181, bin() convert to binary, zfill fill it to 16 bit.
        timeStr = bin(int(timeStr, 16))[2:].zfill(16)
        hourStr = timeStr[0:5]
        minStr = timeStr[5:11]
        secStr = timeStr[11:]

        hour = int(hourStr, 2)
        minute = int(minStr, 2)
        second = int(secStr, 2) * 2
        if hour > 12:
            hour = hour - 12
            AP = AMPM[1]
        elif hour == 12:
            AP = AMPM[1]
        else:
            AP = AMPM[0]
        print "Time: " + hour.__str__() + ":" + minute.__str__() + ":" + second.__str__() + " " + AP


def dateconversion(dateStr):
    hexStr = dateStr[0:2]
    if hexStr != '0x':
        error()
    else:
        # str = 0x3a81, int() convert to 16 based integer 0x3181, bin() convert to binary, zfill fill it to 16 bit.
        dateStr = bin(int(dateStr, 16))[2:].zfill(16)
        yearStr = dateStr[0:7]
        monthStr = dateStr[7:11]
        dayStr = dateStr[11:]

        year = int(yearStr, 2) + 1980
        month = months[int(monthStr, 2)]
        day = int(dayStr, 2)

        print "Date: " + month + " " + day.__str__() + ", " + year.__str__()

# read file
def readfile(str):
    f = open(str, 'r')
    line = f.read()
    return line


# input format error
def error():
    print("Please enter valid input:")
    print("-T|-D [-f filename | -h hex_value]")


# main function
while True:
    converString = raw_input()
    # length check
    if len(converString) <= 5:
        error()
        continue

    # read file check
    readFileStr = converString[2:5]
    if readFileStr == ' -h':
        str = converString[6:]
    elif readFileStr == ' -f':
        str = readfile(converString[6:])
    else:
        error()
        continue

    # module check
    moduleStr = converString[0:2]
    if moduleStr == '-T':
        timeconversion(str)
    elif moduleStr == '-D':
        dateconversion(str)
    else:
        error()
