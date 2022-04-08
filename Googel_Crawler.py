from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import argparse
import time
import pandas as pd
from urllib import parse

class ChromeCrawl:
	def __init__(self,page,timeSleep,Txtname):
		self.timeSleep=timeSleep
		self.page=page
		self.Txtname=Txtname
		pass

	def getUrl(self):
		urlList = []
		#//*[@id="rso"]/div/div/div/div/a/div/cite
		#//*[@id="rso"]/div[10]/div/div/div[1]/div/a/div/cite
		a = browser.find_elements(By.XPATH,'//*[@id="rso"]/div/div/div/div/a/div/cite')
		b=browser.find_elements(By.XPATH,'//*[@id="rso"]/div[10]/div/div/div[1]/div/a/div/cite')
		for i in a:
			tmpUrl=i.text
			urlList.append(tmpUrl)

		for i in b:
			urlList.append(i.text)
		return urlList

	def isElementExist(self,by,element):
		flag=True
		try:
			browser.find_element(by,element)
			return flag

		except:
			flag=False
			return flag

	def allPage(self):
		page=self.page
		timeSleep=self.timeSleep
		allUrl = []
		print("开始爬取")
		for i in range(page):
			time.sleep(timeSleep)
			print("当前为第"+str(i+1)+"页")
			if self.isElementExist(By.ID,"search"):
				allUrl.append(self.getUrl())
				print("第"+str(i+1)+"页爬取完成")
				if self.isElementExist(By.ID,"pnnext"):
					browser.find_element(By.ID,"pnnext").click()
					if i == page - 1:
						print("全部爬取完成！")
						return allUrl
				else:
					print("没有下一页，全部爬取完成！")
					return allUrl
			else:
				print("不存在元素，全部爬取完成！")
				return allUrl

	def createCsvandTxt(self,aList):
		with open(self.Txtname.replace(".csv",".txt"),"a+",encoding="utf-8") as f:
			for i in range(len(aList)):
				for j in range(len(aList[i])):
					f.write(aList[i][j].replace(" › ","/")+"\n")
		csvName=self.Txtname
		domain = []
		urlL = []
		for i in range(len(aList)):
			for j in range(len(aList[i])):
				parsed_tuple = parse.urlparse(aList[i][j])
				domain.append(parsed_tuple.netloc)
				urlL.append(aList[i][j].replace(" › ","/"))
		urlDict = {"domain":domain, "url":urlL}
		df = pd.DataFrame(urlDict)
		df.to_csv(csvName,index=False,encoding="utf-8")


class CrawlerConfiguration:
	def __init__(self):
		self.TEXT="-"*50

	def ArgumentPars(self):
		TxtName = str(int(time.time())) + ".csv"
		parser = argparse.ArgumentParser()
		parser.add_argument('--gpu', action="store_false", help='输入该参数将显示chrome，显示爬取过程，默认为False')
		parser.add_argument('-s', type=str, default='site:.com', help='请输入你想搜索的google hacking语句，默认为site:.com，以此作为测试')
		parser.add_argument('-po', type=str, default='127.0.0.1:7890', help='请输入一下谷歌浏览器的代理,默认127.0.0.1:7890')
		parser.add_argument('-p', type=int, default=1, help='请输入你想搜索的页数，默认1页')
		parser.add_argument('-t', type=int, default=3, help='请输入翻下一页停顿的时间，默认3秒')
		parser.add_argument('-r', type=str, default=TxtName, help='请输入你想输出的文件名称，默认为'+TxtName)
		args = parser.parse_args()
		return args

	def ChromeInitialization(self):
		global browser
		args=self.ArgumentPars()
		chrome_options = Options()
		chrome_options.add_argument(f"--proxy-server=http://{args.po}")
		if args.gpu:
			chrome_options.add_argument('--headless')
			chrome_options.add_argument('--disable-gpu')
			chrome_options.add_argument('--ignore-certificate-errors')
			chrome_options.add_argument('--ignore-ssl-errors')
		chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
		browser = webdriver.Chrome(chrome_options=chrome_options)
		browser.get("https://www.google.com")

		#/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input是搜索框的XPath,模拟输入点击
		browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(
			args.s)
		browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()
		print(self.TEXT)

		newChromeCrawl = ChromeCrawl(args.p, args.t, args.r)
		newChromeCrawl.createCsvandTxt(newChromeCrawl.allPage())
		browser.quit()


if __name__ == '__main__':
	newCrawlerConfiguration=CrawlerConfiguration()
	newCrawlerConfiguration.ChromeInitialization()