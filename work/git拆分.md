# Git仓库拆分分享

## Subtree
当前在 msm8905 工程中移植和修改了部分中间层代码，由于要把中间层单独提出来做共有工程，
故需要将已移植部分单独建仓，此时又想将原有的修改记录一并复制以便将来查看，在请教了苗工之后，
认识到 git subtree 这个工具。
现将仓库拆分迁移步骤描述如下，以供大家参考：

1. $ cd /work/msm8905  
先切换到包含准备要拆分的文件夹 tozed 所在的工程根目录。
2. $ git subtree split -P tozed master -b tozed  
-P tozed  为准备要拆分出来的文件目录，应该可以使用目录结构，没试；  
master 为主分支名，默认为当前所在分支，可以试试改为其他分支名是否可行；  
-b tozed 为要分离出的子树名，可随意取不与现有分支名相同的即可。
该命令会将 tozed 目录相关所有提交分离出来，并建立一个名为 tozed 的子树。使用 gitk –all 可
以看到在 master 主树下面会有另外一棵 tozed 子树。
3. $cd /work  
$ mkdir tozed && cd tozed  
$ git init  
新建文件夹存放新仓。  
如果当前仓已经有了，可忽略。
4. $ git pull ../msm8905 tozed  
将 msm8905 下的 tozed 子树拉到当前文件夹下。  
此时可能会提示当前分支异常，需要使用 git branch –unset-upstream 进行修复。按提示执行即
可，原因可能是子树里原有的远程跟踪与当前不符。  
因为我当前建立的 tozed 仓为空仓，所以没有出现冲突或其他异常现象。如果当前仓中已有提交，
不知道是否还能这样直接 pull 过来，可以一试。

## Format-patch am
在当前 tozed 仓不为空情况下，应该可以使用 format-patch 和 am 命令进行移植。  
参考资料 [git am说明](https://blog.csdn.net/qq_27636049/article/details/81351739)  
有待完善。。。