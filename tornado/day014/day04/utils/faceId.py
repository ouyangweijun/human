from aip import AipFace

""" 你的 APPID AK SK """
APP_ID = '15750965'
API_KEY = 'R8vFwISg2pARS8SjFtPKZElB'
SECRET_KEY = 'kd3amWfp3Ywap02Fx3PElwKI2Fhmxdwn'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


def face_register(image, userId, imageType='BASE64', groupId='user'):
    """
    调用百度的人脸注册接口
    :return:
    """
    """ 调用人脸注册 """
    res = client.addUser(image, imageType, groupId, userId)
    if res['error_code']:
        # 注册失败
        return False
    # 注册成功
    return True


def face_login(image, imageType='BASE64', groupId='user'):
    """
    调用百度的人脸检索接口
    """
    res = client.search(image, imageType, groupId)
    # {'error_code': 0, 'error_msg': 'SUCCESS', 'log_id': 1368654425495337131, 'timestamp': 1552549533, 'cached': 0, 'result': {'face_token': '34a78b7103e5d5a60bb539afba244321', 'user_list': [{'group_id': 'user', 'user_id': '4', 'user_info': '', 'score': 96.27961730957}]}}
    if res['error_code']:
        return False
    return True

