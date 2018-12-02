import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BOOK_URLS = {
    'allite': 'http://www.allitebooks.com/'
}

DOWNLOAD_PATH = '/home/zhouyang/Downloads'

DATABASE ={
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
}