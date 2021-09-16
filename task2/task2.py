def distance(file1,file2):
    data1 = []
    with open(file1) as f:
        for line in f:
            data1.append([float(x) for x in line.split()])
    x0=data1[0][0]
    y0=data1[0][1]
    r=data1[1][0] 
    data2 = []
    with open(file2) as f:
        for line in f:
            data2.append([float(x) for x in line.split()])
    lst=[]
    for i in range(len(data2)):
        if (data2[i][0]-x0)**2+(data2[i][1]-y0)**2 == r**2:
            lst.append(0)
        elif  (data2[i][0]-x0)**2+(data2[i][1]-y0)**2 < r**2:
            lst.append(1)
        else:
            lst.append(2)
    for i in lst:
        print(i)
distance("data1.txt","data2.txt")