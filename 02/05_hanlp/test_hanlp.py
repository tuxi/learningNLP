# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 11:57 PM
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : test_hanlp.py
# @Software: PyCharm

import os

if __name__=='__main__':
    if os.path.exists('hanlp_source'):
        raise FileNotFoundError('hanlp_source is not found, please download [hanlp.jar] and [data.zip] from https://github.com/hankcs/HanLP')

