import requests, os
from bs4 import BeautifulSoup
from config.settings import BOOK_URLS, DOWNLOAD_PATH

def extract_books(url):
    """找到书籍标签，打印内容"""
    response = requests.get(url)
    bsObj = BeautifulSoup(response.content, 'html.parser')
    bookTags = bsObj.find(id='main-content').findAll('article')
    books = []
    for book in bookTags:
        title = book.find('h2', {'class': 'entry-title'})
        print(title.get_text(), title.a.attrs.get('href'))
        books.append((title.get_text(), title.a.attrs.get('href')))
    return books

def get_book_info(url):
    """提取某个书籍的详情信息存入数据库"""
    response = requests.get(url)
    bsObj = BeautifulSoup(response.content, 'html.parser')
    headerTag = bsObj.find('header', {'class': 'entry-header'})
    title = headerTag.find('h1').get_text()
    subtitleTag = headerTag.find('h4')
    subtitle = subtitleTag.get_text() if subtitleTag else None
    imgURL = headerTag.find('div', {'class': 'entry-body-thumbnail'}).find('img').attrs.get('src')
    bookDetail =headerTag.find('div', {'class': 'book-detail'})
    author_tags = bookDetail.dl.find('dt', string='Author:').next_sibling.find_all('a')
    authors = [a.text for a in author_tags]
    isbn = bookDetail.dl.find('dt', string='ISBN-10:').next_sibling.text
    year = bookDetail.dl.find('dt', string='Year:').next_sibling.text
    pages = bookDetail.dl.find('dt', string='Pages:').next_sibling.text
    language = bookDetail.dl.find('dt', string='Language:').next_sibling.text
    size = bookDetail.dl.find('dt', string='File size:').next_sibling.text
    fileFormat = bookDetail.dl.find('dt', string='File size:').next_sibling.text
    categoryTags = bookDetail.dl.find('dt', string='Category:').next_sibling.find_all('a')
    category = [c.text for c in categoryTags]
    content = bsObj.find('div', {'class': 'entry-content'}).strings
    content = ''.join(list(content)[3:])
    link = bsObj.find('footer', {'class': 'entry-footer'}).a.get('href')

def download(link):
    """下载书籍返回存储路径"""
    bookName = link.split('/')[-1]
    bookPath = os.path.join(DOWNLOAD_PATH, bookName)
    with requests.get(link, stream=True) as bookRep:
        with open(bookPath, 'wb') as f:
            for chunk in bookRep.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)


if __name__ == '__main__':

    books = extract_books(BOOK_URLS.get('allite'))
    for title, url in books:
        print('开始解析：', title)
        get_book_info(url)
