#!/usr/bin/env python3
#-*-coding:utf-8-*-
__author__ = 'IOT'
import requests
f = open ('./name/name.txt','r')
false = open('./name/false.txt','a+')
name = 0
for image in f.readlines():
    image = image.strip('\n')
    format=image.split(".")[-1]
    name = name+1
    try:
        image = requests.get(image)
        with open('./name/%s.%s'%(name,format),'wb') as images:
            images.write(image.content)
    except:
        false.writelines(image+'\n')
