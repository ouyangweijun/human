
from multiprocessing import Pool
import os
import multiprocessing



def copy_file(file_name,old_folder_name,new_folder_name):
    """完成文件的复制"""

    print("模拟拷贝文件：%s" % file_name)
    print("模拟拷贝文件：从%s---》到%s 文件名是：%s" %(old_folder_name,new_folder_name,file_name))
    old_f=open(old_folder_name+'/'+file_name,'rb')
    contet_data=old_f.read()
    old_f.close()

    new_f=open(new_folder_name+'/'+file_name,'bw')
    new_f.write(contet_data)
    new_f.close()

def main():
    """实现copy文件夹"""

    # 1.获取用户想要文件夹名称
    oldboy_folder_name="test"

    # 2.创建一个文件夹
    try:
        new_folder_name=oldboy_folder_name+'[复件]'
        os.mkdir(new_folder_name)
    except Exception as e:
        print(e)
        pass
    # 3.获取文件夹的所有的待copy文件名字 listdir()
    file_list=os.listdir(oldboy_folder_name)
    print(file_list)

    # 4.创建进程池，
    po=multiprocessing.Pool(6)


    # 5.向进程池中添加copy文件的任务
    for file_name in file_list:
        po.apply_async(copy_file,args=(file_name,oldboy_folder_name,new_folder_name))
    po.close()
    po.join()

    # 复制源文件夹的文件，到新的文件夹中去





if __name__ == '__main__':
    main()
