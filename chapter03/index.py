import csv
import re

# 1.读取数据源
with open("source.txt", encoding="utf-8") as f:
    source = f.read()
# 2.读取所有作者 发帖内容  时间
author_data_re = '''class="tb_icon_author "
          title="主题作者:(.*?)"'''
author_data = re.findall(author_data_re, source, re.S)
content_data = re.findall('<div class="threadlist_abs threadlist_abs_onlyline ">(.*?)</div>', source, re.S)
time_data = re.findall('<span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">(.*?)</span>',
                       source, re.S)
# 3.写入文件
result = []
for i in range(len(author_data)):
    # result.append({"author":author_data[i],"content":content_data[i],"time":time_data[i]})
    result.append({"author": i, "content": i + 2, "time": i + 5})
# newline 以空内容 解决输出时有个空行
with open("result.csv", "w", encoding="utf-8",newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["author", 'content', "time"])
    writer.writeheader()
    writer.writerows(result)
print(result)
