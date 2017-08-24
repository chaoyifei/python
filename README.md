# python
selenium为自动化测试框架，其余为python scrapy爬虫



影评分析：
主要做了三件事：
    抓取网页数据
    清理数据
    用词云进行展示
python2.7
1、第一步要对网页进行访问，python中使用的是urllib2库
2、第二步，需要对得到的html代码进行解析，得到里面提取我们需要的数据，使用BeautifulSoup。
3、用jieba分词统计词频(numpy)
4、用云词显示wordcloud




