#coding=utf-8

from pytesser import *
import ImageEnhance
# image = Image.open('D:\\1.png')
#
# #使用ImageEnhance可以增强图片的识别率
# enhancer = ImageEnhance.Contrast(image)
# image_enhancer = enhancer.enhance(4)
# print image_to_string(image_enhancer)
#


im = Image.open("D:\\1.png")
bg = Image.new("RGB", im.size, (255,255,255))
bg.paste(im,im)
print image_to_string(bg)