import requests, os, os.path, random
from bs4 import BeautifulSoup


def get_soup(url):
    """
    获取网站的soup对象
    """
    # my_headers = [
    #     'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
    #     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
    #     'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
    #     'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',
    #     'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
    #     'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)']
    # header = {"User-Agent": random.choice(my_headers)}
    # req = requests.get(url, headers=header)
    req = requests.get(url,)
    html = req.text
    soup = BeautifulSoup(html, features='html.parser')
    return soup


def get_pages(url):
    """
    获取妹子图网站的页数
    """
    soup = get_soup(url)
    nums = soup.find_all('a', class_='page-numbers')
    pages = int(nums[-2].text)
    return pages


def get_menu(url):
    """
    获取页面的所有妹子图主题的链接名称和地址，记入列表
    """
    soup = get_soup(url)
    menu = []
    menu_list = soup.find_all('a', target='_blank')
    for i in menu_list:
        result = i.find_all('img', class_='lazy')
        if result:
            # 图片名字
            name = result[0]['alt']
            address = i['href']
            menu.append([name, address])
    return menu


def get_links(url):
    """
    获取单个妹子图主题一共具有多少张图片
    """
    soup = get_soup(url)
    all_ = soup.find_all('a')
    nums = []
    for i in all_:
        span = i.find_all('span')
        if span:
            nums.append(span[0].text)
    return nums[-2]


def get_image(url, filename):
    """
    从单独的页面中提取出图片保存为filename
    """
    soup = get_soup(url)
    image = soup.find('img').attrs.get('src')
    img_content = requests.get(image, {"Referer": 'http://m.mzitu.com/'}).content
    with open(filename, 'wb') as f:
        f.write(img_content)
    return '%s' % url

def main(page):
    """
    下载第page页的妹子图
    """
    print('正在下载第 %s 页' % page)
    page_url = url + '/page/' + str(page)
    menu = get_menu(page_url)
    print('@@@@@@@@@@@@@@@@第 %s 页共有 %s 个主题@@@@@@@@@@@@@@@@' % (page, len(menu)))
    for i in menu:
        # i[0]代表图片主题名字
        dir_name = os.path.join('MeiZiTu', i[0])
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        pic_nums = int(get_links(i[1]))
        print('\n\n\n@@@@@@@@@主题 %s 一共有 %d 张图片@@@@@@@@@\n' % (i[0], pic_nums))
        for pic in range(1, pic_nums + 1):
            basename = str(pic) + '.jpg'
            filename = os.path.join(dir_name, basename)
            # MeiZiTu\性感美女桃子衣不蔽体 丰乳肥臀难抵诱惑\6.jpg
            pic_url = i[1] + '/' + str(pic)
            # 获取单张图片的url  http://www.mzitu.com/102205/3
            if not os.path.exists(filename):
                pass
                print('......%s' % basename, get_image(pic_url, filename))
            else:
                print(filename + '已存在，略过')


if __name__ == '__main__':
    url = 'http://www.mzitu.com/'
    pages = get_pages(url)
    print('$$$$$$$$$妹子图一共有 %s 页$$$$$$$$$$$$$$' % pages)
    if not os.path.exists('MeiZiTu'):
        os.mkdir('MeiZiTu')
    page_start = input('Input the first page number:\n')
    page_end = input('Input the last page number:\n')
    if int(page_end) > int(page_start):
        for page in range(int(page_start), int(page_end)):
            main(page)
    elif page_end == page_start:
        main(page_end)
    else:
        print("输入错误，起始页必须小于等于结束页\n")
