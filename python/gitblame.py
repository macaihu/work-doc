

import os
import re
#import string

dir="/home/jian/work/gitosis-admin/backupall/"

def printlines(lines):
    count = 0;
    for line in lines:
        line = line.strip()
        if(count < 20):
            print(line)
        else:
            print(str(len(lines)) + '行没有输出！')
            return
        #    print('.', end='')
        count += 1
    

def toomanyfiles(lines):
    have_bins = False;
    have_toomany = False;
    for line in lines:
        line = line.strip()
        #print(line)
        if (line.find('files changed')>0):
            space_pos=line.find(' ')
            changed_files=int(line[0:space_pos])
            if(changed_files>10):
                have_toomany = True
        binstr=re.findall('\\| {1,6}Bin\\b',line)
        if (len(binstr) > 0):
            #print(binstr)
            have_bins = True
    if(have_bins):
        print ('error: 提交了bin文件')
    if(have_toomany):
        print('error: 修改了太多文件！')
    if(have_bins or have_toomany):        
        printlines(lines)
        print("\n\n")
    #if ( lines.count() > 10 )    

gits = os.listdir(dir) 
for g in gits:
    if os.path.isdir(dir+g):
        print(g)
        os.chdir(dir+g)
        #shascmd = os.popen('git log --all --since=2.weeks --date=short --pretty=format:"%H"')
        os.system('git fetch')
        shascmd = os.popen('git log --all --since=2.days --date=short --pretty=format:"%H"')
        #print (shascmd.readlines())
        for sha in shascmd.readlines():
            sha = sha.strip()
            #print("\n\n")
            showcmd_str = 'git show ' + sha + ' --stat '
            showcmd = os.popen(showcmd_str)
            details = showcmd.readlines()
            toomanyfiles(details)
            sha_last = sha
        os.chdir(dir)
