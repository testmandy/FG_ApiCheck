# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 14:21
# @Author  : Mandy
import sys

from testcases.backend.test_device import TestCabinet

if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) > 1:
        env = sys.argv[1]
        req = TestCabinet()
    else:
        print('参数数量1：%s, 即将运行测试环境' % len(sys.argv))
        req = TestCabinet()



