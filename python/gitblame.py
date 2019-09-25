
import os

dir="/home/jian/work/gitosis-admin/backupall/"

def toomanyfiles(lines):
    for line in lines:
        print(line)

gits = os.listdir(dir) 
for g in gits:
    if os.path.isdir(dir+g):
        print(g)
        os.chdir(dir+g)
        shascmd = os.popen('git log --all --since=1.weeks --date=short --pretty=format:"%H"')
        #print (shascmd.readlines())
        for sha in shascmd.readlines():
            showcmd = os.popen('git show --pretty=oneline ' + sha)
            details = showcmd.readlines()
            toomanyfiles(details)
        os.chdir(dir)
