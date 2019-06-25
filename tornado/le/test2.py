import urllib
import requests
import re
from bs4 import BeautifulSoup
# url_ul = 'https://android-artworks.25pp.com/fs08/2016/07/06/3/2_52bac3dab6df7ed150fbd244897b6b18_con_130x130.png'
# url_ul = 'https://www.wandoujia.com/apps/com.kugou.android/download/dot?ch=detail_normal_dl'
# urllib.request.urlretrieve(url_ul, './kugou.apk')

def downIconfile(icon_url,id,package):
    import uuid
    #"down/39/com.tencent.mm/123262/a01d37ce815343538294623b344fdd11.png"
    #icon_url = 'https://www.wandoujia.com/apps/com.kugou.android/download/dot?ch=detail_normal_dl'

    # 第一步：获取文件
    img_response = requests.get(icon_url)

    # 第二步：设文件名
    filename = str(uuid.uuid4()) + '.png'

    import os
    path = '/home/vargo/下载/le/down/'+str(id)+'/'+package+'/'+str(id)+'/'
    comend = 'mkdir -p ' + path
    os.system(comend)
    # 第三步：保存文件

    with open(path+filename, 'wb') as f:
        f.write(img_response.content)

    # urllib.request.urlretrieve(icon_url,'./down/'+str(id)+'/'+package+'/'+str(id)+'/'+name)
    ic_addr = []
    insert_url ='down/'+str(id)+'/'+package+'/'+str(id)+'/' + filename
    ic_addr.append(insert_url)
    return  ic_addr



def downSnapshot(snapshot_url,id,package):
    id= 12
    import uuid
    snapshot_addr = []
    package  = 'com.mozinc.thunderstorm'
    c = ['https://android-screenimgs.25pp.com/fs08/2019/06/17/3/110_6c8768cf4e85dfc6a15c34291b765997_234x360.jpg',
     'https://android-screenimgs.25pp.com/fs08/2019/06/17/9/110_0c341e37d34ae5c8ee2fc475f77bb77a_234x360.jpg',
     'https://android-screenimgs.25pp.com/fs08/2019/06/17/6/110_09cdcead40c2a82d7083a5bbd6e0f126_234x360.jpg',
     'https://android-screenimgs.25pp.com/fs08/2019/06/17/0/110_9f760043e87e7184fb295a905560b6e4_234x360.jpg']
    lens = len(c)
    for i in range(lens):
        icon_url = c[i]
        #icon_url = 'https://www.wandoujia.com/apps/com.kugou.android/download/dot?ch=detail_normal_dl'
    #package = 'com.mozinc.thunderstorm'
    # 第一步：获取文件
        img_response = requests.get(icon_url)

    # 第二步：设文件名
        filename = str(uuid.uuid4()) + '.jpg'

        import os
        path = '/home/vargo/下载/le/down/' + str(id) + '/' + package + '/' + str(id) + '/'
        comend = 'mkdir -p ' + path
        os.system(comend)
    # 第三步：保存文件

        with open(path + filename, 'wb') as f:
            f.write(img_response.content)

    # urllib.request.urlretrieve(icon_url,'./down/'+str(id)+'/'+package+'/'+str(id)+'/'+name)

        insert_url = 'down/' + str(id) + '/' + package + '/' + str(id) + '/' + filename
        snapshot_addr.append(insert_url)
    return snapshot_addr

def downApkFiel(apk_url,package,id):
    import uuid

    #"down/39/com.tencent.mm/123262/a01d37ce815343538294623b344fdd11.png"
    icon_url = 'https://www.wandoujia.com/apps/com.kugou.android/download/dot?ch=detail_normal_dl'
    package = 'com.mozinc.thunderstorm'
    # 第一步：获取文件
    apk_response = requests.get(apk_url)
    id = '12'
    # 第二步：设文件名
    filename = package+'.apk'

    import os
    path = '/home/vargo/下载/le/down/' + str(id) + '/' + package + '/' + str(id) + '/'
    comend = 'mkdir -p ' + path
    os.system(comend)
    # 第三步：保存文件

    with open(path + filename, 'wb') as f:
        f.write(apk_response.content)

    # urllib.request.urlretrieve(icon_url,'./down/'+str(id)+'/'+package+'/'+str(id)+'/'+name)
    apk_addr = []
    insert_url ='down/'+str(id)+'/'+package+'/'+str(id)+'/' + filename
    apk_addr.append(insert_url)
    return apk_addr








if __name__ == '__main__':
    # a = downIconfile('https://android-artworks.25pp.com/fs08/2016/06/08/3/1_56d25deec71482c1fbd99806e8eddbb2_con_130x130.png','123','com.mozinc.thunderstorm')
    # print(a)
    b = downSnapshot()