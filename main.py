import requests
#简单爬取页面
def main():
       url="https://www.google.com"
       headers={"Users-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
       resp=requests.get(url=url,headers=headers)
  #爬取内容导出在0.txt中，使用二进制 
       with open("0.txt","wb+") as f:
              f.write(resp.content)
       pass
if__name___=='__main___':
       main()
               
    
