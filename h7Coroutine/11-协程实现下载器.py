import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

def downloader(img_name,img_url):
    req = urllib.request.urlopen(img_url)

    img_conent = req.read()

    with open(img_name,"wb") as f:
        f.write(img_conent)
def main():

    gevent.joinall([
        gevent.spawn(downloader,'1.jpg','https://res.vmallres.com/pimages/detailImg/2018/12/11/201812112233025695075.png'),
        gevent.spawn(downloader, '2.jpg','https://res.vmallres.com/pimages/detailImg/2018/12/11/201812112233023998633.png' ),
        gevent.spawn(downloader, '3.jpg','https://res.vmallres.com/pimages/detailImg/2018/12/11/201812112233033209844.png' ),

    ])
if __name__ == '__main__':
    main()