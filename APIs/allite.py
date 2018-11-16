import requests
from bs4 import BeautifulSoup
from config.settings import BOOK_URLS

# 要加入异常机制
response = requests.get(BOOK_URLS.get('allite'))

# 用beautifulsoup解析文档
bsObj = BeautifulSoup(response.content, 'html.parser')

# 提取分页信息，遍历爬虫

def extract_books(bsObj):
    '''找到书籍标签，打印内容'''
    bookTags = bsObj.find(id='main-content').findAll('article')
    for book in bookTags:
        title = book.find('h2', {'class': 'entry-title'})
        print(title.get_text())
    # 提取书籍的各种信息

    # 调用SQLalchemy来存入

