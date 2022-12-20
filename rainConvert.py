import glob

def main():
    for i in glob.glob("./RainData/*"):
        for j in glob.glob(i+"/*"): 
            if "Calculated" in j:
                continue
            data = calculateRain(j)
            writeData(j,data)
            
            # c = rowPrint(data)
      
def calculateRain(j):
    k = open(j,'r')
    l = k.readlines()
    garbageRow = 0
    data = []
    for m in range(len(l)):
        if not l[m][0].isdigit():
            continue
        time = l[m].replace("\n","").split(",")[0]
        count = int(float(l[m].replace("\n","").split(",")[1])) * 0.0083333 * 60
    
        data.append([time,count])
        
    return data

def writeData(j,data):
    file = j.replace(".csv","")+"_Calculated.csv"
    f = open(file,'w')
    for k in range(len(data)):
        f.write(data[k][0]+","+str(data[k][1])+"\n")
        # f.write("".join(data[j]))
    f.close()
    


def convert18GHz():
    pass

def rowPrint(list):
    c = 0
    for i in range(len(list)):
        print(list[i])
        c += 1
    return c
    # if(c != 1440):
        # print("============erorr============="+"\n"+j)
        # print(c)
        # print("")

        
        
                
                








if __name__ == "__main__":
    main()