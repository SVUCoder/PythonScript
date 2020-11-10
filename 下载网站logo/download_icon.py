'''
@Date         : 2020-11-10 09:37:25
@LastEditors  : Pineapple
@LastEditTime : 2020-11-10 14:30:16
@FilePath     : /PythonScript/下载网站logo/download_icon.py
@Blog         : https://blog.csdn.net/pineapple_C
@Github       : https://github.com/Pineapple666
'''

import os
from os.path import abspath, dirname, exists

import requests
from loguru import logger

home_url = input('请输入网站主页地址:(举个栗子: https://www.baidu.com) ')
image_name = input('请输入将保存的图片名: ')

icon_url = home_url+'/favicon.ico'
image_path = dirname(abspath(__file__))+'/images'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
}

response = requests.get(url=icon_url, headers=headers)
if response.status_code == 200:
    icon_bytes = response.content
    icon_path = f'{image_path}/{image_name}.jpg'
    if not exists(image_path):
        os.mkdir(image_path)
    if not exists(icon_path):
        with open(icon_path, 'wb') as file:
            file.write(icon_bytes)
            logger.success('Download successful.')
    else:
        logger.debug('Image has exists.')
else:
    logger.error('Download failed.')
