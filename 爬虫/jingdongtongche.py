# -*- coding: utf-8 -*-

import urllib.request  
import re  
from threading import Timer
import time

class JingDong:
	#初始化 传入基地址，是否只看楼主的参数
	def __init__(self,baseUrl):
		self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
		self.baseURL=baseUrl
		#初始化headers  
		self.headers = { 'User-Agent' : self.user_agent }  
		#self.seeLZ='?see_lz='+str(seeLZ)

	#传入某一页的索引获得页面代码  
	def getPage(self):
		try:
			url=self.baseURL
			#构建请求的request  
			request = urllib.request.Request(url,headers=self.headers)  
            #利用urlopen获取页面代码  
			response = urllib.request.urlopen(request)  
            #将页面转化为UTF-8编码  
			pageCode=response.read().decode('gbk').encode('utf-8').decode('utf-8')  #这块一定要注意，一般网页都是uft-8编码，但是京东的是gbk,直接转uft-8会报编码错误，需要先转成utf-8
			#print(pageCode)
			return pageCode  
		except urllib.request.URLError as e:  
			if hasattr(e,"reason"):  
				print(u"连接京东失败,错误原因",e.reason)  
				return None 
	  
 		#获取每一层楼的内容,传入页面内容
	def getContent(self,page):
		#得到商品名称
	    pattern = re.compile('<div id="name">.*?<h1>(.*?)</h1>.*?</div>',re.S)
	    items = re.findall(pattern,page)
	    #print(items[0])
	    #得到商品价格
	    jdid = re.search(r'/(\d+)\.html', self.baseURL).group(1) 
	    url_p = 'http://p.3.cn/prices/get?skuid=J_' + str(jdid) + '&type=1&area=19_1601_51091&callback=cnp'#这就是那个被藏起来的json文件，格式除了京东id部分其他都一样  
	    html = urllib.request.urlopen(url_p).read().decode('utf-8')
	    price = re.search(r'"p":"(.*?)"', html).group(1)  
	    print('商品名称: %s ,单价：%s' % (items[0],price))



	def start(self):	
		page = self.getPage()
		contents = self.getContent(page)
		print(u"写入任务完成"+GetNowTime())  
	


timer_Interval = 5  #等待5秒
def delayrun():
	print('runing')
	baseURL = 'https://item.jd.com/2235572.html'
	jd = JingDong(baseURL)
	jd.start()

def GetNowTime():
	return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

t=Timer(timer_Interval,delayrun)
t.start()
while True:
	time.sleep(10)  #50秒运行一次
	delayrun()