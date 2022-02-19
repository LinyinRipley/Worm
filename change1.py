# 翻页爬取
import requests

def change1():
  #假设这是页码处
  url="https://www.google.com/{}.html"
  headers={"Users-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
  #爬取0-12页，有时候0页不存在或相当于第一页
  for i in range(13):
    urla=url.format(i)
    #查看验证
    print urla
    resp=resquests.get(url=urla,headers=headers)
    #写为同一个文件将会被覆盖
    with open(str(i)+".txt","wb+") as f:
      f.write(resp.content)
  pass
