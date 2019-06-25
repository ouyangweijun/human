# -*- coding:utf-8 -*-
import logging
import datetime
import time
import os
import shutil
import hashlib
import re
import requests
import types


# http://www.cnblogs.com/God-Li/p/7732407.html 线程
# 修正apk类型的中文名称
def fixFrameResType(fameName):
    if fameName == '新闻阅读' or fameName == '资讯阅读':
        return '资讯阅读'
    elif fameName == '便捷生活' or fameName == '生活实用':
        return '生活实用'
    elif fameName == '网上购物' or fameName == '购物理财':
        return '购物理财'
    elif fameName == '交通出行' or fameName == '旅游出行':
        return '旅行出行'
    elif fameName == '健康医疗' or fameName == '医疗健康':
        return '医疗健康'
    elif fameName == '育儿母婴' or fameName == '医疗健康':
        return '医疗健康'
    elif fameName == '图像影音' or fameName == '影音播放':
        return '影音播放'
    elif fameName == '办公商务' or fameName == '办公学习':
        return '办公学习'
    elif fameName == '金融理财' or fameName == '购物理财':
        return '购物理财'
    elif fameName == '系统性能' or fameName == '系统工具':
        return '系统工具'
    elif fameName == '学习教育' or fameName == '办公学习':
        return '办公学习'
    elif fameName == '手机美化' or fameName == '拍摄美化':
        return '拍摄美化'
    elif fameName == '聊天社交' or fameName == '社交通信' or fameName == '通信社交' or fameName == '社交通讯' or fameName == '电话通讯':
        return '社交通讯'
    elif fameName == '系统安全' or fameName == '系统工具':
        return '系统工具'
    elif fameName == '生活服务' or fameName == '生活实用':
        return '生活实用'
    elif fameName == '经营策略' or fameName == '休闲益智' or fameName == '角色扮演' or fameName == '棋牌桌游' or fameName == '体育竞速' or fameName == '动作策略' or fameName == '飞行射击' or fameName == '模拟辅助':
        return '热门游戏'
    else:
        return '其他'


#
#   工具frame中文，获取对应的11大分类
#
def getFrameResID(fameName):
    if fameName == '旅游出行':
        return '4d134da209324e4b0bc30e25'
    elif fameName == '拍摄美化':
        return '4d134da209324e4b0dc30e25'
    elif fameName == '资讯阅读':
        return '4d134da209324e4b0fc30e25'
    elif fameName == '生活实用':
        return '4d134da209324e4b11c30e25'
    elif fameName == '购物理财':
        return '4d134da209324e4b13c30e25'
    elif fameName == '系统工具':
        return '4d134da209324e4b17c30e25'
    elif fameName == '影音播放':
        return '4d134da209324e4b18c30e25'
    elif fameName == '社交通讯':
        return '4d134da209324e4b19c30e25'
    elif fameName == '办公学习':
        return '4d134da209324e4b1ac30e25'
    elif fameName == '热门游戏':
        return '59b95c52e238fe8364ba1b61'
    elif fameName == '医疗健康':
        return '59b97fc8e238fe8364ba1b62'
    else:
        # 其他分类里面的
        return '888888a209324e4b1ac30e25'


def make_subResource_post(o_id,
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
                          t_versioncode,
                          ):
    t_subcategory = fixFrameResType(t_subcategory)  # 修正11大分类

    t_frameResID = getFrameResID(t_subcategory)
    t_size = str(t_size)  # 不然手机端不显示尺寸

    if o_id == '':
        post = {
            "_class": "spider.model.SubResource",
            "billingChannel": "4becd6e89a26a447e417adc6",
            "billingModel": "4bece838e11ba447711a31ee",
            "channels": [
                {
                    "channelId": "50175e69c8575eda7b2195eb"
                },
                {
                    "channelId": "514bf8fa7bb1b6f9da06b993"
                },
                {
                    "channelId": "5163af9f7bb1fe0a7a9ab9ca"
                }
            ],
            "colorTags": [],
            "cp": t_devname,
            "displayLanguage": "1",
            "fileInfo": {
                "androidAttributer": {
                    "packageName": t_packagename,
                    "versionCode": str(t_versioncode).strip(),
                    "versionName": t_version
                },
                "path": t_downloadurl,
                "name": t_packagename + '.apk',
                "size": t_size,
                "format": "android"
            },
            "frameList": [
                {
                    "frameId": "4eafa51f4624d6aae600f57e",
                    "defaulted": False,
                    "resTypeId": t_frameResID
                }
            ],
            "gameRes": {
                "ver": t_version,
                "age": 18,
                "language": "中文",
                "region": "中国"
            },
            "handleModeSupport": {
                "remoteControl": True,
                "joypad": True,
                "motionController": False
            },
            "icons": t_icon,
            "identifier": "0",
            "index": 0,
            "keyword": [
                # "通信社交"
                t_tag
            ],
            "modelList": [
                {
                    "modelId": "4eafa7b359e44404ba444924",
                    "modelCode": "android",
                    "adapteType": "android全机型"
                },
                {
                    "modelId": "5034997fd749db6cbf0f91c7",
                    "modelCode": "240320a10",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91c8",
                    "modelCode": "240320a21",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91c9",
                    "modelCode": "240320a22",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91ca",
                    "modelCode": "240320a23",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91cb",
                    "modelCode": "240400a22",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91cc",
                    "modelCode": "320480a21",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91cd",
                    "modelCode": "320480a22",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91ce",
                    "modelCode": "320480a23",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91cf",
                    "modelCode": "480800a15",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d0",
                    "modelCode": "480800a20",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d1",
                    "modelCode": "480800a21",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d2",
                    "modelCode": "480800a22",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d3",
                    "modelCode": "480800a23",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d4",
                    "modelCode": "480800a40",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d5",
                    "modelCode": "540960a15",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d6",
                    "modelCode": "540960a40",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d7",
                    "modelCode": "1280800a20",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d8",
                    "modelCode": "1280800a21",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d9",
                    "modelCode": "1280800a22",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91da",
                    "modelCode": "1280800a23",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91db",
                    "modelCode": "1280800a30",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91dc",
                    "modelCode": "1280800a31",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91dd",
                    "modelCode": "1280800a40",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91de",
                    "modelCode": "1024600a15",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91df",
                    "modelCode": "1024600a16",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91e0",
                    "modelCode": "1024600a21",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91e1",
                    "modelCode": "1024600a22",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91e2",
                    "modelCode": "1024600a23",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91e3",
                    "modelCode": "6001024a23",
                    "adapteType": ""
                },
                {
                    "modelId": "5035ee967bb1388553231022",
                    "modelCode": "7201280a40",
                    "adapteType": ""
                },
                {
                    "modelId": "5035eeda7bb1388553231023",
                    "modelCode": "8001280a23",
                    "adapteType": ""
                },
                {
                    "modelId": "5035eef97bb1388553231024",
                    "modelCode": "8001280a40",
                    "adapteType": ""
                }
            ],
            "previewMaps": t_screenshot,
            "price": 0,
            "productDesc": t_description,
            "productTag": t_tag,
            "products": [
                {
                    "productId": "59ae427a11705d83248089f9",
                    "status": 1,
                    "lastModifyTime": datetime.datetime.now(),
                    "lastModifyTimestamp": int(time.time() * 1000),
                    "lastModifyUser": "4bf237d0910ecc629d8380a3"
                }
            ],
            "profitPercentage": "0",
            "provide": t_devname,
            "resId": "54ab7cada3101681843d2f4c",  # 不明参数
            "resNature": "4bfe6b7320227f35d31fdf32",
            "resSerialNumber": "20170915042000_5281841",
            "serialNumber": "20170915042000_52818410",
            "sort": "Game",
            "source": "/cms_searcher",
            "star": t_score,
            "statusInfo": {
                "cmsUserId": "5628552b11702699627d591e",
                "createTime": datetime.datetime.now(),
                "lastUserId": "5628552b11702699627d591e",
                "lastModifyTime": datetime.datetime.now(),
                "synchronizationStatus": "1",
                "lastModifyTimestamp": int(time.time() * 1000),
                "applyStatus": "1",
                "rejectStatus": "0"
            },
            "unitPrice": 0,
            "categoryName": t_subcategory,
            "downloadCount": t_downloadcount,
            "name": t_name,
            "id": t_id,
            "extComment": t_editorcomment,
            "category": t_category
        }
    else:
        post = {
            "_id": o_id,
            "_class": "spider.model.SubResource",
            "billingChannel": "4becd6e89a26a447e417adc6",
            "billingModel": "4bece838e11ba447711a31ee",
            "channels": [
                {
                    "channelId": "50175e69c8575eda7b2195eb"
                },
                {
                    "channelId": "514bf8fa7bb1b6f9da06b993"
                },
                {
                    "channelId": "5163af9f7bb1fe0a7a9ab9ca"
                }
            ],
            "colorTags": [],
            "cp": t_devname,
            "displayLanguage": "1",
            "fileInfo": {
                "androidAttributer": {
                    "packageName": t_packagename,
                    "versionCode": str(t_versioncode).strip(),
                    "versionName": t_version
                },
                "path": t_downloadurl,
                "name": t_packagename + '.apk',
                "size": t_size,
                "format": "android"
            },
            "frameList": [
                {
                    "frameId": "4eafa51f4624d6aae600f57e",
                    "defaulted": False,
                    "resTypeId": t_frameResID
                }
            ],
            "gameRes": {
                "ver": t_version,
                "age": 18,
                "language": "中文",
                "region": "中国"
            },
            "handleModeSupport": {
                "remoteControl": True,
                "joypad": True,
                "motionController": False
            },
            "icons": t_icon,
            "identifier": "0",
            "index": 0,
            "keyword": [
                # "通信社交"
                t_tag
            ],
            "modelList": [
                {
                    "modelId": "4eafa7b359e44404ba444924",
                    "modelCode": "android",
                    "adapteType": "android全机型"
                },
                {
                    "modelId": "5034997fd749db6cbf0f91c7",
                    "modelCode": "240320a10",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91c8",
                    "modelCode": "240320a21",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91c9",
                    "modelCode": "240320a22",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91ca",
                    "modelCode": "240320a23",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91cb",
                    "modelCode": "240400a22",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91cc",
                    "modelCode": "320480a21",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91cd",
                    "modelCode": "320480a22",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91ce",
                    "modelCode": "320480a23",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91cf",
                    "modelCode": "480800a15",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d0",
                    "modelCode": "480800a20",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d1",
                    "modelCode": "480800a21",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d2",
                    "modelCode": "480800a22",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d3",
                    "modelCode": "480800a23",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d4",
                    "modelCode": "480800a40",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d5",
                    "modelCode": "540960a15",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d6",
                    "modelCode": "540960a40",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d7",
                    "modelCode": "1280800a20",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d8",
                    "modelCode": "1280800a21",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91d9",
                    "modelCode": "1280800a22",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91da",
                    "modelCode": "1280800a23",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91db",
                    "modelCode": "1280800a30",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91dc",
                    "modelCode": "1280800a31",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91dd",
                    "modelCode": "1280800a40",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91de",
                    "modelCode": "1024600a15",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91df",
                    "modelCode": "1024600a16",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91e0",
                    "modelCode": "1024600a21",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91e1",
                    "modelCode": "1024600a22",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91e2",
                    "modelCode": "1024600a23",
                    "adapteType": ""
                },
                {
                    "modelId": "5034997fd749db6cbf0f91e3",
                    "modelCode": "6001024a23",
                    "adapteType": ""
                },
                {
                    "modelId": "5035ee967bb1388553231022",
                    "modelCode": "7201280a40",
                    "adapteType": ""
                },
                {
                    "modelId": "5035eeda7bb1388553231023",
                    "modelCode": "8001280a23",
                    "adapteType": ""
                },
                {
                    "modelId": "5035eef97bb1388553231024",
                    "modelCode": "8001280a40",
                    "adapteType": ""
                }
            ],
            "previewMaps": t_screenshot,
            "price": 0,
            "productDesc": t_description,
            "productTag": t_tag,
            "products": [
                {
                    "productId": "59ae427a11705d83248089f9",
                    "status": 1,
                    "lastModifyTime": datetime.datetime.now(),
                    "lastModifyTimestamp": int(time.time() * 1000),
                    "lastModifyUser": "4bf237d0910ecc629d8380a3"
                }
            ],
            "profitPercentage": "0",
            "provide": t_devname,
            "resId": "54ab7cada3101681843d2f4c",  # 不明参数
            "resNature": "4bfe6b7320227f35d31fdf32",
            "resSerialNumber": "20170915042000_5281841",
            "serialNumber": "20170915042000_52818410",
            "sort": "Game",
            "source": "/cms_searcher",
            "star": t_score,
            "statusInfo": {
                "cmsUserId": "5628552b11702699627d591e",
                "createTime": datetime.datetime.now(),
                "lastUserId": "5628552b11702699627d591e",
                "lastModifyTime": datetime.datetime.now(),
                "synchronizationStatus": "1",
                "lastModifyTimestamp": int(time.time() * 1000),
                "applyStatus": "1",
                "rejectStatus": "0"
            },
            "unitPrice": 0,
            "categoryName": t_subcategory,
            "downloadCount": t_downloadcount,
            "name": t_name,
            "id": t_id,
            "extComment": t_editorcomment,
            "category": t_category
        }
    return post


#
#  app_id post 完整的插入 subResource 里的doc

#
#

def make_fileResource_post(post_id, post):
    frsPost = {
        "_class": "spider.model.FileResource",
        "subId": str(post_id),
        "name": "1",
        "sort": "Game",
        "billingChannel": "1",
        "icons": post['icons'],
        "keyword": [
            "职业",
            "角色"
        ],
        "modelList": [
            {
                "modelId": "4eafa7b359e44404ba444924",
                "modelCode": "android",
                "adapteType": "android全机型"
            },
            {
                "modelId": "5034997fd749db6cbf0f91c7",
                "modelCode": "240320a10",
                "adapteType": ""
            },
            {
                "modelId": "5034997fd749db6cbf0f91c8",
                "modelCode": "240320a21",
                "adapteType": ""
            }
        ],
        "fileInfo": {
            "androidAttributer": {
                "packageName": post['fileInfo']['androidAttributer']['packageName'],
                "versionCode": str(post['fileInfo']['androidAttributer']['versionCode']).strip(),
                "versionName": post['fileInfo']['androidAttributer']['versionName']
            },
            "path": post['fileInfo']['path'],
            "name": post['fileInfo']['name'],
            "size": post['fileInfo']['size'],
            "format": "android"
        },
        "frameList": [
            {
                "frameId": "4eafa51f4624d6aae600f57e",
                "defaulted": False,
                "resTypeId": post['frameList'][0]['resTypeId']
            }
        ],
        "cp": "未知",
        "isCrawlingCms": True
    }
    return frsPost


def clearIdDir(appDir):
    try:
        if os.path.exists(appDir):
            shutil.rmtree(appDir)
        else:
            pass
        os.makedirs(appDir)
        return True
    except:
        logging.INFO('io error: ' + appDir)
        return False


# 根据id、报名、大路径名生成 app存放路径
def appDirMake(t_id: object, t_packagename: object, diskDir: object) -> object:
    md5 = tomd5(t_packagename)
    appDir = diskDir + '/' + getPre2Int(md5) + '/' + str.rstrip(t_packagename) + '/' + str(t_id) + '/'
    return appDir


def tomd5(str):
    try:
        md5Str = hashlib.md5(str.encode("utf-8")).hexdigest()
        return md5Str
    except:
        return '00000000000000000000000000000000'


def getPre2Int(md5):
    num = re.sub('\D', '', md5)
    if num == '':
        return '00'
    else:
        return num[0:2]


def getUrlFileName(url):
    fileName = os.path.basename(url)
    return fileName


# 规范乐视url转向问题
# http://ka.letvstore.com/dl/SP/com.sina.weibo/3472/
def getUrlLocation(url):
    r = requests.get(url, allow_redirects=False)
    if r.status_code == 302:
        url = r.headers['Location']
    else:
        url = ''
    return url


def fixUrl(url):
    try:
        n = url.index('&')
        url = url[0:n]
    except:
        pass

    try:
        n = url.index('?')
        url = url[0:n]
    except:
        pass

    if url[-1] == '/':
        url = getUrlLocation(url)
        try:
            n = url.index('&')
            url = url[0:n]
        except:
            pass

        try:
            n = url.index('?')
            url = url[0:n]
        except:
            pass
    return url


# 一次down一个
def download_1(url, appDir):
    logging.debug('1:--- :' + url)
    url = fixUrl(url)
    logging.debug('2:--- :' + url)
    fileName = getUrlFileName(url)
    logging.debug('appDir= ' + appDir + ' fileName= ' + fileName + ' url=' + url)

    for i in range(10):
        try:
            r = requests.get(url)
        except Exception as e:
            if i >= 9:
                logging.warning((e.__str__()))
                return None
            else:
                time.sleep(1)
                continue
        else:
            time.sleep(0.1)
            logging.info('For ' + i.__str__() + ' break')
            break

    with open(appDir + fileName, 'wb') as fp:
        try:
            fp.write(r.content)
        except Exception as e:
            logging.debug('IO error:' + appDir + fileName)

    downName = appDir + fileName
    return downName[24:]


# down list 或 url. tList 为接收参数
def download(url, appDir):
    tList = []
    if url == None:
        logging.warning('url is None!')
        return tList

    if isinstance(url, list):
        for tmp in url:
            rFileName = download_1(tmp, appDir)
            tList.append(rFileName)
    else:
        rFileName = download_1(url, appDir)
        tList.append(rFileName)
    return tList
