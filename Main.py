#/usr/bin/python3/
#coding=utf-8
#================ 简介 ===================
#     脚本：          作业帮爬虫     
#     作者：          北方重工NK1 
#     时间：          2017年12月10日 13:37:11
#     描述:           可能对学习有帮助吧233
#================ 简介 ===================



print("Initailizing classes...")
import Downloader
from Comparisoner import *
import sys,os
from ImagerandWorder import *
from qqbot import QQBotSlot as qqbotslot,RunBot




#初始化类,常量赋值
main_path=sys.path[0]
Downloader_init=Downloader.Downloader()
Delay=Downloader.Throttle(delay=2)
#由于要传入本次积攒错题的数量,待修改FileSave_init=FileSave(main_path)
image=imorder()
counter=0
strs=[]
bool0=True
print(main_path)

print("注:如截图存在错位,不全等问题,属正常情况,且该问题不具有普遍性,目前正在尝试解决该问题")
print("注':如有任何问题或bug出现,请联系作者qq:1970938138以解决问题,版本更新信息将会发布于该qq空间")
print("\n当前运行目录为:",main_path,"\n")

'''
while True:
    url_input=input("输入网址(网址可在作业帮中点击分享,通过qq或其他方式发送到电脑):")
    if(url_input=="result"):
        FileSave_init.read()
    elif(url_input):
        htmlpage=Downloader_init.download(url_input,time_retries=2)
        if(htmlpage):
            result=match("Checking_Points",htmlpage)
            if(result):
                FileSave_init.write(result,url_input)
                print("错误信息已储存.")
            #print(result,"\n")
            #print(htmlpage)
        else:
            print("下载失败或网页丢失")

以上为储存考点的内容

'''



#以下为接收qq信息的代码
@qqbotslot
def onQQMessage(bot,contact,member,content):
    if(match("QQ",content)):
        try:
            strs.index(content)
            bot.SendTo(contact,"近期整理过该错题")
        except:
            strs.append(content)
            bot.SendTo(contact,"添加成功")
    
    elif(content=="over"):
        bot.SendTo(contact,"正在整理")
        bool0=main(strs)
        if(bool0):
            os.system("pause")
            bot.Stop()
        else:
            pass
    
    elif(content=="retry"):
        bool0=main(strs)
        if(bool0):
            bot.SendTo(contact,"整理完成")
            os.system("pause")
            bot.Stop()
    
    elif(content=="pop"):
        strs.pop()
    
    else:
        print("接受了一些不可描述的信息...显然作者也不知道这是什么信息...理论上来说这里不应该有这样的信息")
    '''
    elif(content=="-hello"):
        bot.SendTo(contact,"你好,我是qq机器人")
    elif(content=="-stop"):
        bot.SendTo(contact,"QQ机器人已关闭")
        bot.Stop()
    '''



def maininput(htmls):
    global counter
    while True:
        str_input=input("输入网址,用逗号隔开:\n")
        str_input=str_input.split(",")
        for i in os.listdir(main_path+'\screenshots\\'):
            os.remove(os.path.join(main_path+'\screenshots\\',i))
        for i in str_input:
            #使用正则表达式检测是否为作业帮网址
            print('Dealing with:'+i+'...')
            temp=Downloader_init.render(len(str_input),i,main_path)
            image.load(main_path+'\screenshots\screenshot'+str(temp[0])+'.png')
            image.cutbyelement(temp)
            counter+=1
            print("Done.\n")
        FileSave_init=FileSave(main_path,counter)
        FileSave_init.writeword()
        for i in str_input:
            htmlpage=Downloader_init.download(i,time_retries=2)
            if(htmlpage):
                result=match("Checking_Points",htmlpage)
                if(result):
                    FileSave_init.write(result,i)
                    print("考点信息已储存.")
                else:
                    pass



def main(htmls):
    global counter
    str_input=htmls
    try:
        for i in os.listdir(main_path+'\screenshots\\'):
            os.remove(os.path.join(main_path+'\screenshots\\',i))
        for i in str_input:
            print('Dealing with:'+i+'...')
            temp=Downloader_init.render(len(str_input),i,main_path)
            image.load(main_path+'\screenshots\screenshot'+str(temp[0])+'.png')
            image.cutbyelement(temp,main_path)
            counter+=1
            print("Done.\n")
        FileSave_init=FileSave(main_path,counter)
        FileSave_init.writeword()
        for i in str_input:
            htmlpage=Downloader_init.download(i,time_retries=2)
            if(htmlpage):
                result=match("Checking_Points",htmlpage)
                if(result):
                    FileSave_init.write(result,i)
                    print("考点信息已储存.")

                else:
                    pass
        counter=0
        return True
    except Exception as e:
        print("由于标准库存在缺陷,请勿在电脑上开启qq,tim或记事本文件\n发送retry以重试,或发送stop停止")
        print(e)
        return False



if(__name__=="__main__"):
    RunBot()