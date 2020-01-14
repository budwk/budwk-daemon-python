#!/usr/bin/python
# -*- coding: utf-8 -*-
# 初始jar包及配置文件文件夹,jar文件及配置文件以实例名为文件名,文件名中不包含版本号
APP_JARS = 'D://data/jars/'
# 运行目录,*不要手动创建,启动时判断目录是否存在来初始化项目
APP_ROOT = 'D://data/wk/'
# jar文件名,名称要保持与配置文件里 nutz.application.name 值一致
APP_LIST = [
    'wk-nb-service-sys',
    'wk-nb-web-api-daemon',
	'wk-nb-web-admin'
]
# jar包启动的jvm配置参数
APP_OPTS = {
    'wk-nb-service-sys': '-Xmx300m -Xms60m'
}
# 通信密钥,保持与 wk-nb-web-api-daemon 模块里配置内容一致,用于心跳通信
HTTP_SECRET_ID = 'wizzer'
HTTP_SECRET_KEY = 'budwk'
# API路径
HTTP_URL = 'http://127.0.0.1:9901/open/api/deploy'
# 心跳周期(单位:秒)
HTTP_HEARTBEAT = 15
HTTP_TIMEOUT = 120

CACHE_TASK_IDS = []
CACHE_HOST_NAME = ''
