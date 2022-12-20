import glob

def main():
    file = "./precipitation.txt"
    list = accumulation(file)
    writeData(list)
    
def accumulation(file):
    f = open(file,'r')
    data = f.readlines()
    tmp = 0
    befor = 0
    list = []
    for i in data:
        pickedData = i.split(" ")
        tmp += int(pickedData[1])
        list.append([int(pickedData[0]),int(pickedData[1])])
    f.close()
    
    num = len(list)
    for i in range(len(list)):
        num -= 1
        if num < 0:
            break
        y = list[num][0]
        x = list[num][1]
        list[num][0] = ((x+befor)/tmp) * 100
        list[num][1] = y
        befor += x
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
    
# gnuplot> set logscale x
# gnuplot> set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 pi - 1 ps 1.5
# gnuplot> set pointintervalbox 3
# gnuplot> plot 'accumulation.txt' with linespoints ls 1