# 1. 爬虫
- 两大特性
    - 能自动按要求下载数据或内容
    - 能自动在网上流窜

- 三大步骤
    - 下载网页
    - 提取信息
    - 根据一定规则自动跳转到下一网页执行上两步n内容

- 爬虫分类
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）

- Python网络包简介
    - Python2.x: urllib, urllib2, urllib3, httplib, httplib2, request
    - Python3.x: urllib, urllib3, httplib2, request
    - Python2: urllib2, urllib3, request
    - Python3: urllib, request

# 2. urllib

- 包含模块
    - urllib.request: 打开和读取url
    - urllib.error: 包含urllib.request产生的常见错误，使用try捕捉
    - urllib.parse: 包含即系url的方法
    - urllib.robotparse: 解析robots.txt文件