import os
import multiprocessing
import time
import random

def copy_file(file_name,old_folder_name,new_folder_name):
    """完成文件的复制"""

    #print("模拟拷贝文件：%s" % file_name)
    #print("模拟拷贝文件：从%s---》到%s 文件名是：%s" %(old_folder_name,new_folder_name,file_name))
    old_f=open(old_folder_name+'/'+file_name,'rb')
    contet_data=old_f.read()
    old_f.close()

    new_f=open(new_folder_name+'/'+file_name,'bw')
    new_f.write(contet_data)
    new_f.close()

    # 如果是拷贝完啦文件，那么就向队列中写入一个消息，表示已经完成

def main():
    """实现copy文件夹"""

    # 1.获取用户想要文件夹名称
    oldboy_folder_name="test"

    # 2.创建一个文件夹
    try:
        new_folder_name=oldboy_folder_name+'[复件]'
        os.mkdir(new_folder_name)
    except:
        pass
    # 3.获取文件夹的所有的待copy文件名字 listdir()
    file_names=os.listdir(oldboy_folder_name)
    #print(file_names)

    # 4.创建进程池，
    po=multiprocessing.Pool(6)

    # 5.创建一个队列
    q=multiprocessing.Manager().Queue()


    # 6.向进程池中添加copy文件的任务
    for file_name in file_names:
        po.apply_async(copy_file,args=(q,file_name,oldboy_folder_name,new_folder_name))
    po.close()
    #po.join()  # join是用来阻塞当前线程的

    # 守护进程实现
    all_file_num=len(file_names)  # 测一下有多少文件个数
    copy_ok_num=0

    while True:
        file_name=q.get()
        print("已经完成copy:%s" % file_name)
        copy_ok_num+=1
        print("\r拷贝文件的进度是：.2%f%%" % (copy_ok_num*100/all_file_num),end="")
        if copy_ok_num >= all_file_num:
            break
    print()
    # 复制源文件夹的文件，到新的文件夹中去

if __name__ == '__main__':
    main()
