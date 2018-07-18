'''
第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片
'''
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def get_Char():  # 获取随机字母
    ran_char = []
    for i in range(4):
        r_c = random.randint(65, 90)
        r_c_1 = chr(r_c)
        ran_char.append(r_c_1)
    return ran_char


def getRandomColor():  # 获取随机颜色
    return (random.randint(0, 255), random.randint(0, 255),
            random.randint(0, 255))


def getPiture():  # 图片绘制
    width = 240
    height = 60
    image = Image.new('RGB', (width, height), getRandomColor())  # 创建画布
    font = ImageFont.truetype('arial.ttf', 40)  # 设置字体
    draw = ImageDraw.Draw(image)
    code = get_Char()  # 随即验证码
    # print(code)
    for t in range(4):
        draw.text(
            (60 * t + 10, 0), code[t], font=font, fill=getRandomColor())  # 绘制
    image = image.filter(ImageFilter.BLUR)  # 图像模糊
    for i in range(random.randint(1500, 3000)):  # 添加噪点
        draw.point(
            (random.randint(0, width), random.randint(0, height)),
            fill=getRandomColor())
    image.save('test.jpg')
    image.show()


if __name__ == '__main__':
    getPiture()
