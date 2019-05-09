#!/usr/bin/python3

import os
import sys
import datetime

def cur_file_dir():
     path = sys.path[0]
     if os.path.isdir(path):
         return path + '/'
     elif os.path.isfile(path):
         return os.path.dirname(path)

def read_new_title(project_file,mydate):
    f = open(cur_file_dir() + '../projects/'+project_file, "rU")
    contents = f.read()
    first = contents.find('#### '+mydate)
    end = contents.find('#### ', 20)
    if( first > 0):
        content = contents[first+len('#### '+mydate):end]
        print(project_file.replace('.md','') ,"|", mydate, "|",content.replace('\n','<br>') )
     
    #return f
    #print(contents)
    

def cat_projects(mydate):
    projects = os.listdir(cur_file_dir() + '../projects/')         
    #print(projects)
    for p in projects:
        content = read_new_title(p,mydate)
        #print(p)
        #print(content)


if __name__ == '__main__':
    print("项目 | 日期 | 更新内容 ")
    print("-- |---|---- ")
    if(len(sys.argv)== 1):
        now = datetime.datetime.now()
        cat_projects(now.strftime("%Y.%m.%d"))
    else:
        cat_projects(sys.argv[1])