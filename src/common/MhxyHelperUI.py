__author__ = 'zhuwei'
#coding=utf-8

import MhxyHelperUIAction
from Tkinter import *





root = Tk(className="MhxyHelper") #窗口标题
root.resizable(False,False)

root.update() # update window ,must do
curWidth = root.winfo_reqwidth() # get current width
curHeight = root.winfo_height() # get current height
scnWidth,scnHeight = root.maxsize() # get screen width and height
# now generate configuration information
tmpcnf = '%dx%d+%d+%d'%(curWidth,curHeight,
(scnWidth-curWidth)/2,(scnHeight-curHeight)/2)
root.geometry(tmpcnf)


'''标签'''
label = Label(root,text="游戏ID：").grid(row=0,column=0) #创建标签


'''文本框'''
text = StringVar()
text.set("2016")
entry = Entry(root)
entry['textvariable'] = text
entry.grid(row=0,column=1)


'''按钮'''
button = Button(root,text="开始押镖",command=lambda:MhxyHelperUIAction.beginYb(entry)).grid(row=1,column=1)





root.mainloop()