#对问卷的所有可能性进行划分，形成决策树的训练预料，传入的结果是23个单选题目以及一个多选题目,形成十进制的结果
#!/usr/bin/python
import json
import datetime
import os 
import sys


def BitCount1(n):
    bin_n = bin(n)
    return bin_n[2:].count('1')
def GetNbit(x,n):
    return (x>>n) & 1 
#jsonData = {"1":1,"2":0,"3":1,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0,"13":0,"14":0,"15":0,"16":0,"17":0,"18":0,"19":0,"20":0,"21":1,"22":0,"23":0,"24":{"1":0,"2":0,"3":0,"4":0}}

def wirtelog(strwirte):
    fileopen = open(str(datetime.datetime.now().year)+str(datetime.datetime.now().month.PadLeft(2,'0'))+str(datetime.datetime.now().day.PadLeft(2,'0')),"a+")
    fileopen.write(strwirte+"\n")
    fileopen.close()

def jsonToNum(jsonData):
    string_return = '0b'
    text = json.loads(jsonData)
    #print(text["1"])
    for i in range(1,24):
        string_return += str(text[str(i)])
    text_list =  (text["24"])
    for i in range(1,5):
        string_return += str(text_list[str(i)])
    wirtelog(json.dumps(jsonData,ensure_ascii=False))
    return string_return
    #print(jsonToNum(jsonData)) 
def judge(filename):
    #print(filename)
    jsonData = open(filename,"r").readline().replace("\n","")
    number_json = jsonToNum(jsonData)
    #number_json = '0b1101'
    num10json = int(number_json , 2)
    #print(num10json)
    string_output = ""
    if num10json == 0:
        string_output = "未吸毒"
    else:
        if (BitCount1(num10json) <= 4):
            string_output = "吸毒可能性很低"
        elif ((GetNbit(num10json,12) & GetNbit(num10json,11)) or (GetNbit(num10json,9) &GetNbit(num10json,8)) or (not (GetNbit(num10json,7)&GetNbit(num10json,6))) ):
            string_output = "无效问卷"
        elif ((GetNbit(num10json,4)&GetNbit(num10json,5)&GetNbit(num10json,6)&GetNbit(num10json,7)) and ((GetNbit(num10json,23)+GetNbit(num10json,24)+GetNbit(num10json,25)+GetNbit(num10json,26)+GetNbit(num10json,27)+GetNbit(num10json,28))>=5)):
            string_output = "K粉"
        elif ((GetNbit(num10json,2)&GetNbit(num10json,4)&GetNbit(num10json,6)&GetNbit(num10json,8)) and ((GetNbit(num10json,23)+GetNbit(num10json,24)+GetNbit(num10json,25)+GetNbit(num10json,26)+GetNbit(num10json,27)+GetNbit(num10json,28))>=5)):
            string_output = "摇头丸"
        elif ((GetNbit(num10json,0)&GetNbit(num10json,2)&GetNbit(num10json,4)&GetNbit(num10json,10)&GetNbit(num10json,16)) and ((GetNbit(num10json,22)+GetNbit(num10json,23)+GetNbit(num10json,24)+GetNbit(num10json,25)+GetNbit(num10json,26)+GetNbit(num10json,27)+GetNbit(num10json,28))>=6) and(GetNbit(num10json,18)+GetNbit(num10json,19)+GetNbit(num10json,20)>=2)):
            string_output = "麻古"
        elif ((GetNbit(num10json,0)&GetNbit(num10json,2)&GetNbit(num10json,4)&GetNbit(num10json,10)&GetNbit(num10json,16)) and  ((GetNbit(num10json,21)+GetNbit(num10json,22)+GetNbit(num10json,23)+GetNbit(num10json,24)+GetNbit(num10json,25)+GetNbit(num10json,26)+GetNbit(num10json,27)+GetNbit(num10json,28))>=7)):
            string_output = "大麻"
        elif ((GetNbit(num10json,1)&GetNbit(num10json,3)&GetNbit(num10json,9)&GetNbit(num10json,13)&GetNbit(num10json,16)) and ((GetNbit(num10json,21) +GetNbit(num10json,22)+GetNbit(num10json,23)+GetNbit(num10json,24)+GetNbit(num10json,25)+GetNbit(num10json,26)+GetNbit(num10json,27)+GetNbit(num10json,28))>=6) and(GetNbit(num10json,18)+GetNbit(num10json,19)+GetNbit(num10json,20)>=2)):
            string_output = "吗啡"
        elif ((GetNbit(num10json,1)&GetNbit(num10json,2)&GetNbit(num10json,3)&GetNbit(num10json,4)&GetNbit(num10json,10)) and (GetNbit(num10json,21)+GetNbit(num10json,21)+(GetNbit(num10json,22)+GetNbit(num10json,23)+GetNbit(num10json,24)+GetNbit(num10json,25)+GetNbit(num10json,26)+GetNbit(num10json,27)+GetNbit(num10json,28))>=7) and(GetNbit(num10json,15)+GetNbit(num10json,16)+GetNbit(num10json,17))>=2):
            string_output = "冰毒"
        else:
            string_output = "收集更多的信息"
    return(string_output)

def main(argv):
    print(judge(argv))

 

if __name__ == '__main__':
    main(sys.argv[1])