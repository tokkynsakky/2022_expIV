import glob


def main():
    dict_18GHz = {}
    dict_26GHz = {}
    dict_18GHz_total = 0
    dict_26GHz_total = 0
    
    for i in glob.glob("./RxData/*"):
        for j in glob.glob(i+"/*"):
            for k in glob.glob(j+"/*"):
                
                if not("_Calculated_" in k):
                    continue
                
                if ".9_" in k:
                    dict_18GHz =  accumulate(dict_18GHz,k)
                    f = open(k,"r")
                    dict_18GHz_total += len(f.readlines())
                    f.close()
                else:
                    dict_26GHz = accumulate(dict_26GHz,k)
                    f = open(k,"r")
                    dict_26GHz_total += len(f.readlines())
                    f.close
    
    write(dict_18GHz,sorted(dict_18GHz),dict_18GHz_total,"18GHz_accumulated.txt")
    write(dict_26GHz,sorted(dict_26GHz),dict_26GHz_total,"26GHz_accumulated.txt")
    # write(dict_18GHz,reversed(sorted(dict_18GHz)),dict_18GHz_total,"18GHz_accumulated.txt")
    # write(dict_26GHz,reversed(sorted(dict_26GHz)),dict_26GHz_total,"26GHz_accumulated.txt")
    
    
def accumulate(dict,file):
    f = open(file,'r')
    list = f.readlines()
    for i in list:
        data = i.split(",")[1].replace("\n","")
        if data in dict:
            dict[data] += 1
            # dict[int(float(data))] += 1
        else:
            dict[data] = 1
            # dict[int(float(data))] = 1
    f.close()
    return dict

def write(dict,list,total,filename):
    f = open(filename,"w")
    befor = 0
    for i in list:
        x = dict[i]
        print(i)
        f.write(str(((x + befor)/total)*100)+" "+str(i)+"\n")
        befor += x
    f.close()

if __name__ == "__main__":
    main()