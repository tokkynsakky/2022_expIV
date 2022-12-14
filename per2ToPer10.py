# -*- coding:utf-8 -*-

import glob
import chardet

# $ perl -i -pe 's/\R/\n/g' sample.txt             
    
def main():
    timeList = makeTimeList()
    
    for i in glob.glob("./RxData/*"):
        for j in glob.glob(i+"/*"):
            for k in glob.glob(j+"/*"):
                
                with open(k, 'rb') as f:
                    b = f.read()
                    print(k)
                    
                if not(chardet.detect(b)['encoding'] == "ascii"):
                    continue
                
                f = open(k,"r",encoding='utf-8')
                data = f.readlines()
                list = calculate(data,timeList)
                print(len(list))
                f.close()
                f = open(k,"w")
                input(list,f)
                f.close()
    
#時間の区切りを作成する関数
def makeTimeList():
    timeList = []
    value = [00,00,00]#hour:min:sec
    length = 8640
    
    for i in range(length):
        timeList.append([f'{value[0]:02}',':',f'{value[1]:02}',':',f'{value[2]:02}',',',f'{value[2]:02}'])
        
        #10秒おきの時間刻み　00:00:00 ~ 23:59:50まで 8640刻み
        if value[2] == 50:
            value[2] = 0
            value[1] += 1
            if value[1] == 60:
                value[1] = 0
                value[0] += 1
                if value[0] == 24:
                    break
        else:
            value[2] += 10
    return timeList


    
def calculate(data,timeList):
    calculatedList = []
    length = len(data)
    ran = range(length)
    index = 0
    nextHour = 360
    nextMin = 6
    stringRowCount = 0
    rx = 0
    n = 0
    count = 0
 
    for i in ran:
        #最初の文字が数字でない場合Continue
        if not data[i][0].isdigit():
            stringRowCount += 1
            continue
        if i == length - stringRowCount:
            break
        
        if index == len(timeList):
            break
        
        pickedData = data[i].split(",")[:2]
        pickedData[1] = pickedData[1].replace('\n',"")
        pickedTime = pickedData[0].split(":")

        if pickedData[1] == "(SNMP no response)":
            continue
        
        if int(timeList[index][0]) <= int(pickedTime[0]) < int(timeList[index+nextHour][0]):
            # print("timeList[index][0] = "+str(timeList[index][0])+" index = "+str(index))
            # print("int(pickedTime[0]) = "+str(int(pickedTime[0])))
            # print("int(timeList[index+nextHour][0]) = "+str(int(timeList[index+nextHour][0]))+" index+nextHour = "+str(index+nextHour))
            # print("")
            if int(timeList[index][2]) <= int(pickedTime[1]) < int(timeList[index+nextMin][2]):
                if int(timeList[index][4]) <= int(pickedTime[2]) <= int(timeList[index][4]) + 9:
                    rx += int(float(pickedData[1]))
                    n += 1
                else:
                    if n == 0:
                        timeList[index][6] = timeList[index - 1][6]
                        calculatedList.append(["".join(timeList[index][:5]),"".join(timeList[index][6])])
                        count += 1
                    else:
                        timeList[index][6] = str(rx/n)
                        # print("".join(timeList[index]))
                        # print((timeList[index][6]))
                        calculatedList.append(["".join(timeList[index][:5]),"".join(timeList[index][6])])
                        count += 1
                    rx = 0
                    n = 0
                    index += 1
                    rx += int(float(pickedData[1]))
                    n += 1
            else:
                if n == 0:
                    timeList[index][6] = timeList[index - 1][6]
                    calculatedList.append(["".join(timeList[index][:5]),"".join(timeList[index][6])])
                    count += 1
                else:
                    timeList[index][6] = str(rx/n)
                    calculatedList.append(["".join(timeList[index][:5]),"".join(timeList[index][6])])
                    count += 1
                rx = 0
                n = 0
                index += 1
                rx += int(float(pickedData[1]))
                n += 1
        else:
            if n == 0:
                timeList[index][6] = timeList[index - 1][6]
                calculatedList.append(["".join(timeList[index][:5]),"".join(timeList[index][6])])
                count += 1
            else:
                timeList[index][6] = str(rx/n)
                calculatedList.append(["".join(timeList[index][:5]),"".join(timeList[index][6])])
                count += 1
            rx = 0
            n = 0
            index += 1
            rx += int(float(pickedData[1]))
            n += 1
            
    return calculatedList 
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
    
    
        
    
def input(list,f):
    length = len(list)
    for i in range(length):
        f.write(list[i][0]+','+list[i][1]+'\n')
    
if __name__ == "__main__":
    main()