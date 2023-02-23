# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 14:21
# @Author  : Mandy
from common.get_url import TestUrl
from common.method import Request

# URL = TestUrl(version='v1')
URL = TestUrl()


class ReqWithToken(object):
    def __init__(self, account=None, pwd=None):

        self.req = Request()
        self.account = account

        if pwd is None:
            self.pwd = '25d55ad283aa400af464c76d713c07ad'
            self.pwd_nice = '123456'
        else:
            self.pwd = pwd
            self.pwd_nice = pwd
        self.headers = {'Content-Type': 'application/json', 'token': 'Bearer %s'}
        print(self.headers)

    def get(self, url, params=None):
        res = self.req.get(url, params=params, headers=self.headers)
        return res

    def put(self, url, params=None):
        res = self.req.put(url, params=params, headers=self.headers)
        return res

    def post(self, url, params=None, json=None):
        res = self.req.post(url, params=params, json=json, headers=self.headers)
        return res

    def delete(self, url, params=None):
        res = self.req.delete(url, params=params, headers=self.headers)
        return res


if __name__ == '__main__':
    req = ReqWithToken(account='test301', pwd='123456')
