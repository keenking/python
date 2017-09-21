# -*- coding: utf-8 -*-
# __author__ = 'k.'
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
