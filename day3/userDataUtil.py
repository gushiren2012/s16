def getMiddleStr(content,startStr,endStr):
    startIndex = content.index(startStr)
    if startIndex >= 0:
        startIndex += len(startStr)
    endIndex = content.index(endStr)
    return content[startIndex:endIndex]
def getEndStr(content,startStr):
    try:
        startIndex = content.index(startStr)
        if startIndex >= 0:
            startIndex += len(startStr)
        return content[startIndex:]
    except ValueError as e :
        return ""
def getShowWord(sql):
    str = getMiddleStr(sql,'select','from')
    list = str.split(',')
    list1 = []
    for l in list:
        list1.append(l.strip())
    return list1
def fenci_handler(list,key):
    list1 = []
    isHit = False
    for l in list:
        for i in key:
            try:
                if i in l:
                    list2 = []
                    endindex = l.index(i)+len(i)
                    str = l[:l.index(i)].strip()
                    str1 = l[endindex:].strip()
                    list2.append(str.replace("\"",""))
                    list2.append(i)
                    list2.append(str1.replace("\"",""))
                    list1.append(list2)
                    isHit = True
            except ValueError as e:
                pass
    if  isHit == False:
        print("没有命中的条件关键字")
        exit(0)
    return list1

def getSetKey(sql):
    str = getMiddleStr(sql, 'set', 'where')
    if str =="":
        return []
    else:
        list = str.split(",")
        SearchKey=['=']
        return fenci_handler(list, SearchKey)
def getSearchFiter(sql):
    str = getEndStr(sql,'where')
    if str == "":
        return []
    else:
        list = str.split('and')
        SearchKey = ['=','>','like']
        return fenci_handler(list, SearchKey)
def getDataList(filename):
    fl = open(filename)
    list = fl.readlines()
    listData = [] #[[1,alex,22,13651054606,IT,2013-04-01],[2,JACK WANG,30,13304230533,HR,2015-05-03]]
    for l in list:
        l=l.strip()
        list2 = l.split(',')
        listData.append(list2)
    return listData
def getAfterFiterList(Datalist,filterList):
    listOut = []
    for l in Datalist[1:]:
        panduan = True
        for i in filterList:
            if i[0] in Datalist[0]:
                if i[1]==">":
                    if l[Datalist[0].index(i[0])]<=i[2]:
                        panduan = False
                elif i[1]=="=":
                    if l[Datalist[0].index(i[0])]!=i[2]:
                        panduan = False
                elif i[1]=="like":
                    if  i[2] not in l[Datalist[0].index(i[0])]:
                        panduan = False
                else:
                    panduan = False
                    print("不支持"+i[2]+"这个操作符")
            else :
                print("where关键字"+i[0]+"不存在")
                return False
        if panduan == True:
            listOut.append(l)
    return listOut
def getAfterUpdateList(Datalist,filterList,setKeyList):
    listOut = []
    listOut.append(Datalist[0])
    for l in Datalist[1:]:# ['1', 'alex', '22', '13651054606', 'IT', '2013-04-01']
        panduan = True
        for i in filterList:#['age','>','22']
            if i[0] in Datalist[0]:#['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date']
                if i[1]==">":
                    if l[Datalist[0].index(i[0])]>i[2]:
                        for key in setKeyList:#['age','=','24']
                            if key[0] in Datalist[0]:
                                l[Datalist[0].index(key[0])]=key[2]
                elif i[1]=="=":
                    if l[Datalist[0].index(i[0])] == i[2]:
                        for key in setKeyList:#['age','=','24']
                            if key[0] in Datalist[0]:
                                l[Datalist[0].index(key[0])]=key[2]
                elif i[1]=="like":
                    if  i[2] in l[Datalist[0].index(i[0])] :
                        for key in setKeyList:#['age','=','24']
                            if key[0] in Datalist[0]:
                                l[Datalist[0].index(key[0])]=key[2]
                else:
                    print("不支持"+i[2]+"这个操作符")
                    return False
            else :
                print("where关键字"+i[0]+"不存在")
                return False
        listOut.append(l)
    return listOut
def updateData(filename,datalist):
    f1 = open(filename,'w')
    for l in datalist :
        for i in l :
            if l.index(i)==len(l)-1:
                f1.write(i)
            else:
                f1.write(i+',')
        f1.write('\n')
    f1.close()
def getAfterDeleteList(Datalist,filterList):
    for l in Datalist[1:]:
        for i in filterList:
            if i[0] in Datalist[0]:
                if i[1]==">":
                    if l[Datalist[0].index(i[0])]>i[2]:
                        Datalist.remove(l)
                elif i[1]=="=":
                    if l[Datalist[0].index(i[0])]==i[2]:
                        Datalist.remove(l)
                elif i[1]=="like":
                    if  i[2]  in l[Datalist[0].index(i[0])]:
                        Datalist.remove(l)
                else:
                    print("不支持"+i[2]+"这个操作符")
            else :
                print("where关键字"+i[0]+"不存在")
                return False
    return Datalist