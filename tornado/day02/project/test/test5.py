import requests
from bs4 import BeautifulSoup
import pandas as pd
#获取各个分类的url
data = requests.get('https://www.wandoujia.com/category/app')
s = BeautifulSoup(data.text, "html.parser")
divs = [li.div.find_all('a') for li in s.find_all('div')[4].find_all('ul')[0].find_all('li')]
urls_dict = {}
for i in range(len(divs)): #
    #print(divs[i])
    for j in range(len(divs[i])):
        title = divs[i][j].attrs['title']
        url = divs[i][j].attrs['href']
        urls_dict[title] = url


# 获取软件分类

base_url = 'https://www.wandoujia.com/wdjweb/api/category/more?catId='
apps = {}
apps_install = {}
apps_lenpackage = {}
for key in urls_dict.keys():
    # print(key)
    #    key = '视频'
    num = 1
    page_last = False
    catid = urls_dict[key].split('/')[4].split('_')[0]
    subCatId = urls_dict[key].split('/')[4].split('_')[1]
    title_list = []  # 名称
    cat_second_list = []  # 二级分类
    install_list = []  # 安装人数
    package_len_list = []  # 软件大小
    app_addrss_url_list = []  # 地址
    app_head_url_list = [] # 头衔地址
    app_start_nul_url_list = []  # 点赞数量
    app_desc_list = []
    app_snap_list = []
    while not page_last:  # 每个分类最后一页停止
        # 拼接出每页的url，点击加载更多，page会增1
        url = 'https://www.wandoujia.com/wdjweb/api/category/more?catId={}&subCatId={}&page={}&ctoken=4Op4yfsiSsr8OAzRt5b1MtwE'.format(
            catid, subCatId, num)
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
            app_addrss_url_list.extend([li.find_all('a')[0].attrs['href'] for li in soup.find_all('li')])

            for i in app_addrss_url_list:
                # print(i)
                #soup1 = BeautifulSoup(i, "html.parser")
                data1 = requests.get(i)
                # print(data1)
                #json1 = data1.json()
                #print(json1)
                #content1 = json1['data']['content']
                #print(content1)
                #if content1:
                #    soup1 = BeautifulSoup(content1,'html.parser')
                soup1 = BeautifulSoup(data1.text, 'html.parser')

                name =[lia.find_all('img')[0].attrs['alt'] for lia in soup1.find_all(name='div',class_='icon-wrap')][0]
                temp_list=[]
                img = [lia.find_all('img')[0].attrs['src'] for lia in soup1.find_all(name='div',class_='icon-wrap')]
                temp_list.append(name)
                app_head_url_list.extend(img)

                # 获取简介

                desc = []

                #desc.extend([la.find_all('div',{'itemprop':"description"})[0].attrs['div'] for la in soup1.find_all(name='div',class_='desc-info')])
                #desc.extend([soup1.find_all(name='div', class_='desc-info')])
                descript =([soup1.find_all(name='div', class_='desc-info')])

                desc.append(name)
                desc.append(descript)
                app_desc_list.extend(desc)

                # 获取截图

                snapshot = []
                snapshot.append(name)
                snapshot.extend([lia.find_all('img')[0].attrs['src'] for lia in soup1.find_all(name='div', class_='screenshot')])
                for lia in soup1.find_all(name='div', class_='screenshot'):
                    #a = lia.find_all('img')[0].attrs['src']
                    a = lia.find_all('img',{'class':'screenshot-img'})
                    for j in a:
                        print(j.find('img').attrs['src'])
                    # print(a)
                    print('1')
                print('1')





            # print(app_addrss_url)

            # 获取app的名称
            title_list.extend([li.find_all('a')[1].attrs['title'] for li in soup.find_all('li')])
            # 获取app的二级分类
            cat_second_list.extend([li.find_all('a', {'class': "tag-link"})[0].string for li in soup.find_all('li')])
            # 获取app的安装人数
            install_list.extend([li.find_all('span', {'class': "install-count"})[0].string for li in soup.find_all('li')])
            # 获取到apk 大小
            package_len_list.extend([li.find_all('span',)[2].string for li in soup.find_all('li')])

            # 保存到字典
            apps[key] = dict(zip(title_list, cat_second_list))
            apps_install[key] = dict(zip(title_list, install_list))
            apps_lenpackage[key] = dict(zip(title_list, package_len_list))
            # 加载下一页
            num = num + 1
        else:
            # 触发则表示当前分类已经加载所有页面，即到最后一页
            page_last = True

# 创建空数据框，保存到本地
apps_df = pd.DataFrame(columns=['一级分类', '二级分类', 'app名称', '安装人数','软件大小'])
app_ls = []
cat_ls = []
ins_ls = []
len_ls = []
# 将字典解析出来保存到数据框
for key in apps.keys():
    for app in apps[key].keys():
        app_ls.append(app)
        cat_ls.append(apps[key][app])
        ins_ls.append(apps_install[key][app])
        len_ls.append(apps_lenpackage[key][app])

    apps_df_tmp = pd.DataFrame({'app名称': app_ls, '二级分类': cat_ls, '一级分类': key, '安装人数': ins_ls,'软件大小':len_ls})
    apps_df = apps_df.append(apps_df_tmp)

# 导出
apps_df.to_csv('wandoujia_app_cat.csv', index=False)
