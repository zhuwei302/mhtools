__author__ = 'zhuwei'
#coding=utf-8

import MhxyHelperUIService
import tkMessageBox
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def beginYb(kj):
    id = kj.get()
    # print(id)
    if "请输入游戏ID" in id:
        tkMessageBox.showerror(title="错误", message="请输入数字ID")
    else:
         MhxyHelperUIService.getMHXYWinById(id)