from matplotlib import pyplot as plt
import pandas as pd
import matplotlib
from pandas import Series,DataFrame
from os import walk
font = {'family': 'Microsoft YaHei',  'weight': 'bold',  'size': '14'}
matplotlib.rc("font", family="Microsoft YaHei", weight="bold", size="7")
class Readin:
    "读取所有txt并整合入csv文件中"
    def __init__(self):
        self.su=DataFrame([],index=['Date','Type','Operator','Registration','C/n / msn','First flight','Total airframe hrs','Cycles','Total','Aircraft damage','Location','Phase','Nature','Departure airport','Destination airport','Crew','Passengers','Narrative','Classification','Engines','Time','Aircraft fate','Investigating agency','Duration','Accident number','Download report','Crash site elevation','Flightnumber','Issued','Ground casualties','Operating for','Leased from','Collision casualties','Operated by','On behalf of'])#总数据
        #创造数据框
        self.path=[]#txt路径
        pass
    def getpath(self):
        #获取一个文件夹下的所有文件路径并初始化数据框
        filepath='D:\\飞机不安全数据\\asn89-19'

        for a,b,c in walk(filepath):
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
            temp=pd.read_table(i,header=None,error_bad_lines=False)
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

class Visible :
    "数据可视化聚合类"
    def __init__(self,x,y):
        self.x=x;
        self.y=y;
        pass
    def bar(self):
        plt.title("飞机不安全事件发生月份")
        plt.ylabel("事情（件）")
        plt.xlabel("月份")
        plt.bar(self.x,self.y,color='r')
        plt.show()
        pass
    def plot(self):
        plt.title("飞机不安全系数分布")
        plt.ylabel("飞机不安全系数")
        plt.xlabel("飞机状态")
        plt.plot(self.x,self.y,color='r')
        plt.show()
    def __del__(self):
        pass

class Solution:
    "数据分析的解决方案的集合"
    def __init__(self):
        self.su=DataFrame(pd.read_excel('text.xlsx'))
        self.su=self.su.set_index("index")
        pass
    def happenmonth(self):
        monthdict={}
        monthdict['January']=0
        monthdict['February']=0
        monthdict['March']=0
        monthdict['April']=0
        monthdict['May']=0
        monthdict['June']=0
        monthdict['July']=0
        monthdict['August']=0
        monthdict['September']=0
        monthdict['October']=0
        monthdict['November']=0
        monthdict['December']=0
        monthdict['ambiguous']=0


        datesum=[]
        counter=0

        while 1:
            try:
                temp=str(self.su.loc["Date",counter])
                temp=temp.split(" ")
                try:
                    month=temp[-2]
                    pass
                except IndexError:
                    monthdict['ambiguous']=monthdict['ambiguous']+1
                    counter=counter+1
                    continue
                
                try:
                    monthdict[month]=monthdict[month]+1
                    pass
                except KeyError:
                    monthdict['ambiguous']=monthdict['ambiguous']+1
                    counter=counter+1
                    continue
                counter=counter+1
                pass
            except KeyError:
                break
            pass
        vision=Visible(monthdict.keys(),monthdict.values())
        vision.bar()
        pass
    def status(self):

        phasedict={}
        phasedict['Taxi']={'total':0,'Missing':0,'Destroyed':0,'Damaged':0,'Substantial':0,'Minor':0,'None':0};
        phasedict['Takeoff']={'total':0,'Missing':0,'Destroyed':0,'Damaged':0,'Substantial':0,'Minor':0,'None':0};
        phasedict['Initial']={'total':0,'Missing':0,'Destroyed':0,'Damaged':0,'Substantial':0,'Minor':0,'None':0};
        phasedict['En']={'total':0,'Missing':0,'Destroyed':0,'Damaged':0,'Substantial':0,'Minor':0,'None':0};
        phasedict['Approach']={'total':0,'Missing':0,'Destroyed':0,'Damaged':0,'Substantial':0,'Minor':0,'None':0};
        phasedict['Landing']={'total':0,'Missing':0,'Destroyed':0,'Damaged':0,'Substantial':0,'Minor':0,'None':0};

        counter=0
        while 1:
            try:
                temp=str(self.su.loc["Phase",counter])
                temp=temp.split(" ")
                try:
                    phase=temp[0]
                    if len(phase)<2:
                        phase=temp[1]
                        pass
                    pass
                except IndexError:
                    counter=counter+1
                    continue
                
                try:
                    phasedict[phase]['total']=phasedict[phase]['total']+1
                    pass
                except KeyError:
                    counter=counter+1
                    continue

                
                temp=str(self.su.loc["Aircraft damage",counter])
                temp=temp.split(" ")
                try:
                    status=temp[1]
                    pass
                except IndexError:
                    counter=counter+1
                    continue

                try:
                    phasedict[phase][status]=phasedict[phase][status]+1
                except KeyError:
                    counter=counter+1
                    continue
                counter=counter+1
            except KeyError:
                break
            pass
        anslist=[]#危险程度系数
        sumlist=[]
        for i in phasedict:
            sum=0
            templist=[]
            datalist=list(phasedict[i].values())
            for u in range(1,7):
                templist.append(datalist[u])
                sum=sum+datalist[u]
                pass
            ans=templist[0]*0.2+templist[1]*0.2+templist[2]*0.2+templist[3]*0.1+templist[4]*0.07+templist[5]*0.03
            ans=ans/sum
            sumlist.append(sum)
            anslist.append(ans)
            pass
        sumsum=0
        for i in sumlist:
            sumsum=sumsum+i
            pass
        rarelist=[]#状态频率
        for i in sumlist:
            rarelist.append(i/sumsum)
            pass
        plist=[]#不安全系数
        for i in range(6):
            plist.append(rarelist[i]*anslist[i])
            pass
        keylist=list(phasedict.keys())
        vision=Visible(keylist,plist)
        vision.plot()
    def __del__(self):
        pass

if __name__=="__main__":
    '''
    read=Readin()
    read.getpath()
    read.writeinsum()
    '''
    solution=Solution()
    solution.status()
   
    #solution.happenmonth()