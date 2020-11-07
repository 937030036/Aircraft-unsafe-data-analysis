import matplotlib as plt
import pandas as pd
from pandas import Series,DataFrame
from os import walk

class Readin:
    "读取所有txt并整合入csv文件中"
    def __init__(self):
        self.su=DataFrame([],index=['Date','Type','Operator','Registration','C/n / msn','First flight','Total airframe hrs','Cycles','Total','Aircraft damage','Location','Phase','Nature','Departure airport','Destination airport','Crew','Passengers','Narrative','Classification','Engines','Time','Aircraft fate','Investigating agency','Duration','Accident number','Download report','Crash site elevation','Flightnumber','Issued','Ground casualties','Operating for','Leased from','Collision casualties','Operated by','On behalf of'])#总数据
        #创造数据框
        self.path=[]#文件路径
        pass
    def getpath(self):
        #获取一个文件夹下的所有文件路径并初始化数据框
        filepath='D:\\飞机不安全数据\\asn89-19\\1989'
        for a,b,c in walk(filepath):
            pass
        for i in c:
            self.path.append(a+'\\'+i)
        pass
        
        p=[]
        for i in range(35):
            p.append(-1)
            pass
        for i in range(len(self.path)):
            self.su[i]=p
            pass
        pass
    def writeinsum(self):
        #把所有信息写入sum
        counter=-1
        for i in self.path:
            temp=pd.read_table(i,header=None)
            counter=counter+1
            for u in range(len(temp)):
                eachraw=str(temp.loc[u,0]);
                eachraw=eachraw.split(":",1)
                try:
                    self.su.loc[eachraw[0],counter]=eachraw[1]
                    pass
                except IndexError:
                    continue
                pass
            pass
        #打印到csv格式
        self.su.to_csv("text.csv")

    def __del__(self):
        pass
    pass
if __name__=="__main__":
    read=Readin()
    read.getpath()
    read.writeinsum()
    pass