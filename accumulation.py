import glob

def main():
    file = "./precipitation.txt"
    list = accumulation(file)
    writeData(list)
    
        
            

def accumulation(file):
    f = open(file,'r')
    data = f.readlines()
    tmp = 0
    count = 0
    befor = 0
    list = []
    for i in data:
        pickedData = i.split(" ")
        # memory = int(pickedData[0])
        tmp += int(pickedData[1])
        
        
        # 追加
        # if int(pickedData[1]) == 0:
        #     continue
        
        
        list.append([int(pickedData[0]),int(pickedData[1])])
        # list.append([memory,tmp])
    f.close()
    
    for i in list:
        # roundNum = 8
        # y = i[0]
        # x = i[1]
        # i[0] = round((x/tmp),roundNum)
        # i[1] = y
        
        
        
        y = i[0]
        x = i[1]
        i[0] = x/tmp #+ befor
        i[1] = y
        # befor = x/tmp
        
        
        # roundNum = 8
        # y = i[0]
        # x = i[1]
        # i[0] = round((x/tmp),roundNum) + round(befor,roundNum)
        # i[1] = y
        # befor = i[0]
        
        # roundNum = 8
        # i[1] = round((i[1]/tmp),roundNum) + round(befor,roundNum)
        # befor = i[1]
    return list
        

def writeData(list):
    file = "./accumulation.txt"
    f = open(file,'w')
    for k in range(len(list)):
        f.write(str(list[k][0])+" "+str(list[k][1])+"\n")
        print(list[k])
    f.close()
    

if __name__ == "__main__":
    main()