__author__ = 'zhuwei'
#coding=utf-8

import MhxyHelperUIService

def beginYb(kj):
    id = kj.get()
    print(id)
    if id == "请输入游戏ID":
        print("请输入id")
    else:
        MhxyHelperUIService.getMHXYWinById(id)