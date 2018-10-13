# 导入cv模块
import cv2
#读取图像，支持 bmp、jpg、png、tiff 等常用格式
for i in range(0, 580):
    img = cv2.imread('/Users/yycx/VScode/python/xm/overwatch/' + str(i) +
                     '.jpg')
    cv2.imshow('image', img)
    cv2.waitKey(2)

#释放窗口
cv2.destroyAllWindows()