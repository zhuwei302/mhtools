__author__ = 'zhuwei'
#coding=utf-8
'''
Created on 2016-5-26

@author: zhuwei
'''
import win32con
import win32gui
import win32api
import time
import autopy
import utils.MouseAndKeyboardUtils
from win32gui import *
from pprint import pprint
from ctypes import windll


'''转换编码'''
def gbk2utf8(s):
    return s.decode('gbk').encode('utf-8')


'''显示窗口属性并返回窗口句柄'''
def getWindow(hWndList,id):
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
            break

    return h



'''移动鼠标到窗口中央'''
def setMousePositonByHwn(h):
    # win32gui.SetWindowPos(h,0,0,0,0,0,win32con.SWP_NOSIZE|win32con.SWP_NOZORDER) #移动到0（0,0）位置
    a = win32gui.GetWindowPlacement(h)  # 获取位置信息
    if len(a) == 5:
        rect = a[4]
        startX = rect[0]
        startY = rect[1]
        endX = rect[2]
        endY = rect[3]
        print(startX, startY, endX, endY)
        m_posX = startX + (endX - startX) / 2
        m_posY = startY + (endY - startY) / 2
        utils.MouseAndKeyboardUtils.mouse_dclick(m_posX, m_posY)
        # str = 'hello'
        # utils.MouseAndKeyboardUtils.key_input(str)



'''遍历窗口集合'''
def show_windows(hWndList):
    for h in hWndList:
        getWindow(h)

'''获取所有窗口列表'''
def getTopWindows():
    '''''
    演示如何列出所有的顶级窗口
    :return:
    '''
    hWndList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    # show_windows(hWndList)

    return hWndList


'''获取子窗口'''
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


'''窗口置前'''
def windowToTop(hwnd):
    win32gui.SetForegroundWindow(hwnd)



'''喊话'''
def talk(h):
    a = win32gui.GetWindowPlacement(h)  # 获取位置信息
    if len(a) == 5:
        rect = a[4]
        startX = rect[0]
        startY = rect[1]
        endX = rect[2]
        endY = rect[3]
        print(startX, startY, endX, endY)
        m_posX = startX + (endX - startX) / 4
        m_posY = endY - 15
        autopy.mouse.smooth_move(m_posX,m_posY)
        windowToTop(h)
        # utils.MouseAndKeyboardUtils.mouse_dclick(m_posX, m_posY)
        # str = 'hello'
        # utils.MouseAndKeyboardUtils.key_input(str)
    # 模拟按下上键
    time.sleep(0.5)
    win32api.keybd_event(0x26, 0, 0, 0)
    print("up down")
    win32api.keybd_event(0x26, 0, win32con.KEYEVENTF_KEYUP, 0)
    print("up up")
    # 模拟按下回车键
    win32api.keybd_event(0x0D, 0, 0, 0)
    print("enter down")
    win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)
    print("enter up")






'''通过传入的字符串获取窗口'''
def getMHXYWinById(id):
    hWndList = getTopWindows()
    h = getWindow(hWndList,id)
    #窗口置前
    # windowToTop(h)
    #发话
    talk(h)






'''
测试
'''
# getMHXYWinById("梦幻西游 ONLINE")

