# -*- coding: utf-8 -*-
# __author__ = 'k.'


'''截取文本中顿号前面的词语'''
f1 = open("before.txt", "r", encoding='utf-8')
f2 = open("after.txt", "w", encoding='utf-8')
for line in f1:
    a = line.split("、", -1)
    for b in a:
        f2.write(b+'\n')
f1.close()
f2.close()
