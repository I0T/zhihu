#!/usr/bin/env python3
#-*-coding:utf-8-*-
__author__ = 'IOT'
import time
import requests
time_start = time.time()
print ('开始下载图片')
name = 'name'
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
            print ('第%s张下载完毕   '%pic_name+an+'%')
    except:
            false.writelines(str(image)+'\n')
    time_now = str(time.time()-time_start).split('.')[0]
    print ('程序运行时间%ss'%time_now)
