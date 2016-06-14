__author__ = 'zhuwei'
#coding=utf-8

import MhxyHelperUIAction
from Tkinter import *


# def btnOnClick():
#     label['text'] = "游戏名称"


root = Tk(className="MhxyHelper") #窗口标题


'''标签'''
label = Label(root,text="游戏ID").grid(row=0,column=0) #创建标签


'''文本框'''
text = StringVar()
text.set("请输入游戏ID")
entry = Entry(root)
entry['textvariable'] = text
entry.grid(row=0,column=1)


'''按钮'''
button = Button(root,text="开始押镖",command=lambda:MhxyHelperUIAction.beginYb(entry)).grid(row=1,column=1)





root.mainloop()