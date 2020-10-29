# 一个打卡软件
## 1.安装
### 1.1 selenium
- [1] win+R cmd；
- [2] pip install selenium
### 1.2 googledevice
- [1] 下载对应版本的chromedriver驱动文件，具体版本请对照连接对应关系表：[下载地址](http://chromedriver.storage.googleapis.com/index.html)
- [2] 下载后把文件解压，然后放到本机chrome浏览器文件路径里，如：C:\Program Files (x86)\Google\Chrome\Application
- [3] 将chromedriver添加到环境变量Path中
- [4] 修改auto_report.py中的驱动地址和你的用户名和密码

### [selenium使用chrome浏览器](https://www.jb51.net/article/151629.htm)

### 1.3 计算机定时启动
- [1] 新建outo_report.bat文件，在里面用文本框输入python outo_report.py
- [2] 设置定时启动.bat文件。参考博客[Windows10系统设置定时任务 开机启动.bat文件](https://blog.csdn.net/circle_do/article/details/84861028)




