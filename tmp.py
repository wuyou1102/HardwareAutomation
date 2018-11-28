# -*- encoding:UTF-8 -*-
with open('D:\Profile\Desktop\\d.txt') as color:
    for line in color.readlines():
        # print line
        lst = line.split('\t')
        print '{color_name} = wx.Colour({color_rgb}) # {chinese_name} {HEX} '.format(color_name=lst[1],
                                                                                     color_rgb=lst[4].strip('\r\n'),
                                                                                     chinese_name=lst[2], HEX=lst[3])
