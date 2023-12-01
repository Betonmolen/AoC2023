import re
def calibNumber(line):
    fNumb = ''
    lNumb = ''
    for i in line:
        try:
            fNumb = int(i)
            fNumb = i
            break
        except:
            pass
    line = line[:-1]
    for i in range(1,len(line)+1):

        try:
            # print(line[-i])
            lNumb = int(line[-i])
            lNumb = line[-i]
            break
        except:
            pass

    cNumber = int(fNumb + lNumb)
    # print(cNumber)
    return (cNumber)
def calibNumber2(line):
    fNumb = ''
    lNumb = ''
    fNumbindex = 0
    lNumbindex = 0
    word_2_num = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',

    }

    line = line[:-1]
    for i in range(1,len(line)+1):

        try:
            # print(line[-i])
            lNumb = int(line[-i])
            lNumb = line[-i]
            lNumbindex = line.find(i)
            break
        except:
            pass
    in_num = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))',line)
    try:
        fNumb = word_2_num[in_num[0]]
    except:
        fNumb = in_num[0]
    try:
        lNumb = word_2_num[in_num[-1]]
    except:
        lNumb = in_num[-1]

    cNumber = int(fNumb + lNumb)
    # print(cNumber)
    return (cNumber)

def main():
    filepath = "C:/Users\youri\Documents\Repos\AoC 2023\Day1\input.txt"
    # filepath = "C:/Users\youri\Documents\Repos\AoC 2023\Day1\example.txt"
    # filepath = "C:/Users\youri\Documents\Repos\AoC 2023\Day1\example2.txt"
    with open(filepath, 'r') as file:
        lines = file.readlines()
        cNumberTotal = 0
        cNumberTotal2 = 0
    for j in lines:
        tempCNumb = calibNumber(j)
        cNumberTotal += tempCNumb
    print(cNumberTotal)
    for j in lines:
        tempCNumb = calibNumber2(j)
        cNumberTotal2 += tempCNumb
    print(cNumberTotal2)




if __name__ == "__main__":
    main()
