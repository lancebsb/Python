# # codeing=utf-8  
import urllib.request  
import re  
'''''通过京东服务器查'''  
url = 'https://item.jd.com/2235572.html'  
jdid = re.search(r'/(\d+)\.html', url).group(1)  
print(jdid)
url = 'http://p.3.cn/prices/get?skuid=J_' + str(jdid) + '&type=1&area=19_1601_51091&callback=cnp'#这就是那个被藏起来的json文件，格式除了京东id部分其他都一样  
#其实就是p.3.cn/prices/get?skuid=J_997951&type=1&area=19_1601_51091&callback=cnp  
html = urllib.request.urlopen(url).read().decode('utf-8')  
print(html)
aa = re.search(r'"p":"(.*?)"', html).group(1)  
  
print(aa)  




#京东移动端抓取
# codeing=utf-8  
# import urllib.request  
# import re  
# #通过京东移动接口  
# url = 'http://item.jd.com/2235572.html'#原本的网址  
# jdid = re.search(r'/(\d+)\.html',url).group(1)#原本的网址提取出商品ID，即2235572 
  
  
# url = 'http://m.jd.com/product/'+str(jdid)+'.html'#转换成为移动商城的url  
# html = urllib.request.urlopen(url).read().decode('utf-8')#通过对源代码进行utf-8解码  
# print(html)
# pattern = re.compile('<span class="big-price">(.*?)</span>',re.S)
# items = re.findall(pattern,html)

# print(items[0])
#   