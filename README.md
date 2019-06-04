>  更新于 2019 年 4月

## Follow 使用说明


### 初始化项目

```bash

git clone https://github.com/aikuyun/yuque-follow.git


cd yuque-follow


pip install -r requirements.txt

```

文件结构说明：

```text
.
├── README.md                    # 说明
├── chromedriver                 # Mac 版谷歌浏览器确定
├── chromedriver-linux           # Linux 版
├── chromedriver.exe             # Windows 版
├── follow.py                    # 启动程序
├── requirements.txt             # 相关依赖
└── yuque.csv                    # 用户 Id 信息

```


### 用户数据导入 Mysql

把yuque.csv 导入mysql 数据库。

也可以自己选择使用 python 直接读 CSV 的 ID 信息。（本次读的数据库）


### 自定义部分代码


数据库连接信息：
```python
# 连接database
conn = pymysql.connect(host="127.0.0.1", user="XXXX", password="XXXX", 
    database="XXXX", charset="utf8")  

# 替换成你自己的数据库即可。
```

修改驱动：

```python
# 加载浏览器驱动。
# 先看一下自己的谷歌浏览器是什么版本的，我这里是  73.0.3683.86（正式版本） （64 位） 
# 截至到 20190331 的最新版本

driver = webdriver.Chrome(executable_path='./chromedriver')

```

> 我已经在目录下放了三个版本供大家选择。 chrome浏览器驱动,我这里选的是 Mac 版。windows 用户这里改成 ./chromedriver.exe ; Linux 用户请改成 ./chromedriver-linux

如果遇到版本问题可以访问：https://npm.taobao.org/mirrors/chromedriver 下载适合你的驱动版本。

添加自己的语雀用户名和密码

```python
name.send_keys('xxxxxxx') # 这里替换成你的用户名

password.send_keys('xxxxxx') # 这里替换成你的密码

```

That's all.





