# -*- coding: utf-8 -*-
# __author__ = 'k.'

import urllib3
import re
import time
import sys

# 正则表达式 <a href="http://www.wandoujia.com/apps/com.melot.meshow" title="KK美女直播" class="name">KK美女直播</a>
appNameRegex = re.compile(b'href=[\'|"](http://www.wandoujia.com/apps/.*?)[\'|"]\s*?title=[\'|"](.*?)[\'|"]')

# <div class="con">真人视频交友直播，漫漫长夜不再寂寞</div>
detailRegex = re.compile(b'<div\s*?class=[\'|"]con[\'|"]>(.+?)</div>')

# <span class="dev-sites" itemprop="name">杭州开迅科技有限公司</span>
companyNameRegex = re.compile(b'<span\s*?class=[\'|"]dev-sites[\'|"]\s*?itemprop=[\'|"]name[\'|"]>(.+?)</span>')

# datetime="2017年05月31日"
publishTimeRegex = re.compile(b'datetime=[\'|"]((.*?))[\'|"]')

# <img src="http://xxx.jpg" class="screenshot-img"
screenShotRegex = re.compile(b'<img\s*?src=[\'|"](http://.+?jpg)[\'|"]\s*?class=[\'|"]screenshot-img[\'|"]')

# UserDownloads:336
downloadCountRegex = re.compile(b'[\'|"]UserDownloads:(.+?)[\'|"]')

# <meta itemprop="fileSize" content="33.19MB">
appSizeRegex = re.compile(b'<meta\s*?itemprop=[\'|"]fileSize[\'|"]\s*?content=[\'|"](\d)')

f = open('temp.txt', 'w+', encoding='utf-8')

http = urllib3.PoolManager()

for x in range(1, 39):

	r = http.request('GET','http://www.wandoujia.com/category/5029_1006/'+ str(x))
# print(r.status)
# print(r.data)


	# print('第'+str(x)+'页')

	for appNameMo in appNameRegex.finditer(r.data):
		if appNameMo != None:

			# 打开网页获取详细信息
			r = http.request('GET',appNameMo.group(1).decode('utf-8'))

			# 公司
			companyNameMo = companyNameRegex.search(r.data)
			if companyNameMo != None:

				companyName = companyNameMo.group(1).decode('utf-8')
				if companyName.find('公司') != -1:
					print(companyName)
					appName = appNameMo.group(2).decode('utf-8')
					f.write( appName + '\n')

					#公司名字
					f.write(companyName + '\n')

					# 应用介绍
					detailMo = detailRegex.search(r.data)
					if detailMo != None:
						appDetail = detailMo.group(1).decode('utf-8')
						f.write(appDetail + '\n')
					else :
						f.write('无介绍\n')

					# 应用截图
					# for screenShotMo in screenShotRegex.finditer(r.data):
					# 	if screenShotMo != None:
					# 		screenShot = screenShotMo.group(1).decode('utf-8')
					# 		f.write('<img src="' + screenShot + '"/>\n')

					downloadCountMo = downloadCountRegex.search(r.data)
					if downloadCountMo != None:
						downloadCount = downloadCountMo.group(1).decode('utf-8')
						if downloadCount.find('万') != -1:
							downloadCount = str(int(float(downloadCount[:len(downloadCount)-1]) * 10000))
						elif downloadCount.find('亿') != -1:
							downloadCount = str(int(float(downloadCount[:len(downloadCount)-1]) * 100000000))
						f.write(downloadCount + '\n')
					else :
						f.write('无下载量\n')

					# 发布时间
					publishTimeMo = publishTimeRegex.search(r.data)
					if publishTimeMo != None:
						f.write(publishTimeMo.group(1).decode('utf-8') + '\n\n')
						f.flush()
						time.sleep(1)

# 排序
f = open('temp.txt','r',encoding='utf-8')
newFileDate = open('appDate'+ str(time.strftime("%Y%m%d_%H%M%S", time.localtime())) + '.txt','w+',encoding='utf-8')
newFileDownload = open('appDownload'+ str(time.strftime("%Y%m%d_%H%M%S", time.localtime())) + '.txt','w+',encoding='utf-8')

appArr = []

# 读取出全部数据
app = {}
for line in f.readlines():
	if line.isspace():
		appArr.append(app)
		app = {}
	else:
		if 'appName' not in app:
			app['appName'] = line
		elif 'company' not in app:
			app['company'] = line
		elif 'detail' not in app:
			app['detail'] = line
		elif 'downloadCount' not in app:
			app['downloadCount'] = int(line)
		elif 'date' not in app:
			timestamp = time.mktime(time.strptime(line,'%Y年%m月%d日\n'))
			app['date'] = line
			app['timestamp'] = int(timestamp)

# 排序
appArr.sort(key = lambda x:x['timestamp'],  reverse = True)

# 重新写入
for app in appArr:
	newFileDate.write(app['appName'])
	newFileDate.write(app['company'])
	newFileDate.write(app['detail'])
	newFileDate.write(str(app['downloadCount']) + '\n')
	newFileDate.write(app['date'])
	newFileDate.write('\n')

# 排序
appArr.sort(key = lambda x:x['downloadCount'],  reverse = True)

# 重新写入
for app in appArr:
	newFileDownload.write(app['appName'])
	newFileDownload.write(app['company'])
	newFileDownload.write(app['detail'])
	newFileDownload.write(str(app['downloadCount']) + '\n')
	newFileDownload.write(app['date'])
	newFileDownload.write('\n')

