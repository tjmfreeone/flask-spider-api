#! /usr/bin/python3
# -*- coding: utf-8 -*-
import asyncio
import aiohttp
import requests
from lxml import etree
from common.retJson import retJson
import re

URL = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D{}&page_type=searchall&page={}'
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
}

class FetchMachine():
    def launch(self, pageNum="1", keyword=None):
        self.adic = locals()
        self.retJson = retJson()
        self.item_list, self.pageNum, self.has_next = [], None, False
        if not self.adic['pageNum'] or not self.adic["keyword"]:
            return self.retJson["10005"]

        res = self.start_get_req()
        if not res:
            return self.retJson["10001"]


        if not self.item_list:
            return self.retJson["10008"]

        self.retJson["00000"]["data"] = self.item_list
        self.retJson["00000"]["pageNum"] = self.pageNum
        self.retJson["00000"]["hasNext"] = self.has_next
        return self.retJson["00000"]

    def start_get_req(self):
        pt = eval(self.adic["pageNum"])
        req_url = URL.format(self.adic["keyword"], self.adic["pageNum"])
        resp = requests.get(req_url,headers=HEADERS)
        if resp.status_code != 200:
            return None

        res_json = resp.json()

        if res_json["data"]["cardlistInfo"]["page"]:
            self.pageNum = pt + 1
            self.has_next = True


        for item in res_json["data"]["cards"]:
            baseObj = {}
            try:
                item["mblog"] = item["mblog"]
            except:
                continue
            baseObj["content"] = re.sub(r'<.*?>','',item["mblog"]["text"])
            baseObj["author"] = item["mblog"]["user"]["screen_name"]
            baseObj["date"] = item["mblog"]["created_at"]
            try:
                temp = item["mblog"]["pics"]
            except:
                item["mblog"]["pics"] = None
            baseObj["imgUrls"] = [ x["url"] for x in item["mblog"]["pics"] ] if item["mblog"]["pics"] else None
            self.item_list.append(baseObj)


        return True

        
    

                


    