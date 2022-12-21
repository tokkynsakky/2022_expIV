# -*- coding:utf-8 -*-

import glob
import chardet
import subprocess

# $ perl -i -pe 's/\R/\n/g' sample.txt             
    
def main():
    timeList = makeTimeList()
    for i in glob.glob("./RxData/*"):
        for j in glob.glob(i+"/*"):
            for k in glob.glob(j+"/*"):
                print(k+" is Now")
                
                if "_Calculated_" in k:
                    continue
                
                with open(k, 'rb') as f:
                    b = f.read()
                    
                if not(chardet.detect(b)['encoding'] == "ascii"):
                    print("move!!")
                    subprocess.call(["sed", "-i", "-e", "23751,27815d", "RxData/200910/20091012/192.168.100.11_csv.log"])
                    
                    # continue
                
                f = open(k,"r",encoding='utf-8')
                data = f.readlines()
                list = calculate(data,timeList)
                f.close()
                
                if ".9_csv.log" in k:
                    list = convert(list)
                
                file = k.replace("_","_Calculated_")
                
                f = open(file,"w")
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


#10秒おきに変換する関数 
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
    flag = ""
 
    for i in ran:
        #最初の文字が数字でない場合Continue
        if flag == "need sed":
            # コマンドを実行したい
            pass
            
        if not data[i][0].isdigit():
            stringRowCount += 1
            flag = "need sed"
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

# sed -i -e '23751,27815d' RxData/200910/20091012/192.168.100.11_csv.log
# sed -i -e '23751,27815d' spare\ data/RxData\ copy/200910/20091012/192.168.100.11_csv.log

# エラーが発生して途中に文字コードの異なるファイルが紛れたファイル名
# RxData/200910/20091012/192.168.100.11_csv.log
# 23751 <= 該当箇所 <= 27815

# 18GHzのデータを物理量に対応させるための関数
def convert(list):
    for i in range(len(list)):
        data = int(float(list[i][1]))
        if data < 0:
            data = data + 256
        list[i][1] = str(data/2 - 121)
        
    return list

# listの中身を取り出して与えられたファイルに書き込む関数 
def input(list,f):
    length = len(list)
    for i in range(length):
        f.write(list[i][0]+','+list[i][1]+'\n')
    
if __name__ == "__main__":
    main()