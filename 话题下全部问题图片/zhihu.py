#!/usr/bin/env python3
#-*-coding:utf-8-*-
__author__ = 'IOT'
#获取自拍页面网页源码
import re
import os
import time
import requests
def zhihu():
    # 获取问题页面源码
    User_Agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:44.0) Gecko/20100101 Firefox/44.0")
    html = requests.get (url,{User_Agent:User_Agent})
    html = html.text
    #mkdir
    name = str(re.findall('<title>(.*?) - 等待回答 - 知乎</title>',html,re.S)).strip("[]'")
    print ('[%s]主题为:%s'%(time.strftime("%X"),name))
    os.mkdir('./%s/'%name)
    #生成所有答案页面列表
    page_max = re.findall('page=(.*?)"',html,re.S)
    page_max = max([int(k) for k in page_max])
    page_all = list(range(1,page_max+1))
    #获取所有答案页面
    f= open('./%s/%s图片链接1.txt'%(name,name),'a+')
    for page in page_all:
        pages = ("%s?page=%s"%(url,page))
        pages = requests.get(pages,{User_Agent:User_Agent})
        questions = re.findall(r'_link" href="(.*?)"',pages.text,re.S)
        for question in questions:
            question_all = ("https://www.zhihu.com%s"%question)
            question_html = requests.get(question_all,{User_Agent:User_Agent})
            question_html = question_html.text
            pic_urls = str(re.findall('data-actualsrc="(.*?)"',question_html,re.S))
            f.writelines(pic_urls+'\n')
            print(pic_urls)
        an = str(100*page/page_max).split('.')[0]
        print (r'[%s]第(%s/%s)页抓取完毕'%(time.strftime("%X"),page,page_max)+an+'%')
        time_now = str(time.time()-time_start).split('.')[0]
        print('[%s]程序运行时间:%ss'%(time.strftime("%X"),time_now))
    f.close()
    #处理答案页面，保留图片url
    f = open('./%s/%s图片链接1.txt'%(name,name),'r')
    f = re.findall("h(.*?)'",str(f.readlines()),re.S)
    for x in f:
        x = 'h'+x
        f_1 = open('./%s/%s图片链接.txt'%(name,name),'a+')
        f_1.writelines(x+'\n')
    print ('[%s]%s图片链接生成完毕'%(time.strftime("%X"),name))
    #开始下载图片
    print ('[%s]开始下载图片'%(time.strftime("%X")))
    f= open ('./%s/%s图片链接.txt'%(name,name),'r')
    f= f.readlines()
    num = len(f)
    false = open('./%s/无法下载的链接.txt'%name,'a+')
    pic_name = 0
    for image in f:
        image = image.strip('\n')
        format=image.split(".")[-1]
        pic_name = pic_name+1
        try:
            image = requests.get(image)
            with open('./%s/%s.%s'%(name,pic_name,format),'wb') as images:
                images.write(image.content)
                an =str(100*pic_name/num).split('.')[0]
                print ('[%s]第%s张下载完毕   '%(time.strftime("%X"),pic_name)+an+'%')
        except:
                false.writelines(str(image)+'\n')
        time_now = str(time.time()-time_start).split('.')[0]
        print ('[%s]程序运行时间%ss'%(time.strftime("%X"),time_now))
    #删除程序运行残留
    print('[%s]删除程序运行残留'%(time.strftime("%X")))
    os.remove('./%s/%s图片链接.txt'%(name,name))
    os.remove('./%s/%s图片链接1.txt'%(name,name))
if __name__=='__main__':
    #话题URL在此修改
    time_start = time.time()
    url = ("https://www.zhihu.com/topic/19566151/questions")
    zhihu()
    time_end = time.time()
    time = str(time_end-time_start).split('.')[0]
    print ('[%s]程序运行时间为%ss'%(time.strftime("%X"),time))
