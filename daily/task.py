# -*- coding: utf-8 -*-
# __author__ = 'k.'
import urllib
import urllib3
'''
做个爬虫，把网址 http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/index.html 数据爬回来。
表格式：
DROP TABLE IF EXISTS `area`;
CREATE TABLE `area` (
  `id` bigint(20) NOT NULL COMMENT '行政区划代码',
  `aname` varchar(128) default NULL COMMENT '行政区划名称',
  `lv` tinyint(4) default NULL COMMENT '行政区划等级',
  `pid` bigint(20) default NULL COMMENT '上级行政区划',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='行政区划';

-- ----------------------------
-- Records of area
-- ----------------------------
INSERT INTO `area` VALUES ('110000000000', '北京', '1', '0');
INSERT INTO `area` VALUES ('110100000000', '市辖区', '2', '110000000000');
INSERT INTO `area` VALUES ('110101000000', '东城区', '3', '110100000000');
INSERT INTO `area` VALUES ('110102000000', '西城区', '3', '110100000000');
INSERT INTO `area` VALUES ('110105000000', '朝阳区', '3', '110100000000');
INSERT INTO `area` VALUES ('110106000000', '丰台区', '3', '110100000000');
INSERT INTO `area` VALUES ('110107000000', '石景山区', '3', '110100000000');
INSERT INTO `area` VALUES ('110108000000', '海淀区', '3', '110100000000');'''
url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/index.html'
def download(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    response = requests.get(url, headers=headers)
    return response.text
html = download(url)


def main(args):
    basic_url = '招聘（求职）尽在智联招聘?'

    for keyword in KEYWORDS:
        mongo_table = db[keyword]
        paras = {'jl': args[0],
                 'kw': keyword,
                 'p': args[1]  # 第X页
                 }
        url = basic_url + urlencode(paras)
        # print(url)
        html = download(url)
        # print(html)
        if html:
            data = get_content(html)
            for item in data:
                if mongo_table.update({'zw_link': item['zw_link']}, {'$set': item}, True):
                    print('已保存记录：', item)