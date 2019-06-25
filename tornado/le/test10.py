import requests
from bs4 import BeautifulSoup
import pandas as pd

# 获取各个分类的url
data = requests.get('https://www.wandoujia.com/category/app')
s = BeautifulSoup(data.text, "html.parser")
divs = [li.div.find_all('a') for li in s.find_all('div')[4].find_all('ul')[0].find_all('li')]
divs_two = [li.div.find_all('a', attrs={"class": "cate-link"}) for li in
            s.find_all('div')[4].find_all('ul')[0].find_all('li')]

divss = [li.find_all('a', attrs={"class": "cate-link"}) for li in s.find_all('div')[4].find_all('ul')[0].find_all('li')]
# print(divss)
# print(divs)
urls_dict = {}
# for i in range(len(divs)): #
#     #print(divs[i])
#     for j in range(len(divs[i])):
#         title = divs[i][j].attrs['title']
#         url = divs[i][j].attrs['href']
#         urls_dict[title] = url


# urls_dict1 = {}
for i in range(len(divss)):  #
    # print(divs[i])
    for j in range(len(divss[i])):
        title = divss[i][j].attrs['title']
        url = divss[i][j].attrs['href']
        urls_dict[title] = url

# 获取软件分类

base_url = 'https://www.wandoujia.com/wdjweb/api/category/more?catId='
apps = {}  # 软件名称
apps_install = {}  # 安装数量
apps_lenpackage = {}  # 软件大小
apps_en = {}  # 软件英文名称

app_addrss = {}  # 地址
app_head = {}  # 头像地址
app_start = {}  # 点赞数量
app_desc = {}  # 描述
app_snap = {}  # 新版本截图
dev_sites = {}  # 开发着
app_down = {}  # apk 下载地址
shot_coment = {}  # 短评
app_version = {}  # 版本号
app_id = {}  # app id
app_vcode = {}  # app vcode
app_vsersion_new = {}  # 新版本

# 创建空数据框，保存到本地
# apps_df = pd.DataFrame(columns=[ 'app名称','一级分类', '安装人数','软件大小','头像地址','描述','新版本截图','开发者','apk下载地址','软件短评','版本号'])


for key in urls_dict.keys():
    # print(key)
    #    key = '视频'
    print(key)
    # if key == '影音播放':
    #     pass
    # elif key =='系统工具':
    #     pass
    #
    # elif key == '通讯社交':
    #     pass
    #
    # elif key == '手机美化':
    #     pass
    #
    # elif key == '新闻阅读':
    #     pass
    #
    # elif key == '摄影图像':
    #     pass
    #
    # elif key == '考试学习':
    #     pass
    #
    # elif key == '网上购物':
    #     pass
    # elif key == '金融理财':
    #     pass
    # elif key == '生活休闲':
    #     pass
    # elif key == '旅游出行':
    #     pass
    # elif key == '健康运动':
    #     pass
    # elif key == '办公商务':
    #     pass
    # else:
    if key != '融理财' or key != '公商务':
        num = 1
        page_last = False
        catid = urls_dict[key].split('/')[4].split('_')[0]

        # subCatId = urls_dict[key].split('/')[4].split('_')[1]
        subCatId = 0  # 全部是0

        title_list = []  # 名称
        title_en_list = []  # 英文名称
        cat_second_list = []  # 二级分类
        install_list = []  # 安装人数
        package_len_list = []  # 软件大小

        app_addrss_url_list = []  # 地址

        app_head_url_list = []  # 头像地址
        # app_start_nul_url_list = []  # 点赞数量
        app_desc_list = []  # 描述
        app_snap_list = []  # 新版本截图
        dev_sites_list = []  # 开发着
        app_down_url = []  # apk 下载地址
        shot_coment_list = []  # 短评
        app_version_list = []  # 版本号
        image_len_list = []  # 临时头像
        app_id_list = []  # app_id
        app_vcode_list = []  # app vcode
        app_vsersion_new_list = []  # 新版本

        while not page_last:  # 每个分类最后一页停止
            # 拼接出每页的url，点击加载更多，page会增1
            url = 'https://www.wandoujia.com/wdjweb/api/category/more?catId={}&subCatId={}&page={}&ctoken=4Op4yfsiSsr8OAzRt5b1MtwE'.format(
                catid, subCatId, num)
            # print(url)
            # print(url)
            # 爬取对应的网页
            data = requests.get(url)
            # print(data)
            # 解析出json
            json = data.json()
            # print(json)
            content = json['data']['content']

            # print(content)
            if content != '':  # 判断是否最后一页
                soup = BeautifulSoup(content, "html.parser")

                # 获取到下载地址
                app_addrss_url_list = []
                app_addrss_url_list.extend([li.find_all('a')[0].attrs['href'] for li in soup.find_all('li')])

                for i in app_addrss_url_list:
                    data1 = requests.get(i)
                    soup1 = BeautifulSoup(data1.text, 'html.parser')
                    # try:
                    #     name =[lia.find_all('img')[0].attrs['alt'] for lia in soup1.find_all(name='div',class_='icon-wrap')][0]
                    #     print(name)
                    # except Exception:
                    #     pass
                    # img = [lia.find_all('img')[0].attrs['src'] for lia in soup1.find_all(name='div',class_='icon-wrap')]
                    # try:
                    #     app_head_url_list.append([lia.find_all('img')[0].attrs['src'] for lia in soup1.find_all(name='div',class_='icon-wrap')][0])
                    # except Exception:
                    #     app_head_url_list.append([lia.find_all('img')[0].attrs['src'] for lia in soup1.find_all(name='div', class_='app-icon')][0])

                    # 获取简介
                    # desc.extend([la.find_all('div',{'itemprop':"description"})[0].attrs['div'] for la in soup1.find_all(name='div',class_='desc-info')])
                    # desc.extend([soup1.find_all(name='div', class_='desc-info')])
                    # descript =([soup1.find_all(name='div', class_='desc-info')])
                    # if name == '支付宝':
                    #     descript = soup1.find_all(name='div', class_='desc-info')[0].find_all(name='div')[1].text
                    #     app_desc_list.append(descript)

                    # 获取简介
                    # try:
                    #     name =[lia.find_all('img')[0].attrs['alt'] for lia in soup1.find_all(name='div',class_='icon-wrap')][0]
                    #     print('1')
                    #     print(name)
                    # except:
                    #     name =[lia.find_all('span',class_='name') for lia in soup1.find_all(name='div', class_='app-info')][0]
                    #     print(name)
                    # print(2)
                    # if name == '福彩双色球彩票':

                    # 获取描述
                    try:
                        temp_desc = []
                        descript = soup1.find_all(name='div', class_='desc-info')[0].find_all(name='div', class_='con')[
                            0].get_text()
                        temp_desc.append(descript)
                        app_desc_list.append(temp_desc[0])
                    except Exception:
                        # try:
                        #     name =[lia.find_all('img')[0].attrs['alt'] for lia in soup1.find_all(name='div',class_='icon-wrap')][0]
                        #     print(name)
                        # ss = soup1.find_all(name='div', class_='desc-info')[0]
                        # descript = soup1.find_all(name='div', class_='desc-info')[0].find_all(name='div')[0].text
                        temp_desc = []
                        # descript = soup1.find_all(name='div', class_='desc-info')[0].find_all(name='div')[1].text
                        temp_desc.append('未知')
                        app_desc_list.append(temp_desc[0])
                        pass

                        # app_desc_list.append('未知')
                        # except Exception:
                        #     pass

                    # 获取截图

                    # snapshot.extend([lia.find_all('img')[0].attrs['src'] for lia in soup1.find_all(name='div', class_='screenshot')])
                    cut_img_list = []
                    for lia in soup1.find_all(name='div', class_='screenshot'):
                        # a = lia.find_all('img')[0].attrs['src']
                        a = lia.find_all('img', {'class': 'screenshot-img'})
                        lenth = len(a)
                        for j in range(lenth):
                            # image_url =a[j].attrs['src']
                            cut_img_list.append(a[j].attrs['src'])
                    app_snap_list.append(cut_img_list)

                    # level = soup1.find(name='i', attrs={"class": "score-current"}).attrs['style']
                    # app_start_nul_url_list.append(level)

                    # 获取开发者
                    # dev_sites = soup1.find(name='span', attrs={"class": "dev-sites"}).text
                    # temp_dev = []
                    try:
                        temp_desc.append(soup1.find(name='span', attrs={"class": "dev-sites"}).text)

                        dev_sites_list.append(soup1.find(name='span', attrs={"class": "dev-sites"}).text)
                    except Exception:
                        # temp_dev.append('未知')
                        dev_sites_list.append('未知')
                        pass
                    # 下载地址
                    # app_down = soup1.find_all('a',attrs={"class":"normal-dl-btn"})[0].attrs['href']
                    try:
                        app_down_url.append(soup1.find_all('a', attrs={"class": "normal-dl-btn"})[0].attrs['href'])
                    except Exception:
                        app_down_url.append('未知')
                        pass

                    # 获取版本号
                    # a =soup1.find_all(name='dl', attrs={"class": "infos-list"})[0].find_all(name='dd')[3].text

                    # temp_ver = []
                    try:

                        dtname = soup1.find_all(name='dl', attrs={"class": "infos-list"})[0].find_all(name='dt')[3].text
                        if '要求' == dtname:
                            # app_version_list.append(soup1.find_all(name='dl', attrs={"class": "infos-list"})[0].find_all(name='dd')[2].text)
                            # temp_ver.append(soup1.find_all(name='dl', attrs={"class": "infos-list"})[0].find_all(name='dd')[2].text)
                            app_version_list.append(
                                soup1.find_all(name='dl', attrs={"class": "infos-list"})[0].find_all(name='dd')[2].text)
                            # print(soup1.find_all(name='dl', attrs={"class": "infos-list"})[0].find_all(name='dd')[2].text)
                        elif '版本' == dtname:
                            # print(soup1.find_all(name='dl', attrs={"class": "infos-list"})[0].find_all(name='dd')[3].text)

                            # temp_ver.append(soup1.find_all(name='dl', attrs={"class": "infos-list"})[0].find_all(name='dd')[3].text)
                            app_version_list.append(
                                soup1.find_all(name='dl', attrs={"class": "infos-list"})[0].find_all(name='dd')[3].text)
                    except:
                        pass
                    # print('1')
                    # .find_all(name='dd')[5]

                    # 获取app_id
                    sa = soup1.find_all('div', attrs={'class': 'download-wp'})[0].find_all(name='a', attrs={
                        "class": "install-btn i-source"})[0].attrs['data-app-id']
                    app_id_list.append(sa)


                    # 获取到vcode
                    app_vcode_list.append(soup1.find_all('div', attrs={'class': 'download-wp'})[0].
                                          find_all(name='a', attrs={"class": "install-btn i-source"})[0].attrs['data-app-vcode'])

                    # 获取新版本data-app-vname
                    app_vsersion_new_list.append(soup1.find_all('div', attrs={'class': 'download-wp'})[0].
                                          find_all(name='a', attrs={"class": "install-btn i-source"})[0].attrs['data-app-vname'])
                    # print('1')
                app_addrss_url_list = []
                # 获取app的名称
                title_list.extend([li.find_all('a')[1].attrs['title'] for li in soup.find_all('li')])
                # 获取app的二级分类
                cat_second_list.extend(
                    [li.find_all('a', {'class': "tag-link"})[0].string for li in soup.find_all('li')])
                # 获取app的安装人数
                install_list.extend(
                    [li.find_all('span', {'class': "install-count"})[0].string for li in soup.find_all('li')])
                # 获取到apk 大小
                package_len_list.extend([li.find_all('span', )[2].string for li in soup.find_all('li')])

                # image_len_list.extend()

                # 获取短评论
                shot_coment_list.extend(
                    [li.find_all('div', {'class': "comment"})[0].string for li in soup.find_all('li')])

                # 获取头像
                app_head_url_list.extend([li.find_all('img')[0].attrs['data-original'] for li in soup.find_all('li')])

                # 获取英文名称

                title_en_list.extend(
                    [li.find_all('a', {'class': 'detail-check-btn'})[0].attrs['data-app-pname'] for li in
                     soup.find_all('li')])

                # title_en_list.extend()

                # # 保存到字典
                apps[key] = dict(zip(title_list, cat_second_list))  # 名称
                apps_en[key] = dict(zip(title_list, title_en_list))  # 英文名称
                apps_install[key] = dict(zip(title_list, install_list))  # 安装量
                apps_lenpackage[key] = dict(zip(title_list, package_len_list))  # 安装包大小

                # app_addrss[key] = dict(zip(title_list, cat_second_list))  # 地址
                app_head[key] = dict(zip(title_list, app_head_url_list))  # 头像地址
                # app_start[key] = dict(zip(title_list, cat_second_list))  # 点赞数量
                app_desc[key] = dict(zip(title_list, app_desc_list))  # 描述
                app_snap[key] = dict(zip(title_list, app_snap_list))  # 新版本截图
                dev_sites[key] = dict(zip(title_list, dev_sites_list))  # 开发着
                app_down[key] = dict(zip(title_list, app_down_url))  # apk 下载地址
                shot_coment[key] = dict(zip(title_list, shot_coment_list))  # 短评
                app_version[key] = dict(zip(title_list, app_version_list))  # 版本号
                app_id[key] = dict(zip(title_list,app_id_list))  # id 号码
                app_vcode[key] = dict(zip(title_list,app_vcode_list))  # app vcode
                app_vsersion_new[key] = dict(zip(title_list,app_vsersion_new_list)) # 新版本

                # 加载下一页
                num = num + 1
                # if num == 2:
                #     break

            if num == 5:
                page_last = True
        # else:
        #     # 触发则表示当前分类已经加载所有页面，即到最后一页
        #     page_last = True
        # if num == 2:
        #     break

# 创建空数据框，保存到本地
apps_df = pd.DataFrame(
    columns=['app名称', '英文名称', '一级分类', '安装人数', '软件大小', '头像地址', '描述', '新版本截图', '开发者', 'apk下载地址', '软件短评', '版本号','id号码','vcode','新版本号'])
# app_ls = []  # app名称
# cat_ls = []  # 二级分类
# ins_ls = []  # 安装人数
# len_ls = []  # 软件大小
# head_url_ls =[]  # 头像地址
# #start_url_ls = []  # 点赞数
# desc_ls = [] # 完整描述
# snap_ls = []  # 新版本截图
# dev_sites_ls = []  # 开发者
# app_down_ls = []  # apk 下载地址
# app_shot_commt_ls = []  # 简短描述
# app_version_ls = []  # 版本号
# 将字典解析出来保存到数据框
for key in apps.keys():
    print(key)
    app_ls = []  # app名称
    app_en_ls = []  # 英文名称
    cat_ls = []  # 二级分类
    ins_ls = []  # 安装人数
    len_ls = []  # 软件大小
    head_url_ls = []  # 头像地址
    # start_url_ls = []  # 点赞数
    desc_ls = []  # 完整描述
    snap_ls = []  # 新版本截图
    dev_sites_ls = []  # 开发者
    app_down_ls = []  # apk 下载地址
    app_shot_commt_ls = []  # 简短描述
    app_version_ls = []  # 版本号
    app_id_ls = [] # id 号码
    app_vcode_ls =[]  # vcode
    app_vsersion_new_ls = []  # 新版本号码

    for app in apps[key].keys():
        print(app)
        app_ls.append(app)
        app_en_ls.append(apps_en[key][app])
        cat_ls.append(apps[key][app])
        ins_ls.append(apps_install[key][app])
        len_ls.append(apps_lenpackage[key][app])
        head_url_ls.append(app_head[key][app])
        desc_ls.append(app_desc[key][app])
        snap_ls.append(app_snap[key][app])  # 新版本截图
        dev_sites_ls.append(dev_sites[key][app])  # 开发者
        app_down_ls.append(app_down[key][app])  # apk 下载地址
        app_shot_commt_ls.append(shot_coment[key][app])  # 短评
        app_id_ls.append(app_id[key][app])   # id 号码
        app_vcode_ls.append(app_vcode[key][app])  # vcode
        app_vsersion_new_ls.append(app_vsersion_new[key][app])  # 新版本号码


        if app == '透明屏幕搞怪':
            print(app_version)
        try:
            app_version_ls.append(app_version[key][app])
        except Exception:
            app_version_ls.append('1.2')
            pass

    apps_df_tmp = pd.DataFrame(
        {'app名称': app_ls, '英文名称': app_en_ls, '一级分类': key, '安装人数': ins_ls, '软件大小': len_ls, '头像地址': head_url_ls,
         '描述': desc_ls, '新版本截图': snap_ls, '开发者': dev_sites_ls, 'apk下载地址': app_down_ls, '软件短评': app_shot_commt_ls,
         '版本号': app_version_ls,'id号码':app_id_ls,'vcode':app_vcode_ls,'新版本号':app_version_ls})
    apps_df = apps_df.append(apps_df_tmp)
    # print(apps_df_tmp)

# 导出
apps_df.to_csv('wandoujia_app_cat_6.csv', index=False)
print(apps_df)
