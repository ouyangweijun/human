#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-04 01:23
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : 08-面向对象设计.py
# @Desc     : 面向对象设计

# 面向对象设计
# 继承 - 是基于Python中的属性查找(如X.name)
# 多态 - 在X.method方法中，method的意义取决于X的类型
# 封装 - 方法和运算符实现行为，数据隐藏默认是一种惯例
# 参考实例
# 腾讯即时通信模块,初级封装

#! /usr/bin/env python
# coding: utf-8

import random
import time


class Message(object):

    def __init__(self, msgarr=[], toacc=''):
        self.msgbody = msgarr # 此处为MsgDict对象实例的列表或者空列表
        self.toacc = toacc # toacc为字符串(单发)或者列表(批量发)
        self.msgrandom = random.randint(1, 1000000000)
        self.msgrequest = {
            'To_Account': toacc, # 消息接收方账号
            'MsgRandom': self.msgrandom, # 消息随机数，由随机函数产生
            'MsgBody': [t.msg for t in msgarr]
        }

    def del_option(self, option):
        if option in (set(self.msgrequest)-set(['To_Account', 'MsgRandom', 'MsgBody'])):
            self.__dict__.pop(option)
            self.msgrequest.pop(option)

    def append_msg(self, msg):
        self.msgbody.append(msg)
        self.msgrequest['MsgBody'].append(msg.msg)

    def insert_msg(self, index, msg):
        self.msgbody.insert(index, msg)
        self.msgrequest['MsgBody'].insert(msg.msg)

    def del_msg(self, index):
        if index in range(len(self.msgbody)):
            del self.msgbody[index]
            del sel.msgrequest['MsgBody'][index]

    def set_from(self, fromacc):
        # 指定消息的发送方，默认为服务器发送
        self.fromacc = fromacc
        self.msgrequest['From_Account'] = fromacc

    def set_to(self, toacc):
        # 指定消息的接收方，可以为String(单发),可以为List(批量发送)
        self.toacc = toacc
        self.msgrequest['To_Account'] = toacc

    def refresh_random(self):
        self.msgrandom = random.randint(1, 1000000000)
        self.msgrequest['MsgRandom'] = self.msgrandom, # 消息随机数，由随机函数产生

    def set_sync(self, sync):
        # 同步选项：1, 把消息同步到From_Account在线终端和漫游上
        #           2, 消息不同步至From_Account
        #           若不填写，默认情况下会将消息同步
        #           仅在单发单聊消息中可调用
        self.sync = sync
        self.msgrequest['SyncOtherMachine'] = sync

    def set_timestamp(self):
        # 设置消息时间戳，unix时间, 仅在单发单聊消息中可以调用
        self.timestamp = int(time.time())
        self.msgrequest['MsgTimeStamp'] = self.timestamp

    def set_offlinepush(self, pushflag=0, desc='', ext='', sound=''):
        # 仅适用于APNa推送，不适用于安卓厂商推送
        self.msgrequest['OfflinePushInfo'] = {
            'PushFlag': pushflag,
            'Desc': desc,
            'Ext': ext,
            'Sound': sound
        }


class MsgDict(object):

    def __init__(self, msgtype='', msgcontent={}):
        self.msgtype = msgtype
        self.msgcontent = msgcontent

    @property
    def msg(self):
        return {
            'MsgType': self.msgtype,
            'MsgContent': self.msgcontent
        }

    def set_content(self, content):
        self.msgcontent = content


class TextMsg(MsgDict):

    def __init__(self, text='', msgtype='TIMTextElem'):
        self.text = text
        content = {'Text': text}
        super(TextMsg, self).__init__(msgtype=msgtype, msgcontent=content)

    def set_text(self, text):
        self.text = text
        self.msgcontent['Text'] = text


class LocationMsg(MsgDict):

    def __init__(self, desc='', latitude=0, longitude=0, msgtype='TIMLocationElem'):
        self.desc = desc
        self.latitude = latitude
        self.longitude = longitude
        content = {
            'Desc': desc,  # 地理位置描述信息, String
            'Latitude': latitude, # 纬度, Number
            'Longitude': longitude # 经度, Number
        }
        super(LocationMsg, self).__init__(msgtype=msgtype, msgcontent=content)

    def set_desc(self, desc):
        self.desc = desc
        self.msgcontent['Desc'] = desc

    def set_location(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.msgcontent['Latitude'] = latitude
        self.msgcontent['Longitude'] = longitude

    def set_latitude(self, latitude):
        self.latitude = latitude
        self.msgcontent['Latitude'] = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude
        self.msgcontent['Longitude'] = longitude


class FaceMsg(MsgDict):

    def __init__(self, index=1, data='', msgtype='TIMFaceElem'):
        self.index = index
        self.data = data
        content = {
            'Index': index, # 表情索引，用户自定义, Number
            'Data': data # 额外数据, String
        }
        super(TextMsg, self).__init__(msgtype=msgtype, msgcontent=content)

    def set_index(self, index):
        self.index = index
        self.msgcontent['Index'] = index

    def set_data(self, data):
        self.data = data
        self.msgcontent['Data'] = data


class CustomMsg(MsgDict):

    def __init__(self, data='', desc='', ext='', sound='', msgtype='TIMCustomElem'):
        self.data = data
        self.desc = desc
        self.ext = ext
        self.sound = sound
        content = {
            'Data': data, # 自定义消息数据。不作为APNS的payload中字段下发，故从payload中无法获取Data字段, String
            'Desc': desc, # 自定义消息描述，当接收方为iphone后台在线时，做ios离线Push时文本展示
            'Ext': ext, # 扩展字段，当接收方为ios系统且应用处在后台时，此字段作为APNS请求包Payloads中的ext键值下发，Ext的协议格式由业务方确定，APNS只做透传
            'Sound': sound # 自定义APNS推送铃声
        }
        super(CustomMsg, self).__init__(msgtype=msgtype, msgcontent=content)

    def set_data(self, data):
        self.data = data
        self.msgcontent['Data'] = data

    def set_desc(self, desc):
        self.desc = desc
        self.msgcontent['Desc'] = desc

    def set_ext(self, ext):
        self.ext = ext
        self.msgcontent['Ext'] = ext

    def set_sound(self, sound):
        self.sound = sound
        self.msgcontent['Sound'] = sound


class SoundMsg(MsgDict):

    def __init__(self, uuid='', size=0, second=0, msgtype='TIMSoundElem'):
        self.uuid = uuid
        self.size = size
        self.second = second
        content = {
            'UUID': uuid, # 语音序列号，后台用于索引语音的键值，String
            'Size': size, # 语音数据大小, Number
            'Second': second # 语音时长，单位秒 Number
        }
        super(SoundMsg, self).__init__(msgtype=msgtype, msgcontent=content)

    def set_uuid(self, uuid):
        self.uuid = uuid
        self.msgcontent['UUID'] = uuid

    def set_size(self, size):
        self.size = size
        self.msgcontent['Size'] = size

    def set_second(self, second):
        self.second = second
        self.msgcontent['Second'] = second


class ImageMsg(MsgDict):

    def __init__(self, uuid='', imgformat=0, imginfo=[], msgtype='TIMImageElem'):
        self.uuid = uuid
        self.imgformat = imgformat
        self.imginfo = imginfo
        content = {
            'UUID': uuid, # 图片序列号，后台用于索引语音的键值，String
            'ImageFormat': imgformat, # 图片格式， BMP=1, JPG=2, GIF=3, 其他=0, Number
            'ImageInfoArray': [t.info for t in imginfo] # 原图，缩略图或者大图下载信息, Array
        }
        super(ImageMsg, self).__init__(msgtype=msgtype, msgcontent=content)

    def set_uuid(self, uuid):
        self.uuid = uuid
        self.msgcontent['UUID'] = uuid

    def set_format(self, imgformat):
        self.imgformat = imgformat
        self.msgcontent['ImageFormat'] = imgformat

    def append_info(self, info):
        # info 为ImageInfo对象实例
        self.imginfo.append(info)
        self.msgcontnet['ImageInfoArray'].append(info.info)

    def insert_info(self, index, info):
        self.imginfo.insert(index, info)
        self.msgcontent['ImageInfoArray'].insert(index, info.info)

    def del_info(self, index):
        del self.imginfo[index]
        del self.msgcontent['ImageInfoArray'][index]


class FileMsg(MsgDict):

    def __init__(self, uuid='', size=0, name='', msgtype='TIMFileElem'):
        self.uuid = uuid
        self.size = size
        self.name = name
        content = {
            'UUID': uuid, # 文件序列号，后台用于索引语音的键值，String
            'FileSize': size, # 文件数据大小, Number
            'FileName': name # 文件名称/路径， String
        }
        super(FileMsg, self).__init__(msgtype=msgtype, msgcontent=content)

    def set_uuid(self, uuid):
        self.uuid = uuid
        self.msgcontent['UUID'] = UUID

    def set_size(self, size):
        self.size = size
        self.msgcontent['FileSize'] = size

    def set_name(self, name):
        self.name = name
        self.msgcontent['FileName'] = name


class ImageInfo(object):

    def __init__(self, itype=1, size=0, width=0, height=0, url=''):
        #图片类型， 1-原图， 2-大图， 3-缩略图, 0-其他
        self.itype = itype
        # 图片数据大小,Number
        self.size = size
        # 图片宽度,Number
        self.width = width
        # 图片高度, Number
        self.height = height
        # 图片下载地址,String
        self.url = url

    @property
    def info(self):
        return {
            'Type': self.itype,
            'Size': self.size,
            'Width': self.width,
            'Height': self.height,
            'URL': self.url
        }

    def set_type(self, itype):
        self.itype = itype

    def set_size(self, size):
        self.size = size

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_url(self, url):
        self.url = url
# 微信开发包，python实现, wechat_sdk开发
# http://wechat-python-sdk.com/
# 截取部分代码，学习类的设计


from __future__ import unicode_literals

import time

# from wechat_sdk.lib.crypto import BasicCrypto
# from wechat_sdk.lib.request import WechatRequest
# from wechat_sdk.exceptions import NeedParamError
# from wechat_sdk.utils import disable_urllib3_warning


class WechatConf(object):
    """ WechatConf 配置类

    该类将会存储所有和微信开发相关的配置信息, 同时也会维护配置信息的有效性.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs: 配置信息字典, 可用字典 key 值及对应解释如下:
                       'token': 微信 Token

                       'appid': App ID
                       'appsecret': App Secret

                       'encrypt_mode': 加解密模式 ('normal': 明文模式, 'compatible': 兼容模式, 'safe': 安全模式(默认))
                       'encoding_aes_key': EncodingAESKey 值 (传入此值必须保证同时传入 token, appid, 否则抛出异常)

                       'access_token_getfunc': access token 获取函数 (用于单机及分布式环境下, 具体格式参见文档)
                       'access_token_setfunc': access token 写入函数 (用于单机及分布式环境下, 具体格式参见文档)
                       'access_token_refreshfunc': access token 刷新函数 (用于单机及分布式环境下, 具体格式参见文档)
                       'access_token': 直接导入的 access token 值, 该值需要在上一次该类实例化之后手动进行缓存并在此处传入, 如果不
                                       传入, 将会在需要时自动重新获取 (传入 access_token_getfunc 和 access_token_setfunc 函数
                                       后将会自动忽略此处的传入值)
                       'access_token_expires_at': 直接导入的 access token 的过期日期, 该值需要在上一次该类实例化之后手动进行缓存
                                                  并在此处传入, 如果不传入, 将会在需要时自动重新获取 (传入 access_token_getfunc
                                                  和 access_token_setfunc 函数后将会自动忽略此处的传入值)

                       'jsapi_ticket_getfunc': jsapi ticket 获取函数 (用于单机及分布式环境下, 具体格式参见文档)
                       'jsapi_ticket_setfunc': jsapi ticket 写入函数 (用于单机及分布式环境下, 具体格式参见文档)
                       'jsapi_ticket_refreshfunc': jsapi ticket 刷新函数 (用于单机及分布式环境下, 具体格式参见文档)
                       'jsapi_ticket': 直接导入的 jsapi ticket 值, 该值需要在上一次该类实例化之后手动进行缓存并在此处传入, 如果不
                                       传入, 将会在需要时自动重新获取 (传入 jsapi_ticket_getfunc 和 jsapi_ticket_setfunc 函数
                                       后将会自动忽略此处的传入值)
                       'jsapi_ticket_expires_at': 直接导入的 jsapi ticket 的过期日期, 该值需要在上一次该类实例化之后手动进行缓存
                                                  并在此处传入, 如果不传入, 将会在需要时自动重新获取 (传入 jsapi_ticket_getfunc
                                                  和 jsapi_ticket_setfunc 函数后将会自动忽略此处的传入值)

                       'partnerid': 财付通商户身份标识, 支付权限专用
                       'partnerkey': 财付通商户权限密钥 Key, 支付权限专用
                       'paysignkey': 商户签名密钥 Key, 支付权限专用

                       'checkssl': 是否检查 SSL, 默认不检查 (False), 可避免 urllib3 的 InsecurePlatformWarning 警告
        :return:
        """

        self.__request = WechatRequest()

        if kwargs.get('checkssl') is not True:
            disable_urllib3_warning()  # 可解决 InsecurePlatformWarning 警告

        self.__token = kwargs.get('token')

        self.__appid = kwargs.get('appid')
        self.__appsecret = kwargs.get('appsecret')

        self.__encrypt_mode = kwargs.get('encrypt_mode', 'safe')
        self.__encoding_aes_key = kwargs.get('encoding_aes_key')
        self.__crypto = None
        self._update_crypto()

        self.__access_token_getfunc = kwargs.get('access_token_getfunc')
        self.__access_token_setfunc = kwargs.get('access_token_setfunc')
        self.__access_token_refreshfunc = kwargs.get('access_token_refreshfunc')
        self.__access_token = kwargs.get('access_token')
        self.__access_token_expires_at = kwargs.get('access_token_expires_at')

        self.__jsapi_ticket_getfunc = kwargs.get('jsapi_ticket_getfunc')
        self.__jsapi_ticket_setfunc = kwargs.get('jsapi_ticket_setfunc')
        self.__jsapi_ticket_refreshfunc = kwargs.get('jsapi_ticket_refreshfunc')
        self.__jsapi_ticket = kwargs.get('jsapi_ticket')
        self.__jsapi_ticket_expires_at = kwargs.get('jsapi_ticket_expires_at')

        self.__partnerid = kwargs.get('partnerid')
        self.__partnerkey = kwargs.get('partnerkey')
        self.__paysignkey = kwargs.get('paysignkey')

    @property
    def token(self):
        """ 获取当前 Token """
        self._check_token()
        return self.__token

    @token.setter
    def token(self, token):
        """ 设置当前 Token """
        self.__token = token
        self._update_crypto()  # 改动 Token 需要重新更新 Crypto

    @property
    def appid(self):
        """ 获取当前 App ID """
        return self.__appid

    @property
    def appsecret(self):
        """ 获取当前 App Secret """
        return self.__appsecret

    def set_appid_appsecret(self, appid, appsecret):
        """ 设置当前 App ID 及 App Secret"""
        self.__appid = appid
        self.__appsecret = appsecret
        self._update_crypto()  # 改动 App ID 后需要重新更新 Crypto

    @property
    def encoding_aes_key(self):
        """ 获取当前 EncodingAESKey """
        return self.__encoding_aes_key

    @encoding_aes_key.setter
    def encoding_aes_key(self, encoding_aes_key):
        """ 设置当前 EncodingAESKey """
        self.__encoding_aes_key = encoding_aes_key
        self._update_crypto()  # 改动 EncodingAESKey 需要重新更新 Crypto

    @property
    def encrypt_mode(self):
        return self.__encrypt_mode

    @encrypt_mode.setter
    def encrypt_mode(self, encrypt_mode):
        """ 设置当前加密模式 """
        self.__encrypt_mode = encrypt_mode
        self._update_crypto()

    @property
    def crypto(self):
        """ 获取当前 Crypto 实例 """
        return self.__crypto

    @property
    def access_token(self):
        """ 获取当前 access token 值, 本方法会自行维护 access token 有效性 """
        self._check_appid_appsecret()

        if callable(self.__access_token_getfunc):
            self.__access_token, self.__access_token_expires_at = self.__access_token_getfunc()

        if self.__access_token:
            now = time.time()
            if self.__access_token_expires_at - now > 60:
                return self.__access_token

        self.grant_access_token()  # 从腾讯服务器获取 access token 并更新
        return self.__access_token

    @property
    def jsapi_ticket(self):
        """ 获取当前 jsapi ticket 值, 本方法会自行维护 jsapi ticket 有效性 """
        self._check_appid_appsecret()

        if callable(self.__jsapi_ticket_getfunc):
            self.__jsapi_ticket, self.__jsapi_ticket_expires_at = self.__jsapi_ticket_getfunc()

        if self.__jsapi_ticket:
            now = time.time()
            if self.__jsapi_ticket_expires_at - now > 60:
                return self.__jsapi_ticket

        self.grant_jsapi_ticket()  # 从腾讯服务器获取 jsapi ticket 并更新
        return self.__jsapi_ticket

    @property
    def partnerid(self):
        """ 获取当前财付通商户身份标识 """
        return self.__partnerid

    @property
    def partnerkey(self):
        """ 获取当前财付通商户权限密钥 Key """
        return self.__partnerkey

    @property
    def paysignkey(self):
        """ 获取商户签名密钥 Key """
        return self.__paysignkey

    def grant_access_token(self):
        """
        获取 access token 并更新当前配置
        :return: 返回的 JSON 数据包 (传入 access_token_refreshfunc 参数后返回 None)
        """
        self._check_appid_appsecret()

        if callable(self.__access_token_refreshfunc):
            self.__access_token, self.__access_token_expires_at = self.__access_token_refreshfunc()
            return

        response_json = self.__request.get(
            url="https://api.weixin.qq.com/cgi-bin/token",
            params={
                "grant_type": "client_credential",
                "appid": self.__appid,
                "secret": self.__appsecret,
            },
            access_token=self.__access_token
        )
        self.__access_token = response_json['access_token']
        self.__access_token_expires_at = int(time.time()) + response_json['expires_in']

        if callable(self.__access_token_setfunc):
            self.__access_token_setfunc(self.__access_token, self.__access_token_expires_at)

        return response_json

    def grant_jsapi_ticket(self):
        """
        获取 jsapi ticket 并更新当前配置
        :return: 返回的 JSON 数据包 (传入 jsapi_ticket_refreshfunc 参数后返回 None)
        """
        self._check_appid_appsecret()

        if callable(self.__jsapi_ticket_refreshfunc):
            self.__jsapi_ticket, self.__jsapi_ticket_expires_at = self.__jsapi_ticket_refreshfunc()
            return

        response_json = self.__request.get(
            url="https://api.weixin.qq.com/cgi-bin/ticket/getticket",
            params={
                "type": "jsapi",
            },
            access_token=self.access_token,
        )
        self.__jsapi_ticket = response_json['ticket']
        self.__jsapi_ticket_expires_at = int(time.time()) + response_json['expires_in']

        if callable(self.__jsapi_ticket_setfunc):
            self.__jsapi_ticket_setfunc(self.__jsapi_ticket, self.__jsapi_ticket_expires_at)

        return response_json

    def get_access_token(self):
        """
        获取 Access Token 及 Access Token 过期日期, 仅供缓存使用, 如果希望得到原生的 Access Token 请求数据请使用 :func:`grant_token`
        **仅为兼容 v0.6.0 以前版本使用, 自行维护 access_token 请使用 access_token_setfunc 和 access_token_getfunc 进行操作**
        :return: dict 对象, key 包括 `access_token` 及 `access_token_expires_at`
        """
        self._check_appid_appsecret()

        return {
            'access_token': self.access_token,
            'access_token_expires_at': self.__access_token_expires_at,
        }

    def get_jsapi_ticket(self):
        """
        获取 Jsapi Ticket 及 Jsapi Ticket 过期日期, 仅供缓存使用, 如果希望得到原生的 Jsapi Ticket 请求数据请使用 :func:`grant_jsapi_ticket`
        **仅为兼容 v0.6.0 以前版本使用, 自行维护 jsapi_ticket 请使用 jsapi_ticket_setfunc 和 jsapi_ticket_getfunc 进行操作**
        :return: dict 对象, key 包括 `jsapi_ticket` 及 `jsapi_ticket_expires_at`
        """
        self._check_appid_appsecret()

        return {
            'jsapi_ticket': self.jsapi_ticket,
            'jsapi_ticket_expires_at': self.__jsapi_ticket_expires_at,
        }

    def _check_token(self):
        """
        检查 Token 是否存在
        :raises NeedParamError: Token 参数没有在初始化的时候提供
        """
        if not self.__token:
            raise NeedParamError('Please provide Token parameter in the construction of class.')

    def _check_appid_appsecret(self):
        """
        检查 AppID 和 AppSecret 是否存在
        :raises NeedParamError: AppID 或 AppSecret 参数没有在初始化的时候完整提供
        """
        if not self.__appid or not self.__appsecret:
            raise NeedParamError('Please provide app_id and app_secret parameters in the construction of class.')

    def _update_crypto(self):
        """
        根据当前配置内容更新 Crypto 类
        """
        if self.__encrypt_mode in ['compatible', 'safe'] and self.__encoding_aes_key is not None:
            if self.__token is None or self.__appid is None:
                raise NeedParamError('Please provide token and appid parameters in the construction of class.')
            self.__crypto = BasicCrypto(self.__token, self.__encoding_aes_key, self.__appid)
        else:
            self.__crypto = None
# 思维锻炼
# 设计讲师和学生类，讲师有上课，备课等方法，学生有听课，做练习等方法，均有姓名、性别、年龄等基本属性
# 设计聊天Message类