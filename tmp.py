# -*- encoding:UTF-8 -*-
ttt=[]
with open('D:\Profile\Desktop\\d.txt') as color:
    for line in color.readlines():
        # print repr(line)
        lst = line.split('\t')
        ttt.append('{color_name} = wx.Colour({color_rgb}) # {HEX}'.format(color_name=lst[0],
                                                                      color_rgb=lst[1].replace(' ', ','),
                                                                      HEX=lst[2].strip('\n')))

ttt.sort()
for t in ttt:
    print t