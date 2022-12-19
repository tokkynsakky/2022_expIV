import glob

def main():
    graphMemory = makeGraphMemory()
    for i in glob.glob("./RainData/*"):
        for j in glob.glob(i+"/*"): 
            if not("Calculated" in j):
                continue
            graphMemory = frequency(j,graphMemory)
    writeData(j,graphMemory)


def writeData(j,data):
    file = "./precipitation.txt"
    f = open(file,'w')
    for k in range(len(data)):
        f.write(str(data[k][0])+" "+str(data[k][1])+"\n")
        # f.write("".join(data[j]))
    f.close()
    
def frequency(j,graphMemory):
    interval = 3
    f = open(j,'r').readlines()
    for k in f:
        l = k.split(",")
        data = int(float(l[1]))
        for m in range(len(graphMemory)):
            memory = graphMemory[m][0]
            if memory <= data < memory + interval:
                graphMemory[m][1] += 1
    return graphMemory
    

def makeGraphMemory():
    interval = 3
    list = []
    memory = 0
    while  not (memory > 150):
        list.append([memory,0])
        memory += interval
    return list



if __name__ == "__main__":
    main()