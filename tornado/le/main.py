# -*- coding:utf-8 -*-
import configparser
import tools
import requests
import pymysql
import pymongo
import logging
import threading
import time
import os
import csv
import urllib
import requests
import re
import uuid
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import pandas as pd

from threading import current_thread
import sys

sys.setrecursionlimit(1000000)

from gevent import monkey
monkey.patch_all()

import gevent


repath = "D:\\human\\tornado\\le\\down\\"

# LOG
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='log.log',
                    filemode='a')
# 同时输出到控制台
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# -----------------------------------------------------------------
# mongoConn = pymongo.MongoClient('192.168.50.121', 27017)
# # mongoConn = pymongo.MongoClient('192.168.0.77', 27017)
# vstore_db = mongoConn.vstore_db
# subResource = vstore_db.subResource
# fileResource = vstore_db.fileResource

# mysqlConn = pymysql.connect(host='10.5.79.51',
#                             user='sjl',
#                             passwd='4574093',
#                             db='spider',
#                             charset='utf8')
# # -----------------------------------------------------------------
# mysqlConn.autocommit(1)
# cursor = mysqlConn.cursor()


# def isWhiteList(pkg_name):  # 白名单检查
#     sql = 'select `pkg_name` from whitelist_app where `pkg_name` = \'' + str.lower(pkg_name) + '\';'
#     cursor.execute(sql)
#     return cursor.rowcount


# 查询是否已经在vstore里了
# def mongoFind(id, name, packagename, version, versionCode):
#     try:
#         logging.info('id: ' + str(
#             id) + ' name: ' + name + ' packagename:' + packagename + ' version: ' + version + ' versionCode: ' + str(
#             versionCode))
#     except Exception as e:
#         logging.warning(e.__str__())
#     i = subResource.find_one({'id': id})
#     if not i:
#         return (1, i)  # 库里没有,需要新增这个app
#     else:
#         if i['fileInfo']['androidAttributer']['versionName'] == version and str(
#                 i['fileInfo']['androidAttributer']['versionCode']).strip() == str(versionCode).strip():
#             return (2, i)  # 正常,无需修改
#         else:
#             return (3, i)  # 有更新
#
#
# def mongoDel(id):
#     subResource.remove({'id': id})
#
#
# # 删除fileRes表里的文件信息，防止重复插入
# def mongoDel_fileResource(subId):
#     fileResource.remove({'subId': subId})


def start_file(i):
    # print(i)
    ss = 'app名称,英文名称,一级分类,安装人数,软件大小,头像地址,描述,新版本截图,开发者,apk下载地址,软件短评,版本号'
    # a0 = i[0]  # app名称
    # a1 = i[1]  # 英文名称
    # a2 = i[2]  # 一级分类
    # a3 = i[3]  # 安装人数
    # a4 = i[4]  #  软件大小
    # a5 = i[5]  # 头像地址
    # a6 = i[6]  # 描述
    # a7 = i[7]  # 新版本截图
    # a8 = i[8]  # 开发者
    # a9 = i[9]  # apk下载地址
    # a10 = i[10]  # 软件短评
    # a11 = i[11]  # 版本号
    # # a12 = i[11]  #
    # j +=1
    #
    # t_category = '软件'  # 软件  写死的
    # t_description = i[6]  # 描述
    # t_devname = i[8]  # 开发者
    # t_downloadcount = i[3]  # 下载量
    # t_downloadurl = i[9]  # 下载地址
    # t_editorcomment = i[10]  # 软件短评
    # t_icon = i[5]  # 头像
    # t_id = 100  # id
    # t_name = i[0]  # 软件名称
    # t_packagename = i[1]  # 英文名称
    # t_releasedate = '2019-10-10'  # 更新时间
    # t_score = 5  # 评价星星
    # t_screenshot = i[7]  # 截图
    # t_size = i[4]  # 软件大小
    # t_subcategory = i[2]  # 一级分类
    # t_tag = i[2]  # 标签 一级分类
    # t_version = i[11]  # 版本
    # t_versioncode = i[11]  #  版本code

    if i[0] == "app名称":
        pass
    else:
        # for i in js['data']['items']:

        #  原来的
        # t_category = i['category'] # 软件  写死的
        # t_description = i['description']  # 描述
        # t_devname = i['devname']  # 开发者
        # t_downloadcount = i['downloadcount']  # 下载量
        # t_downloadurl = i['downloadurl']  # 下载地址
        # t_editorcomment = i['editorcomment']  # 软件短评
        # t_icon = i['icon']  # 头像
        # t_id = i['id']  # id
        # t_name = i['name']  # 软件名称
        # t_packagename = i['packagename']  # 英文名称
        # t_releasedate = i['releasedate']  # 更新时间
        # t_score = i['score']  # 评价星星
        # t_screenshot = i['screenshot']  #截图
        # t_size = i['size']  # 软件大小
        # t_subcategory = i['subcategory']  # 二级分类
        # t_tag = i['tag']  # 标签 二级分类
        # t_version = i['version']   # 版本
        # t_versioncode = i['versioncode']  #

        #  一下是更新的
        t_category = '软件'  # 软件  写死的
        t_description = i[6]  # 描述
        t_devname = i[8]  # 开发者
        t_editorcomment = i[10]  # 软件短评
        t_id = 100  # id
        t_name = i[0]  # 软件名称
        t_packagename = i[1]  # 英文名称
        t_releasedate = '2019-6-16'  # 更新时间
        t_score = 5  # 评价星星
        # t_screenshot = i[7]  # 截图
        # 处理软件大小
        t_size = i[4]  # 软件大小
        if t_size.endswith('KB'):
            t_size = (t_size[:-2].split('.')[0]) * 1024
        elif t_size.endswith('MB'):
            t_size = int(t_size[:-2].split('.')[0]) * 1024 * 1024
        t_subcategory = i[2]  # 一级分类
        t_tag = i[2]  # 标签 一级分类
        t_version_temp = i[11]  # 版本
        # t_versioncode = i[11]  #  版本code

        # 处理版本和处理版本code
        try:
            a13 = t_version_temp.strip()
            ssd = int(a13[-1])
            sa = int(a13[0])
        except Exception as e:
            a13 = '1.2.1'
        t_version = t_version_temp  # 版本
        t_versioncode = t_version.replace('.', '0')  # 版本code

        # 处理下载量
        t_downloadcount = i[3]  # 下载量
        if t_downloadcount.endswith('万人安装'):
            # print(a3)
            t_downloadcount = int(t_downloadcount[:-4].split('.')[0]) * 10000
        elif t_downloadcount.endswith('亿人安装'):
            t_downloadcount = int(t_downloadcount[:-4].split('.')[0]) * 100000000
            # print()
        elif t_downloadcount.endswith("人安装"):
            t_downloadcount = int(t_downloadcount[:-3].split('.')[0]) * 1

        # 获取包名,id号码
        id = i[12]

        #  单独处理头像
        t_icon = []
        t_icon_temp = i[5]  # 头像
        package = t_packagename
        ic_url = downIconfile(t_icon_temp, id, package)
        t_icon.append(ic_url)
        # 单独处理下截图

        t_screenshot_temp = i[7].strip("[]").split(',')
        t_screenshot = []
        for l in t_screenshot_temp:
            # print(eval(l))
            t_screenshot.append(eval(l))
        t_screenshots = downSnapshot(t_screenshot, id, package)
        t_screenshot = t_screenshots

        t_downloadurl = i[9]  # 下载地址
        temp_downurl = downApkFiel(t_downloadurl, id, package)
        t_downloadurl = temp_downurl

        # 特殊处理 qq下载问题
        # pos = t_downloadurl.find('imtt.dd.qq.com')
        # if (pos > 0):
        #     continue
        #### 微信需要处理

        # 不在白名单里,丢弃
        # lock_mysql.acquire()
        # whiteCount = isWhiteList(t_packagename)
        # # lock_mysql.release()
        # if whiteCount == 0:
        #     logging.info('whiteName :' + t_packagename + ' not in')
        #     continue
        # else:
        #     logging.info('whiteName : ' + t_packagename + 'in')

        o_id = ''
        # 查询是否已经存在,同时返回doc
        # status, doc = mongoFind(t_id, t_name, t_packagename, t_version, t_versioncode)
        # logging.info('mogofind status: ' + t_packagename + ' ' + str(status))
        # if status == 3:  # 特殊处理,如果是3，则需要更新: 首先删除mongo中的doc，再设为需要add
        #     o_id = doc['_id']
        #     mongoDel(t_id)
        #     logging.info('update: ' + t_packagename)
        #     status = 1
        status = 1
        if status == 1:  # add
            pass
            # appDir = tools.appDirMake(t_id, t_packagename, diskDir)  # 生成绝对路径
            # logging.info(appDir)

            # if tools.clearIdDir(appDir):  # 清空目标文件夹
            #
            #     tList = tools.download(t_downloadurl, appDir)  # str
            #     t_downloadurl = tList[0]
            #     logging.info(t_downloadurl)
            #
            #     tList = tools.download(t_icon, appDir)  # List
            #     t_icon = tList
            #     logging.info(t_icon)
            #
            #     tList = tools.download(t_screenshot, appDir)  # List
            #     t_screenshot = tList
            #     logging.info(t_screenshot)

            # post = tools.make_subResource_post(o_id,  # o_id ='' 或 ObjectId，post_make根据类型来决定生成post
            #                                    t_category,
            #                                    t_description,
            #                                    t_devname,
            #                                    t_downloadcount,
            #                                    t_downloadurl,
            #                                    t_editorcomment,
            #                                    t_icon,
            #                                    t_id,
            #                                    t_name,
            #                                    t_packagename,
            #                                    t_releasedate,
            #                                    t_score,
            #                                    t_screenshot,
            #                                    t_size,
            #                                    t_subcategory,
            #                                    t_tag,
            #                                    t_version,
            #                                    t_versioncode
            #                                    )
            # # lock_mongo.acquire()
            # logging.info(o_id)
            # post_id = subResource.insert_one(post).inserted_id
            # # 此处插入文件辅助信息doc,不然client读json少信息
            # frsPost = tools.make_fileResource_post(post_id, post)
            # mongoDel_fileResource(str(post_id))
            # frs_id = fileResource.insert_one(frsPost).inserted_id
            # lock_mongo.release()
        #     else:
        #         pass  # io 失败,下次再办
        # elif status == 2:  # 正常无需更新
        #     continue
#
def PRC():
    # try:
    #     r = requests.get(url)
    # except Exception as e:
    #     logging.warning('get error:' + url)
    #     return

    # try:
    #     js = r.json()
    # except Exception as e:
    #     logging.warning('json error: ' + url)
    #     return
    # js = requests.get(url).json()

    with open('wandoujia_app_cat_6.csv', 'r+', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    j = 1


    g_lst = []
    for i in rows:
        g = gevent.spawn(start_file,i)
        g_lst.append(g)
    gevent.joinall(g_lst)

# class Twork(threading.Thread):
#     def __init__(self, url):
#         super(Twork, self).__init__()
#         self.url = url
#
#     def run(self):
#         semaphore.acquire()  # 阻塞
#         logging.debug(self.url)
#         PRC(self.url)
#         semaphore.release()



def downIconfile(icon_url,id,package):
    import uuid
    #"down/39/com.tencent.mm/123262/a01d37ce815343538294623b344fdd11.png"
    #icon_url = 'https://www.wandoujia.com/apps/com.kugou.android/download/dot?ch=detail_normal_dl'

    # 第一步：获取文件
    img_response = requests.get(icon_url)

    # 第二步：设文件名
    filename = str(uuid.uuid4()) + '.png'

    import os
    # '/home/vargo/下载/le/down/'
    path = repath+str(id)+'/'+package+'/'+str(id)+'/'

    comend = 'mkdir -p ' + path
    os.system(comend)
    # 第三步：保存文件

    with open(path+filename, 'wb') as f:
        f.write(img_response.content)

    # urllib.request.urlretrieve(icon_url,'./down/'+str(id)+'/'+package+'/'+str(id)+'/'+name)
    ic_addr = []
    insert_url ='down/'+str(id)+'/'+package+'/'+str(id)+'/' + filename
    ic_addr.append(insert_url)
    return  ic_addr[0]


def downSnapshot(snapshot_url,id,package):
    #id= 12
    snapshot_addr = []
    #package  = 'com.mozinc.thunderstorm'
    # c = ['https://android-screenimgs.25pp.com/fs08/2019/06/17/3/110_6c8768cf4e85dfc6a15c34291b765997_234x360.jpg',
    #  'https://android-screenimgs.25pp.com/fs08/2019/06/17/9/110_0c341e37d34ae5c8ee2fc475f77bb77a_234x360.jpg',
    #  'https://android-screenimgs.25pp.com/fs08/2019/06/17/6/110_09cdcead40c2a82d7083a5bbd6e0f126_234x360.jpg',
    #  'https://android-screenimgs.25pp.com/fs08/2019/06/17/0/110_9f760043e87e7184fb295a905560b6e4_234x360.jpg']
    lens = len(snapshot_url)
    for i in range(lens):
        snap_url = snapshot_url[i]
    # 第一步：获取文件
        img_response = requests.get(snap_url)

    # 第二步：设文件名
        filename = str(uuid.uuid4()) + '.jpg'

        import os
        path = repath+str(id)+'/'+package+'/'+str(id)+'/'
        comend = 'mkdir -p ' + path
        os.system(comend)
    # 第三步：保存文件

        with open(path + filename, 'wb') as f:
            f.write(img_response.content)

        insert_url = 'down/' + str(id) + '/' + package + '/' + str(id) + '/' + filename
        snapshot_addr.append(insert_url)
    return snapshot_addr

def downApkFiel(apk_url,id,package):
    import uuid

    #"down/39/com.tencent.mm/123262/a01d37ce815343538294623b344fdd11.png"
    #icon_url = 'https://www.wandoujia.com/apps/com.kugou.android/download/dot?ch=detail_normal_dl'
    #package = 'com.mozinc.thunderstorm'
    # 第一步：获取文件
    apk_response = requests.get(apk_url)
    #id = '12'
    # 第二步：设文件名
    filename = package+'.apk'

    import os
    path = repath+str(id)+'/'+package+'/'+str(id)+'/'
    comend = 'mkdir -p ' + path
    os.system(comend)
    # 第三步：保存文件

    with open(path + filename, 'wb') as f:
        f.write(apk_response.content)

    # urllib.request.urlretrieve(icon_url,'./down/'+str(id)+'/'+package+'/'+str(id)+'/'+name)
    apk_addr = []
    insert_url ='down/'+str(id)+'/'+package+'/'+str(id)+'/' + filename
    apk_addr.append(insert_url)
    return apk_addr[0]




if __name__ == "__main__":
    config = configparser.ConfigParser()  # 读取api地址
    config.read("config.ini")
    LeApiUrl = config.get("base", "url")
    diskDir = config.get("base", "diskDir")

    # semaphore = threading.BoundedSemaphore(10)
    # lock_mysql = threading.Lock()
    # lock_mongo = threading.Lock()
    #
    # td = []  # 线程存放处

    # for i in range(0, 500):
    #     url = 'http://36.110.161.56:8080/ivvi_cms/api/app/list?pagesize=100&pageno=' + str(i + 1)
    #     t = Twork(url)
    #     td.append(t)
    #     t.start()
    #
    # for t in td:
    #    t.join()

    # cursor.close()
    # mysqlConn.close()
    start = PRC()
    mongoConn.close()
    logging.debug("run over!")
    exit(0)
