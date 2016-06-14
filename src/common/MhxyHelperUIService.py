__author__ = 'zhuwei'
#coding=utf-8
'''
Created on 2016-5-26

@author: zhuwei
'''
import win32con
import win32gui
from win32gui import *
from pprint import pprint

def gbk2utf8(s):
    return s.decode('gbk').encode('utf-8')

def show_window_attr(hWndList,id):
    '''''
    显示窗口的属性
    :return:
    '''
    if not hWndList:
        return

    for h in hWndList:

        #中文系统默认title是gb2312的编码
        title = win32gui.GetWindowText(h)
        title = gbk2utf8(title)


        if id in title:

            clsname = win32gui.GetClassName(h)
            #窗口句柄:268124
            #窗口标题:梦幻西游 ONLINE - (河南2区[牡丹亭] - 一休先生″[32716660])
            #窗口类名:MHXYMainFrame
            print '窗口句柄:%s ' % (h)
            print '窗口标题:%s' % (title)
            print '窗口类名:%s' % (clsname)
            # print '窗口大小:%s' % (win32gui.)
            print ''

            # win32gui.SetWindowPos(h,0,0,0,0,0,win32con.SWP_NOSIZE|win32con.SWP_NOZORDER) #移动到0（0,0）位置
            a = win32gui.GetWindowPlacement(h)  #获取位置信息
            if len(a)==5:
                rect = a[4]
                startX = rect[0]
                startY = rect[1]
                endX = rect[2]
                endY = rect[3]




def show_windows(hWndList):
    for h in hWndList:
        show_window_attr(h)

def getTopWindows():
    '''''
    演示如何列出所有的顶级窗口
    :return:
    '''
    hWndList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    # show_windows(hWndList)

    return hWndList

def getChildsWindows(parent):
    '''''
    演示如何列出所有的子窗口
    :return:
    '''
    if not parent:
        return

    hWndChildList = []
    win32gui.EnumChildWindows(parent, lambda hWnd, param: param.append(hWnd),  hWndChildList)
    show_windows(hWndChildList)
    return hWndChildList




'''通过传入的字符串获取窗口'''
def getMHXYWinById(id):
    hWndList = getTopWindows()
    show_window_attr(hWndList,id)






'''
测试
'''
# getMHXYWinById("梦幻西游 ONLINE")

