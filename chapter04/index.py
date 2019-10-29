import os
import requests
import re
from multiprocessing.dummy import Pool


def runSpider(main_url):
    '''
    开启多线程执行每个章节的数据爬取
    :param main_url:
    :return:
    '''
    urls = getUrls(main_url)
    pool = Pool(3)
    pool.map(parseAndSaveContent, urls)


def getUrls(mainUrl):
    '''
    根据主链接获取每一章对应的链接
    :param mainUrl:
    :return:
    '''
    urls = []
    content = requests.get(mainUrl).content.decode('gb2312')
    # 从content中获取含有链接的大块内容
    content = re.findall('<strong>正文</strong></td>(.*?)</tbody>', content, re.S)[0]
    sub_urls = re.findall('<a href="(.*?)">', content, re.S)
    for url in sub_urls:
        urls.append(mainUrl + url)
    return urls


def parseAndSaveContent(url):
    '''
    获取每一章的内容并写入到文件
    :param url:
    :return:
    '''
    # 提取内容
    content = requests.get(url).content.decode('gb2312')
    chapter_name = re.search('size="4"> (.*?)</font>', content, re.S).group(1)
    chapter_txt = re.search('<p>(.*?)</p>', content, re.S).group(1)
    chapter_txt = chapter_txt.replace("<br />", "")
    # 写入文件
    os.makedirs('动物农场', exist_ok=True)  # 创建文件夹如果存在什么也不做
    with open(os.path.join('动物农场', chapter_name + '.txt'), 'w', encoding="utf-8") as f:
        f.write(chapter_txt)


if __name__ == '__main__':
    runSpider('https://www.kanunu8.com/book3/6879/')
