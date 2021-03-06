#!/usr/bin/env python3
# coding: utf-8
# File: settings.py
# Author: lxw
# Date: 4/26/17 2:48 PM

# Redis数据库的地址和端口
# HOST = "192.168.1.36"
HOST_PROXY = "192.168.1.29"
PORT_PROXY = 6379

# HOST = "101.201.102.233"
# PORT = 63679

# 测试API，用百度来测试
# TEST_API = "https://www.baidu.com/"
TEST_API = "http://www.baidu.com/"

# 如果Redis有密码，则添加这句密码，否则设置为None
# PASSWORD = 'foobared'
# PASSWORD = None

# 代理池数量界限
# POOL_LOWER_THRESHOLD = 10
# POOL_UPPER_THRESHOLD = 100

# 检查周期
# VALID_CHECK_CYCLE = 60
# POOL_LEN_CHECK_CYCLE = 20

DB_NAME_PROXY = "IPPool"
