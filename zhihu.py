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
    name = str(re.findall('<title>(.*?) - 全部问题 - 知乎</title>',html,re.S)).strip("[]'")
    print ('主题为:'+name)
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
        print (r'第(%s/%s)页抓取完毕'%(page,page_max)+str(100*page/page_max)+'%')
    f.close()
    #处理答案页面，保留图片url
    f = open('./%s/%s图片链接1.txt'%(name,name),'r')
    f = re.findall("h(.*?)'",str(f.readlines()),re.S)
    for x in f:
        x = 'h'+x
        f_1 = open('./%s/%s图片链接.txt'%(name,name),'a+')
        f_1.writelines(x+'\n')
        print(f_1)
    print ('%s图片链接生成完毕'%name)
    #开始下载图片
    f = open ('./%s/%s图片链接.txt'%(name,name),'r')
    false = open('./%s/无法下载的链接.txt'%name,'a+')
    name = 0
    for image in f.readlines():
        image = image.strip('\n')
        format=image.split(".")[-1]
        name = name+1
        try:
            image = requests.get(image)
            with open('./%s/%s.%s'%(name,name,format),'wb') as images:
                images.write(image.content)
        except:
                false.writelines(image+'\n')
    #删除程序运行残留
    # os.remove('./%s/所有图片链接.txt'%name)
    os.remove('./%s/%s图片链接1.txt'%(name,name))
        #要不把所有页面先保存到txt里面 再读取？还是直接for in 出来直接抓取图片－－尝试两个方法好了－－
        #我想把所有结果爬取下来 生成一个html文件 可以直接看问题内容 超链接直接点开地址 后面是问题关注人数 问题回答人数
        #获取所有页面源代码 取出问题链接＋提问都作者 生成一个TXT 内容为问问题者＋问题标题
#问题名字建立文件夹 答主名字命名照片 IOT_1 IOT_2 etc
if __name__=='__main__':
    #话题URL在此修改
    url = ("https://www.zhihu.com/topic/19584431/questions")
    time_start = time.time()
    zhihu()
    time_end = time.time()
    print ('程序运行时间为%s s'%(time_end-time_start))
