#!/usr/bin/python3

import os
import sys
import datetime
import time

def cur_file_dir():
     path = sys.path[0]
     if os.path.isdir(path):
         return path + '/'
     elif os.path.isfile(path):
         return os.path.dirname(path)

def inc_day(adate):
    mydate = datetime.datetime.strptime(adate, "%Y.%m.%d")
    #print(mydate)
    #mydate.timedelta(days=-1)
    mydate = mydate + datetime.timedelta(days=-1)
    return mydate.strftime("%Y.%m.%d")

def read_new_title(project_file,mydate, days):
    f = open(cur_file_dir() + '../projects/'+project_file, "rU")
    contents = f.read()
    i = 0
    showtitile = 1
    while i < int(days) : 
        first = contents.find('#### '+mydate)
        end = contents.find('#### ', 20+first)
        if( first > 0):
            content = contents[first+len('#### '+mydate)+1:end]
            if showtitile == 1:
                content = content.replace("\n\n", "\n")
                print(project_file.replace('.md','') ,"|", mydate, "|",content.replace('\n','<br>') )
                showtitile = 0
            else:
                print(" |   |", mydate, "|",content.replace('\n','<br>') )
        i = i+1
        mydate = inc_day(mydate)
     
    #return f
    #print(contents)
    

def cat_projects(mydate, days):
    projects = os.listdir(cur_file_dir() + '../projects/')         
    #print(projects)
    for p in projects:
        content = read_new_title(p,mydate, days)
        #print(p)
        #print(content)


if __name__ == '__main__':
    print("项目 | 日期 | 更新内容 ")
    print("-- |---|---- ")
    if(len(sys.argv)== 1):
        now = datetime.datetime.now()
        cat_projects(now.strftime("%Y.%m.%d"), 10)
    else:
        cat_projects(sys.argv[1], sys.argv[2])