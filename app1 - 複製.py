from git import Repo
import os

dirfile = os.path.abspath('C:\Users\TibeMe_user\Desktop\cockroach_linebot_test') # code的文件位置，我默认将其存放在根目录下
repo = Repo(dirfile)

g = repo.git
g.add("--all")
g.commit("-m auto update")
g.push()
print("Successful push!")