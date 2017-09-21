# -*- coding: utf-8 -*-
# __author__ = 'k.'

import os
import easygui

# class BatchRename():
#     '''
#     批量重命名文件夹中的图片文件
#     '''
#     def __init__(self):
#         self.path = input('your path:')
#
#     def rename(self):
#         filelist = os.listdir(self.path)
#         total_num = len(filelist)
#         i = input('输入你想要的数字位数：')
#         pname = input('your name:')
#         for item in filelist:
#             if item.endswith('.png'):
#                 src = os.path.join(os.path.abspath(self.path), item)
#                 dst = os.path.join(os.path.abspath(self.path), str(pname) + '_' + str("%03d" % i) + '.png')
#                 try:
#                     os.rename(src, dst)
#                     print ('converting %s to %s ...' % (src, dst))
#                     i = i + 1
#                 except:
#                     continue
#         print ('total %d to rename & converted %d pngs' % (total_num, i))
#         Yes_or_No = easygui.buttonbox(('total %d to rename & converted %d pngs' % (total_num, i)))
#         return Yes_or_No
#
# if __name__ == '__main__':
#     demo = BatchRename()
#     demo.rename()
# file_open_files = easygui.fileopenbox(msg='信息', title='标题', default='2', multiple=True)
dir_open = easygui.diropenbox(msg='所选目录', title='要转换的目录', default='2')
pname = input('your name:')
j = input('从数字几开始：')
i = input('输入你想要的数字位数：')
j = int(j)
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





