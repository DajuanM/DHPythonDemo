from urllib import request

if __name__ == '__main__':
    url = "https://www.lagou.com/zhaopin/Python/?labelWords=label"
    # 打开url
    rsp = request.urlopen(url)
    # 读取
    html = rsp.read()
    # 解码
    html = html.decode()
    print(html)