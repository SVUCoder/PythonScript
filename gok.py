'''
@Date         : 2020-11-02 10:09:31
@LastEditors  : Pineapple
@LastEditTime : 2020-11-02 18:50:48
@FilePath     : /PythonScript/gok.py
@Blog         : https://blog.csdn.net/pineapple_C
@Github       : https://github.com/Pineapple666
'''

import asyncio
import json
import os
import re
import time
from os.path import abspath, dirname
from urllib.parse import unquote

import aiohttp
import requests
from loguru import logger

IMAGEPATH = dirname(abspath(__file__))+'/images'


class GOK:
    '''
    协程爬取王者450张，450M，1080P壁纸
    '''

    def __init__(self) -> None:
        '''
        初始化操作
        '''
        self.heros_url = 'https://pvp.qq.com/web201605/js/herolist.json'
        self.api_url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi'
        self.max_page = 23
        self.headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
        }
        self.count = 1
        self.tasks = []
        self.hero_list = []
        if os.path.exists(IMAGEPATH):
            os.rmdir()
        os.mkdir(IMAGEPATH)
        os.mkdir(IMAGEPATH+'/其他')
        response = requests.get(url=self.heros_url, headers=self.headers)
        heros = response.json()
        for hero in heros:
            self.hero_list.append(hero.get('cname'))

    def make_dir(self, hero_path):
        '''
        根据英雄名创建文件夹
        '''
        if not os.path.exists(hero_path):
            os.mkdir(hero_path)

    def get_params(self):
        '''
        生成表单参数
        '''
        for page in range(self.max_page):
            yield {
                'activityId': '2735',
                'sVerifyCode': 'ABCD',
                'sDataType': 'JSON',
                'iListNum': '20',
                'totalpage': '0',
                'page': page,
                'iOrder': '0',
                'iSortNumClose': '1',
                'iAMSActivityId': '51991',
                '_everyRead': 'true',
                'iTypeId': '2',
                'iFlowId': '267733',
                'iActId': '2735',
                'iModuleId': '2735',
                '_': time.time()
            }

    async def get_image_info(self, params, session):
        '''
        请求api，提取壁纸信息
        '''
        async with session.get(url=self.api_url, headers=self.headers, params=params) as response:
            if response.status == 200:
                response = await response.text()
                image_list = json.loads(
                    re.search(r'{.*}', response).group()).get('List')
                for image_info in image_list:
                    # 提取壁纸名，及其对应的1080P下载地址
                    image_name = unquote(image_info.get('sProdName'))
                    image_url = unquote(image_info.get('sProdImgNo_6')[:-3])
                    await self.save_to_jpg(image_name, image_url, session)

    async def save_to_jpg(self, image_name, image_url, session):
        '''
        保存为jpg图片
        '''
        down = False
        response = await session.get(url=image_url, headers=self.headers)
        if response.status == 200:
            result = await response.content.read()
            # 遍历英雄列表，对壁纸进行分类下载
            for hero_name in self.hero_list:
                if image_name.count(hero_name):
                    hero_path = f'{IMAGEPATH}/{hero_name}'
                    self.make_dir(hero_path)
                    # async with aiofiles.open(f'{hero_path}/{image_name}.jpg', 'wb') as file:
                    with open(f'{hero_path}/{image_name}.jpg', 'wb') as file:
                        file.write(result)
                        down = True
                        break
            # 针对遗留壁纸，统一下载到其他目录下
            if not down:
                with open(f'{IMAGEPATH}/其他/{image_name}.jpg', 'wb') as file:
                    file.write(result)
            logger.success(
                f'Download {image_name} successful, count {self.count}')
            self.count += 1
        else:
            logger.error(
                f'Download {image_name} error, url {image_url}')
        response.close()

    async def main(self):
        async with aiohttp.ClientSession() as session:
            for params in self.get_params():
                self.tasks.append(asyncio.create_task(
                    self.get_image_info(params, session)))
            await asyncio.wait(self.tasks)


if __name__ == "__main__":
    start = time.time()
    gok = GOK()
    asyncio.run(gok.main())
    end = time.time()
    logger.info(f'Download {gok.count-1} images, cost {end-start:.3f}s')
