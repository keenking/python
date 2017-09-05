# -*- coding: utf-8 -*-
# __author__ = 'k.'
import os
import easygui

msg = "请填写修改内容项"
title = "图片批量修改定制版"
fieldNames = ["输入重命名前缀", "输入数字0的个数", "*输入开始位数字"]
fieldValues = []
fieldValues = easygui.multenterbox(msg, title, fieldNames)
while True:
    if fieldValues == None:
        break
    errmsg = ""
    for i in range(len(fieldNames)):
        option = fieldNames[i].strip()
        if fieldValues[i].strip() == "" and option[0] == "*":
            errmsg += ("【%s】为必填项   " % fieldNames[i])
    if errmsg == "":
        break
    fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)
dir_open = easygui.diropenbox('祖安泽', '图片')
pname = fieldValues[0]
j = int(fieldValues[2])
i = int(fieldValues[1])
filelist = os.listdir(dir_open)
for item in filelist:
    if item.endswith('.png'):
        src = os.path.join(os.path.abspath(dir_open), item)
        dst = os.path.join(os.path.abspath(dir_open), str(pname) + str((("%0" + str(i) + "d")%j)) + '.png')
        try:
            os.rename(src, dst)
            j += 1
        except:
            continue

