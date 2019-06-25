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
mongoConn = pymongo.MongoClient('10.5.79.51', 27017)
# mongoConn = pymongo.MongoClient('192.168.0.77', 27017)
vstore_db = mongoConn.vstore_db
subResource = vstore_db.subResource
fileResource = vstore_db.fileResource

mysqlConn = pymysql.connect(host='10.5.79.51',
                            user='sjl',
                            passwd='4574093',
                            db='spider',
                            charset='utf8')
# -----------------------------------------------------------------
mysqlConn.autocommit(1)
cursor = mysqlConn.cursor()


def isWhiteList(pkg_name):  # 白名单检查
    sql = 'select `pkg_name` from whitelist_app where `pkg_name` = \'' + str.lower(pkg_name) + '\';'
    cursor.execute(sql)
    return cursor.rowcount


# 查询是否已经在vstore里了
def mongoFind(id, name, packagename, version, versionCode):
    try:
        logging.info('id: ' + str(
            id) + ' name: ' + name + ' packagename:' + packagename + ' version: ' + version + ' versionCode: ' + str(
            versionCode))
    except Exception as e:
        logging.warning(e.__str__())
    i = subResource.find_one({'id': id})
    if not i:
        return (1, i)  # 库里没有,需要新增这个app
    else:
        if i['fileInfo']['androidAttributer']['versionName'] == version and str(i['fileInfo']['androidAttributer']['versionCode']).strip() == str(versionCode).strip():
            return (2, i)  # 正常,无需修改
        else:
            return (3, i)  # 有更新


def mongoDel(id):
    subResource.remove({'id': id})

# 删除fileRes表里的文件信息，防止重复插入
def mongoDel_fileResource(subId):
    fileResource.remove({'subId': subId})


def PRC(url):
    try:
        r = requests.get(url)
    except Exception as e:
        logging.warning('get error:' + url)
        return

    try:
        js = r.json()
    except Exception as e:
        logging.warning('json error: ' + url)
        return
    # js = requests.get(url).json()
    for i in js['data']['items']:
        t_category = i['category']
        t_description = i['description']
        t_devname = i['devname']
        t_downloadcount = i['downloadcount']
        t_downloadurl = i['downloadurl']
        t_editorcomment = i['editorcomment']
        t_icon = i['icon']
        t_id = i['id']
        t_name = i['name']
        t_packagename = i['packagename']
        t_releasedate = i['releasedate']
        t_score = i['score']
        t_screenshot = i['screenshot']
        t_size = i['size']
        t_subcategory = i['subcategory']
        t_tag = i['tag']
        t_version = i['version']
        t_versioncode = i['versioncode']

        # 不在白名单里,丢弃
        lock_mysql.acquire()
        whiteCount = isWhiteList(t_packagename)
        lock_mysql.release()
        if whiteCount == 0:
            logging.info('whiteName :' + t_packagename + ' not in')
            continue
        else:
            logging.info('whiteName : ' + t_packagename + 'in')

        o_id = ''
        # 查询是否已经存在,同时返回doc
        status, doc = mongoFind(t_id, t_name, t_packagename, t_version, t_versioncode)
        logging.info('mogofind status: ' + t_packagename + ' ' + str(status))
        if status == 3:  # 特殊处理,如果是3，则需要更新: 首先删除mongo中的doc，再设为需要add
            o_id = doc['_id']
            mongoDel(t_id)
            logging.info('update: ' + t_packagename)
            status = 1

        if status == 1:  # add
            appDir = tools.appDirMake(t_id, t_packagename, diskDir)  # 生成绝对路径
            logging.info(appDir)

            if tools.clearIdDir(appDir):  # 清空目标文件夹

                tList = tools.download(t_downloadurl, appDir)  # str
                t_downloadurl = tList[0]
                logging.info(t_downloadurl)

                tList = tools.download(t_icon, appDir)  # List
                t_icon = tList
                logging.info(t_icon)

                tList = tools.download(t_screenshot, appDir)  # List
                t_screenshot = tList
                logging.info(t_screenshot)

                post = tools.make_subResource_post(o_id,  # o_id ='' 或 ObjectId，post_make根据类型来决定生成post
                                                   t_category,
                                                   t_description,
                                                   t_devname,
                                                   t_downloadcount,
                                                   t_downloadurl,
                                                   t_editorcomment,
                                                   t_icon,
                                                   t_id,
                                                   t_name,
                                                   t_packagename,
                                                   t_releasedate,
                                                   t_score,
                                                   t_screenshot,
                                                   t_size,
                                                   t_subcategory,
                                                   t_tag,
                                                   t_version,
                                                   t_versioncode
                                                   )
                lock_mongo.acquire()
                logging.info(o_id)
                post_id = subResource.insert_one(post).inserted_id
                # 此处插入文件辅助信息doc,不然client读json少信息
                frsPost = tools.make_fileResource_post(post_id, post)
                mongoDel_fileResource(str(post_id))
                frs_id = fileResource.insert_one(frsPost).inserted_id
                lock_mongo.release()
            else:
                pass  # io 失败,下次再办
        elif status == 2:  # 正常无需更新
            continue


class Twork(threading.Thread):
    def __init__(self, url):
        super(Twork, self).__init__()
        self.url = url

    def run(self):
        semaphore.acquire()  # 阻塞
        logging.debug(self.url)
        PRC(self.url)
        semaphore.release()


if __name__ == "__main__":
    config = configparser.ConfigParser()  # 读取api地址
    config.read("config.ini")
    LeApiUrl = config.get("base", "url")
    diskDir = config.get("base", "diskDir")

    try:
        r = requests.get(LeApiUrl)
    except Exception as e:
        logging.warning(e.__str__())
        exit(1)
    else:
        pass

    result = r.json()
    TotalPages = result['data']['totalcount']  # 当前总app数量
    PageSize = int(TotalPages / 100) + 1  # 页数（100/页）

    semaphore = threading.BoundedSemaphore(10)
    lock_mysql = threading.Lock()
    lock_mongo = threading.Lock()

    td = []  # 线程存放处

    for i in range(0, 500):
        url = 'http://36.110.161.56:8080/ivvi_cms/api/app/list?pagesize=100&pageno=' + str(i + 1)
        t = Twork(url)
        td.append(t)
        t.start()

    for t in td:
        t.join()

    cursor.close()
    mysqlConn.close()
    mongoConn.close()
    logging.debug("run over!")
    exit(0)
