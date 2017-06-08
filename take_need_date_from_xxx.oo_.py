#-*_coding:utf8-*-

import xlwt
import re


def getinfo(file, pattern, pos):
	info = []
	with open(file, 'r') as f:
		for line in f.readlines():
			m = re.search(pattern, line)
			if m:
				info.append(int(m.group(pos)))
        return info

if __name__ == '__main__':
    meminfo = getinfo('xxx.oo', r'.*>+(\d+)', 1)
    # cpuinfo = getinfo('123.txt', r'\d+\s+\d+\s+(\d+)%.*xxxxxx.com', 1)
    # batespinfo = getinfo('123.txt', r'temperature:\s+(\d+)', 1)
    '''将结果写入excel文档'''
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('testresult', cell_overwrite_ok=True)
    '''列名'''
    column0 = [u'time(ms)']
    '''for循环取出每行对应结果值'''
    for i in range(0, len(column0)):
        sheet1.write(0, i, column0[i])
    for j in range(0, len(meminfo)):
        sheet1.write(j+1, 0, int(meminfo[j]))
    # for h in range(0, len(cpuinfo)):
    #     sheet1.write(h+1, 1, int(cpuinfo[h]))
    # for k in range(0, len(batespinfo)):
    #     sheet1.write(k+1, 2, batespinfo[k])
    workbook.save('test_resultAAA.xls')