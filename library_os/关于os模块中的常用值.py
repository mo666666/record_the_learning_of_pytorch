import os

################################################################
#                   1 获取当前的路径(.)                          #
################################################################
choose = False
if choose:
    print(os.curdir)
################################################################
#                   2 获取上层文件夹(..)                        #
################################################################
choose = False
if choose:
    print(os.pardir)
################################################################
#                   3 获取当前系统的分隔符(都是\)                #
################################################################
choose = False
if choose:
    print(os.sep)
################################################################
#                   4 获取文件名与后缀的分隔符(都是.)              #
################################################################
choose = False
if choose:
    print(os.extsep)

################################################################
#                   5 获取换行符号                               #
################################################################
choose = False
if choose:
    print(os.linesep)

################################################################
#                   6 相对目录与绝对目录                         #
################################################################
choose = False
if choose:
    open('../../a.txt', 'w')
