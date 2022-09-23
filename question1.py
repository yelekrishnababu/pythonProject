distances = {}
#changing dictionary as per the orders
def changeMap(location,order):
    final = []
    for i in range(len(location)):
        distances[tuple(location[i])] = (float(location[i][0]) ** 2) + (float(location[i][1]) ** 2)
    finaldistances = (dict(sorted(distances.items(), key=lambda item: item[1])))
    for i in range(int(order)):
        final.append(list(finaldistances.keys())[i])
        location.remove(list(finaldistances.keys())[i])
        del distances[list(finaldistances.keys())[i]]
    fout.write(f'{final}\n')

#reading input file
file1 = open('/home/ky2910/PycharmProjects/pythonProject/InputPS02Q1.txt', 'r')
with open(r"/home/ky2910/PycharmProjects/pythonProject/InputPS02Q1.txt", 'r') as fp:
    lines = len(fp.readlines())
location=[]

#writing to a output file
fout = open("/home/ky2910/PycharmProjects/pythonProject/OutputPS02Q1.txt", "w")


for i in range(lines):
    line=file1.readline().strip()
    if(len(line)>9):
        line=line[11:]
        g=list(line.split(":"))
        location.append(((float(g[0]),float(g[1]))))
        fout.write(f'{(float(g[0]),float(g[1]))}\n')
    else:
        x=line[7:]
        changeMap(location,float(x))

fout.close()