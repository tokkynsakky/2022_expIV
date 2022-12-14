# -*- coding:utf-8 -*-

import glob
import chardet

                    
    
def main():
    timeList = makeTimeList()
    
    
    
    k = "./RxData/200906/20090602/192.168.100.11_csv.log"
    
    f = open(k,"r",encoding='utf-8')
    data = f.readlines()
    list = calculate(data,timeList)
    f.close()
    # print(timeList)
    # print(len(timeList))



#時間の区切りを作成する関数
def makeTimeList():
    timeList = []
    value = [00,00,00]#hour:min:sec
    length = 8640
    
    for i in range(length):
        timeList.append([f'{value[0]:02}',':',f'{value[1]:02}',':',f'{value[2]:02}',',',f'{value[2]:02}'])
        # timeList.append(str(value[0]).zfill(2)+":"+str(value[1]).zfill(2)+":"+str(value[2]).zfill(2))
        
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


def carrier():
    pass

def count():
    
    pass

    
def calculate(data,timeList):
    length = len(data)
    ran = range(length)
    indexTimeList = 0
    
    indexHour = 0
    indexMin = 0
    indexSec = 0
    nextHour = 360
    nextMin = 6
    nextSec = 1
    stringRowCount = 0
    
    c = 0
    rx = 0
    n = 0
    
 
    for i in ran:
        #最初の文字が数字でない場合Continue
        if not data[i][0].isdigit():
            stringRowCount += 1
            continue
        if i == length - 2:
            break
        
        pickedData = data[i].split(",")[:2]
        pickedTime = pickedData[0].split(":")
        
        
        
        if int(timeList[indexHour][0]) <= int(pickedTime[0]) < int(timeList[indexHour+nextHour][0]):
            if int(timeList[indexMin][2]) <= int(pickedTime[1]) < int(timeList[indexMin+nextMin][2]):
                if int(timeList[indexSec][4]) <= int(pickedTime[2]) <= int(timeList[indexSec][4]) + 9:
                    rx += int(pickedData[1])
                    n += 1
                else:
                    if n != 0:
                        timeList[indexTimeList][6] = str(rx/n)
                    rx = 0
                    n = 0
                    indexTimeList += 1
                    indexSec += nextSec    
            else:
                if n != 0:
                    timeList[indexTimeList][6] = str(rx/n)
                rx = 0
                n = 0
                indexTimeList += 1
                indexSec += nextSec
                indexMin += nextMin
        else:
            if n != 0:
                timeList[indexTimeList][6] = str(rx/n)
            rx = 0
            n = 0
            indexTimeList += 1
            indexSec += nextSec
            indexMin += nextMin
            indexHour += nextHour
            
            
        # print("timeList[indexHour][0] = "+timeList[indexHour][0]+"\n"+"indexHour = "+str(indexHour))
        # print("timeList[indexHour+nextHour][0] = "+timeList[indexHour+nextHour][0]+"\n"+"indexHour+nextHour = "+str(indexHour+nextHour))
        # print("timeList[indexMin][2] = "+timeList[indexMin][2]+"\n"+"indexMin = "+str(indexMin))
        # print("timeList[indexMin+nextMin][2] = "+timeList[indexMin+nextMin][2]+"\n"+"indexMin+nextMin = "+str(indexMin+nextMin))
        # print("timeList[indexSec][4] = "+timeList[indexSec][4]+"\n"+"indexSec = "+str(indexSec))
        # print("timeList[indexSec+nextSec][4] = "+timeList[indexSec+nextSec][4]+"\n"+"indexSec+nextSec = "+str(indexSec+nextSec))
        # print("")
       
            

            
    for i in range(20): 
        print(timeList[i])
        pass
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
    
    
        
    
def input(list,f):
    length = len(list)
    for i in range(length):
        f.write(list[i]+'\n')
    
if __name__ == "__main__":
    main()