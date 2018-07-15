import glob
# import re
import os
from PIL import Image
'''
第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
'''

img = glob.glob(r'./test(0000-0025)/0005/*.jpg')
# print(img)
print(len(img))

# for each in img:
#     if re.match(r'.jpg$|.png$', str(each)) is not True:
#         print(each)
#         img.remove(each)
# 不知道哪里错了
# print(img)
# print(len(img))


def thumbnail_pic(img):
    for each in img:
        name, etc = os.path.splitext(each)  # 提取图片名称，可以另存为
        # print(name, etc)
        im = Image.open(each)
        w, h = im.size
        print(im.size)
        if w > 1136 or h > 640:
            im.thumbnail((1136, 640))
            im.save(name + '.jpg', 'JPEG')
        # print(im.format, im.size, im.mode)
    print('Done!')


if __name__ == '__main__':
    thumbnail_pic(img)