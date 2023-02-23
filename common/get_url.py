# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 14:22
# @Author  : Mandy
import yaml

import conftest


class TestUrl(object):
    def __init__(self, env="dev"):
        if env == "dev":
            self.base_url = self.get_uri('base_url_dev')
        else:
            self.base_url = self.get_uri('base_url')

    def get_uri(file_name, key):
        filename = conftest.data_dir + '/url.yaml'
        data = open(filename, encoding='UTF-8').read()
        yaml_reader = yaml.safe_load(data)
        uri = yaml_reader[key]
        return uri

    def get_url(self, name):
        return self.base_url + self.get_uri(name)
