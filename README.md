
![image](https://user-images.githubusercontent.com/75877299/162341284-398faf38-4839-4847-85d3-b3a548770b48.png)
![image](https://user-images.githubusercontent.com/75877299/162341306-3fb558f6-a222-4e69-b255-f3de62303f24.png)

右键复制完整的Xpath,这样省着我们一个一个去查找了
而且如果Xpath换了,也可以很简单的修改源码
1. 下载Chrome浏览器，然后去https://npm.taobao.org/mirrors/chromedriver/下载对应之前下载的Chrome浏览器版本的chromedriver.exe
2. 将下载好的chromedriver.exe放入python.exe的所在文件夹，然后再放入chrome.exe的所在文件夹。
3. 将chrome.exe的所在文件夹设到系统变量中。

```
python .\Googel_Crawler.py -s "site:lzu.edu.cn" -p 3 -t 5 --gpu
```

![image](https://user-images.githubusercontent.com/75877299/162341384-c4e4c6bb-cd61-4a92-85d4-35bf5038009c.png)

