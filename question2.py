file1 = open('/home/ky2910/PycharmProjects/pythonProject/inputPS02Q2.txt', 'r')
lines = file1.readlines()
product_names = list(map(lambda x:x.strip() , lines[0].split(':')[1].strip().split('/')))
staging_time = list(map(lambda x:int(x.strip()) , lines[1].split(':')[1].strip().split('/')))
photo_time = list(map(lambda x:int(x.strip()) , lines[2].split(':')[1].strip().split('/')))
arr = []
for i in range(len(product_names)):
    arr.append((staging_time[i],photo_time[i],product_names[i]))
    arr = sorted(arr,key = lambda x : (x[0],x[1]))

fout = open("/home/ky2910/PycharmProjects/pythonProject/outputPS02Q2.txt", "w")
for i in range(len(product_names)):
    out=list(arr[i])
    if i==len(product_names)-1:
        fout.write(str(out[2]))
    else:
        fout.write(str(out[2])+",")

fout.close()