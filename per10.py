# -*- coding:utf-8 -*-

import glob
import chardet
import codecs
# import io

# 変換前の文字コード
# src_codec = codecs.lookup("shift_jis") 
# src_codec = codecs.lookup("ISO-8859-1")

# 変換後の文字コード
# dest_codec = codecs.lookup("utf_8") 



# try:
#     f = open(k,"r",encoding='utf-8')
# except UnicodeDecodeError:#機能していない...?
#     print("erorr")
#     f = open(k,"r",encoding='ISO-8859-1')
                    
                    
    
def main():

    for i in glob.glob("./RxData/*"):
        for j in glob.glob(i+"/*"):
            for k in glob.glob(j+"/*"):
                
                with open(k, 'rb') as f:
                    b = f.read()
    
                    print(k)
                    
                if not(chardet.detect(b)['encoding'] == "ascii"):
                    # codecConvert(b)
                    continue
                
                f = open(k,"r",encoding='utf-8')
                
                data = f.readlines()
                list = calculate(data)
                f.close()
                f = open(k,"w")
                input(list,f)
                f.close()


    
def calculate(data):
    count = 0
    c = 0
    timeRange = [0,9]
    rxAverage = 0
    perTime = []
    
    calculatedList = []
    
    for i in range(len(data)):
        if not(data[i][0].isdecimal()):
        # if not(data[i][0].isdigit()):
            c += 1
            continue
        if(i == len(data) - c):
            break

        pickedData = data[i].split(',')
        pickedTime = pickedData[0].split(':')
        
        pickedData[1] = pickedData[1].replace('\n',"")
        if pickedData[1] == "(SNMP no response)":
            continue
        rxAverage += int(pickedData[1])
        count += 1
        
        if((i == 2 and c != 0) or (i == 0 and c == 0)):
            rxAverage = round(rxAverage / count)
            calculatedList.append(pickedData[0]+','+str(rxAverage))
        
        if not(timeRange[0] <= int(pickedTime[2]) <= timeRange[1]):
            rxAverage = round(rxAverage / count)
            count = 0
            if count == 0:
                perTime = pickedData[0]
            calculatedList.append(perTime+','+str(rxAverage))
            
            rxAverage = 0
                
            if timeRange[1] == 59:
                timeRange = [0,9]

            else:
                timeRange[0] += 10
                timeRange[1] += 10
    c = 0
    return calculatedList


def codecConvert(b):
    # print(b.encode('ISO-8859-1').decode('utf-8'))
    for i in range(len(b)):
        print(b[i].encode('ISO-8859-1').decode('utf-8'))
    # length = len(b)
    # for i in range(length):    
    #     print(b[i])
    #     b[i] = b[i].decode('utf-8')
    #     print(b[i]+"==================================")


def timeRange():
    pass


def input(list,f):
    length = len(list)
    for i in range(length):
        f.write(list[i]+'\n')
    
if __name__ == "__main__":
    main()