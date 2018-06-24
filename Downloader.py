#/usr/bin/python3/
#coding=utf-8
#================ 简介 ===================
#     脚本：          下载器     
#     作者：          北方重工NK1 
#     时间：          2017年12月10日 13:37:11
#     描述:           下载器脚本
#================ 简介 ===================




from urllib import request as urllib2
import urllib.parse as urlparse
import time,datetime
from selenium import webdriver
#import lxml.html
import sys,os
from ImagerandWorder import imorder
#新建qq号来接受作业帮网址



Headers={
    'host':'www.zybang.com',
    'referer':"https://www.zybang.com/",
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'accept-language':'en-US;q=0.5,en;q=0.3',
    'connection':'keep-alive',
    'upgrade-insecure-requests':'1',
    'cache-control':'max-age=0',
    'cookie':'p_ab_id=4; p_ab_id_2=8; device_token=91c3112fe5a33aa8c9d02d8b37403500; module_orders_mypage=%5B%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; login_ever=yes; __utma=235335808.562646940.1501219988.1501781881.1501791377.12; __utmz=235335808.1501329291.5.3.utmcsr=accounts.pixiv.net|utmccn=(referral)|utmcmd=referral|utmcct=/login; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=female=1^6=user_id=26394916=1^9=p_ab_id=4=1^10=p_ab_id_2=8=1^11=lang=zh=1; _ga=GA1.2.562646940.1501219988; auto_view_enabled=1; PHPSESSID=26394916_4b100233c217b05721b53059aa2d27ec; is_sensei_service_user=1'
    }



class Downloader:
    def __init__(self):
        print("The Downloader has been launched.")
        self.header=Headers
        self.counter=0

    def download(self,url,time_retries=2):
        self.url=url
        print("Downloading:",url)
        request_0=urllib2.Request(url,headers=Headers)
        try:
            html=urllib2.urlopen(request_0).read().decode('utf-8')
        except urllib2.URLError as e:
            print("Download Error:",e.reason)
            html=None
            if(time_retries>0):
              if(hasattr(e,'code') and 500<=e.code<600):
                #retry 5xx errors
                 return download(url,time_retries-1)
        return html

    def render(self,times,url,absolut_path):
        driver = webdriver.PhantomJS(executable_path=('C:/Phantomjs/bin/phantomjs'),service_args=['--ignore-ssl-errors=true','--ssl-protocol=TLSv1'])
        driver.set_window_size(540,960)
        driver.get(url)
        driver.save_screenshot(absolut_path+'\screenshots\screenshot'+str(self.counter)+'.png')
        #将图片编号
        '''

        注意解决元素获取到的位置和截图位置不符的问题

        '''
        #寻找题目所在的元素组,可以F12该元素后右键copy->xpath或selector
        '''用content的最后一个元素测试是否为什么都有的常规问题'''
        try:
            element_test=driver.find_element_by_css_selector('body > div.main-body > div > div.content > div > dl.card.refer > dd:nth-child(5)')
        #将题目所在的元素组截图
        except:
            try:
                element_question=driver.find_element_by_css_selector('body > div.main-body > div > div > div > dl.card.refer > dd:nth-child(2) > dl > dd')
                element_answer=driver.find_element_by_css_selector('body > div.main-body > div > div > div > dl.card.refer > dd:nth-child(3) > dl > dd')
            except:
                print("Ooops,looks we've got an error here...try to have a discussion with the developer by qq:1970938138\nGive him the following address please.\n")
                print(url)
                os.system("pause")
        else:
            element_question=driver.find_element_by_css_selector('body > div.main-body > div > div.content > div > dl.card.refer > dd:nth-child(2) > dl > dd')
            element_answer=driver.find_element_by_css_selector('body > div.main-body > div > div.content > div > dl.card.refer > dd:nth-child(5) > dl > dd')
        finally:
            left_question = element_question.location['x']
            top_question = element_question.location['y']
            right_question = element_question.location['x'] + element_question.size['width']
            bottom_question = element_question.location['y'] + element_question.size['height']
            left_answer = element_answer.location['x']
            top_answer = element_answer.location['y']
            right_answer = element_answer.location['x'] + element_answer.size['width']
            bottom_answer = element_answer.location['y'] + element_answer.size['height']
        '''
        一定要记得driver.quit()防止内存爆满
        '''
        result=list([self.counter,left_question,top_question,right_question,bottom_question,left_answer,top_answer,right_answer,bottom_answer])
        self.counter+=1
        print(self.counter)
        if(self.counter==times):
            driver.quit()
        if(result):
            return result
        else:
            print('Download Error.')
        

class Throttle:
    #实现延时
    def __init__(self,delay):
        print("初始化限速器...")
        #设置延迟
        self.delay=delay
        #最终访问一个集合的时间戳
        self.domains={}

    def wait(self,url):
        domain=urlparse.urlparse(url).netloc
        #最后一次访问时间
        last_accessed=self.domains.get(domain)
        if(self.delay>0 and last_accessed is not None):
            sleep_secs=self.delay-(datetime.datetime.now()-last_accessed).second
            if(sleep_secs>0):
                #近期访问过该网站
                #延迟
                time.sleep(sleep_secs)
        #更新延迟时间
        self.domains[domain]=datetime.datetime.now()



#以下为调试区
'''
Download=Downloader()
print(Download.download(url='https://www.zybang.com/question/rcswebview/8ae38c6be5a4d043ccec9e58ac5e71b9.html?nqid=ea0810ab758c70edbf571d9aff3cb22f2db28d64a0b35e06',time_retries=2))
throttle=Throttle(delay)
result=Downloader.download(url,Headers,time_retries=2)
print(sys.path[0])

2018年2月6日 10:19:36
成功将网页截图裁剪为问题与答案
Download=Downloader()
temp=Download.render('https://www.zybang.com/question/rcswebview/07503827c5943b041efa0775f7a40331.html?nqid=4d043fe94097522e5a3137502ec7eeb862e03365b020e860',sys.path[0])
image=imorder()
image.load(sys.path[0]+'\screenshots\screenshot'+str(temp[0])+'.png')
image.cutbyelement(temp)
print(temp)
'''