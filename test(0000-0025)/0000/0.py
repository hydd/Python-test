from PIL import Image, ImageFont, ImageDraw
img = Image.open('0.jpg')
# img.show()
w, h = img.size  # 获取长宽
print(w, h)
font = ImageFont.truetype('arial.ttf', 300)
draw = ImageDraw.Draw(img)  # 生成
draw.text((4 * w / 5, 0), '5', fill=(255, 10, 10), font=font)  # 绘制
img.save('0.png')
Image.open('0.png').show()