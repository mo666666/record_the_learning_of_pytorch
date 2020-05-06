import os

################################################################
#                     1    关于系统路径                         #
################################################################
choose = False
if choose:
    os.chdir('C:/Users/apple/Desktop/解决os的问题/record_the_learning_of_pytorch/library_os/新建')  # 改变当前的工作目录
    result = os.getcwd()  # 获取当前的工作目录
    open('a.txt', 'w')
    print(result)

################################################################
#                     2    关于文件夹的信息                      #
################################################################
choose = False
if choose:
    print(os.listdir('C:/Users/apple/Desktop/解决os的问题/record_the_learning_of_pytorch/library_os/新建'))

################################################################
#                     3    创建文件夹                           #
################################################################
choose = False
if choose:
    os.mkdir('C:/Users/apple/Desktop/解决os的问题/record_the_learning_of_pytorch/library_os/A')

################################################################
#                     4    递归创建文件夹                        #
################################################################
choose = False
if choose:
    os.makedirs('C:/Users/apple/Desktop/解决os的问题/record_the_learning_of_pytorch/library_os/try/a/b')

################################################################
#                     5    删除空文件夹                         #
################################################################
choose = False
if choose:
    os.rmdir('C:/Users/apple/Desktop/解决os的问题/record_the_learning_of_pytorch/library_os/try/a/b')

################################################################
#                     6    递归删除空文件夹                      #
################################################################
choose = False
if choose:
    os.removedirs('C:/Users/apple/Desktop/解决os的问题/record_the_learning_of_pytorch/library_os/try/a')
#  注意：删除的路径一定要是最底层的路径，然后上面的空文件夹会依次删除

################################################################
#                     7    重命名空文件夹                        #
################################################################
choose = False
if choose:
    os.rename('C:/Users/apple/Desktop/解决os的问题/record_the_learning_of_pytorch/library_os/关于工作目录一.PNG',
              'C:/Users/apple/Desktop/解决os的问题/record_the_learning_of_pytorch/library_os/关于工作目录1.PNG')

################################################################
#                     8    查看文件的性质                        #
################################################################
choose = False
if choose:
    print(os.stat('C:/Users/apple/Desktop/解决os的问题/record_the_learning_of_pytorch/library_os/关于工作目录1.PNG'))