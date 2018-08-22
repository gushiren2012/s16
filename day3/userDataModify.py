import codecs
import userDataUtil
def select(filename,sql):
    Datalist=[]#user表的数据列表
    FilterList=[]#条件列表
    listOut=[]#经过条件筛选后的数据列表
    list4 = []#需要显示的数据列表
    Datalist = userDataUtil.getDataList(filename)#[['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date'], ['1', 'alex', '22', '13651054606', 'IT', '2013-04-01'], ['2', 'JACK WANG', '30', '13304230533', 'HR', '2015-05-03']]
    FilterList = userDataUtil.getSearchFiter(sql) #[['age','>','22'],['name','=','liucy']]
    listOut = userDataUtil.getAfterFiterList(Datalist,FilterList)
    list4 = userDataUtil.getShowWord(sql) #['name','age']
    if len(listOut)>0:
        for l in listOut:
            str1 = ""
            for k in list4:
                if k=="*":
                    str1= str(l)
                elif k in Datalist[0]:
                    str1 += l[Datalist[0].index(k)] +","
            print(str1)
def update(filename,sql):
    Datalist=[]#user表的数据列表
    FilterList=[]#条件列表
    listOut=[]#经过更新后的数据列表
    Datalist = userDataUtil.getDataList(filename)#[['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date'], ['1', 'alex', '22', '13651054606', 'IT', '2013-04-01'], ['2', 'JACK WANG', '30', '13304230533', 'HR', '2015-05-03']]
    FilterList = userDataUtil.getSearchFiter(sql) #[['age','>','22'],['name','=','liucy']]
    setKeyList = userDataUtil.getSetKey(sql) #[['age','=','24'],['name','=','liucy']]
    listOut = userDataUtil.getAfterUpdateList(Datalist,FilterList,setKeyList)#[['1', 'alex', '22', '13651054606', 'IT', '2013-04-01']]
    userDataUtil.updateData(filename,listOut)
def insert():
    pass
def delete(filename,sql):
    Datalist=[]#user表的数据列表
    FilterList=[]#条件列表
    listOut=[]#经过删除的数据列表
    Datalist = userDataUtil.getDataList(filename)
    FilterList = userDataUtil.getSearchFiter(sql)
    listOut = userDataUtil.getAfterDeleteList(Datalist,FilterList)
    userDataUtil.updateData(filename, listOut)
if __name__ =="__main__":
    filename = "userData.txt"
    while True:
        key = input("请输入SQL语句，select/insert/update/delete \n")
        if key.startswith("select") :
            select(filename,key)
        elif key.startswith("insert"):
            insert(filename,key)
        elif key.startswith("update"):
            update(filename,key)
        elif key.startswith("delete"):
            delete(filename,key)
        else:
            print("输入SQL不被认同，请重新输入!")