import os

################################################
#            1 将相对路径转换为绝对路径           #
################################################
choose = False
if choose:
    path1 = '../../关于环境变量的.py'
    result = os.path.abspath(path1)
    print(result)
################################################
#            2 获取路径的主体与前面的路径部分      #
################################################
choose = False
if choose:
    path1 = os.getcwd()
    print(os.path.basename(path1))
    print(os.path.dirname(path1))
################################################
#            3  连接两个路径                    #
################################################
choose = False
if choose:
    path1 = os.getcwd()
    name1 = (os.path.basename(path1))
    name2 = os.path.dirname(path1)
    print(os.path.join(name2, name1))
################################################
#            4  拆分两个路径(拆成路径与主体部分）  #
################################################
choose = False
if choose:
    path1 = os.getcwd()
    print(os.path.split(path1))

################################################
#            5  拆分两个路径(后缀与路径）         #
################################################
choose = False
if choose:
    path1 = os.getcwd()
    print(os.path.splitext(path1))

################################################
#            6  获取文件的大小                   #
################################################
choose = False
if choose:
    path1 = 'C:/Users/apple/Desktop/解决os的问题/record_the_learning_of_pytorch/library_os/关于工作目录1.PNG'
    print(os.path.getsize(path1))
################################################
#            7  检测                            #
################################################
choose = False
if choose:
    path1 = 'C:/Users/apple/Desktop/解决os的问题/record_the_learning_of_pytorch/library_os/关于工作目录1.PNG'
    print(os.path.isfile(path1))  # 是不是文件
    print(os.path.isdir(path1))  # 是不是工作目录
    print(os.path.islink(path1))  # 是不是链接（仅仅限于Linux）
    print(os.path.isabs(path1))  # 是不是绝对路径
################################################
#            8  关于时间的方法                   #
################################################
choose = False
if choose:
    path1 = 'C:/Users/apple/Desktop/解决os的问题/record_the_learning_of_pytorch/library_os/关于工作目录1.PNG'
    print(os.path.getctime(path1))  # 获取创建的时间
    print(os.path.getmtime(path1))  # 获取上一次修改的时间
    print(os.path.getatime(path1))  # 获取上一次访问的时间
    # 返回的是创建的时间戳
################################################
#            9  判断文件或者文件夹是不是存在       #
################################################
choose = False
if choose:
    path1 = 'C:/Users/apple/Desktop/解决os的问题/record_the_learning_of_pytorch/library_os/关于工作目录1.PNG'
    print(os.path.exists(path1))
################################################
#            10 判断是不是同一个路径              #
################################################
choose = True
if choose:
    path1 = 'C:/Users/apple/Desktop/解决os的问题/record_the_learning_of_pytorch/library_os/关于工作目录1.PNG'
    path2 = './关于工作目录1.PNG'
    print(os.path.samefile(path1, path2))