#/usr/bin/python3/
#coding=utf-8
#================ 简介 ===================
#     脚本：          伪·红石比较器     
#     作者：          北方重工NK1 
#     时间：          2017年12月10日 13:37:11
#     描述:           匹配元素_作业帮
#================ 简介 ===================



import re



Checking_Points1=r'<dt>考点：</dt>([\s\S]*?)</dd>'
Checking_Points2=r'.+?\[(.*?)\].+?'
Checking_Points_biology=r'<dd>([\s\S]*)\\n'
QQmsg=r'http://www.zybang.com/question/rcswebview/'
print("The comparisoner has been launched.")



def match(target,html):
    if(target=="Checking_Points"):
        result=re.findall(Checking_Points1,html)
        if(result):
            result=re.findall(Checking_Points2,str(result))
            if(result):
                return result
            else:
                result=re.findall(Checking_Points1,html)
                result=re.findall(Checking_Points_biology,str(result))
                if(result):
                    result_0=str(result[0]).strip('\\n')
                    result_0=result_0.strip(' ')
                    return result_0
                else:
                    print("没有找到考点,可能是该题目没有提供考点信息.如果你确定题目提供了考点信息,请联系原作者,并向其发送该题目的网址.","\n")
                    return None
        else:
            print("没有找到考点,可能是该题目没有提供考点信息.如果你确定题目提供了考点信息,请联系原作者,并向其发送该题目的网址.","\n")
            return None
    elif(target=="QQ"):
        if(re.match(QQmsg,html)):
            return True
        else:
            return False