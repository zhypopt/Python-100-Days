fork from https://github.com/jackfrued/Python-100-Days

a method to update with the souce of fork
https://blog.csdn.net/matrix_google/article/details/80676034?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4

1)查看远程仓库
git remote -v

2)配置原仓库的路径
git remote add upstream utrl

3)抓取原仓库的修改文件
git fetch upstream

4)合并远程原仓库与本地仓(先切换到master分支)
git merge upstream/master

5)同步fork远程仓
git push origin master

3)~4) can be replaced by 
git pull upstream master
