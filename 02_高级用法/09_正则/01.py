import re

# 查找数字
# r表示字符串不转义

p = re.compile(r'\d+')
# s = p.match("dmiwq92121312832")
s = p.match("as4355dasddq454364574", 2, 7)
print(s)

# match
p = re.compile(r'([a-z]+) ([a-z]+)', re.I)
s = p.match("I am really love you")
print(s)
print(s.group(0)) # 0全部
print(s.groups())
print(s.start(0))
print(s.end(0))

# search, findall
p = re.compile(r'\d+')
m = p.search("one12two34three56")
print(m.group(0))
rst = p.findall("one12two34three56")
print(rst)

# sub
# \w 包含字母跟数字
p = re.compile(r"(\w+) (\w+)")
s = "helo 12 wang 34 yin, i love you"
rst = p.sub(r'hello world', s)
print(rst)

# 匹配中文
title = u"世界 你好，hello world"
p = re.compile(r"[\u4e00-\u9fa5]+")
rst = p.findall(title)
print(rst)

# 贪婪和非贪婪
# 贪婪：尽可能多的匹配，(*)表示贪婪匹配
# 非贪婪：表示找到符合条件的最小内容即可, (?)表示非贪婪
title = u"<div>name</div><div>age</div>"

p1 = re.compile(r"<div>.*</div>")
p2 = re.compile(r"<div>.*?</div>")

m1 = p1.search(title)
print(m1.group())
m2 = p2.search(title)
print(m2.group())



