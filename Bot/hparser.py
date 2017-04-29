import urllib.request
from lxml import html


class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link


def get_titles():
    videos = []
    url = "https://www.youtube.com/user/PewDiePie/videos"
    page = html.fromstring(urllib.request.urlopen(url).read())
    a_xpath = '//*[@id="channels-browse-content-grid"]/li[{}]/div/div[1]/div[2]/h3/a'

    for i in range(10):
        a = page.xpath(a_xpath.format(i + 1))
        title = a[0].get("title")
        link = a[0].get("href")
        link = 'https://www.youtube.com' + link
        videos.append(Video(title, link))

    return videos


def get_new():
    url = "https://www.youtube.com/user/PewDiePie/videos"
    page = html.fromstring(urllib.request.urlopen(url).read())
    a_xpath = '//*[@id="channels-browse-content-grid"]/li[1]/div/div[1]/div[2]/h3/a'
    a = page.xpath(a_xpath)
    title = a[0].get("title")
    link = a[0].get("href")
    link = 'https://www.youtube.com' + link
    return Video(title, link)
