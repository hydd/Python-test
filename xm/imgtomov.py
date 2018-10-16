import cv2
import glob
import os.path


def wirteToMovie(imgs, movpath, imgpath, dirfile):  # 将图片写入视频
    fps = 24  # 视频帧率
    size = cv2.imread(dirfile).shape
    movsize = (size[1], size[0])
    print(movsize)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    videoWriter = cv2.VideoWriter(movpath, fourcc, fps,
                                  movsize)  # 视频分辨率必须和图片分辨率一样！！！

    for img in imgs:
        # print(img)
        im = cv2.imread(imgpath + str(img) + '.jpg')
        # print(imgpath + str(img) + '.jpg')
        cv2.imshow('Img', im)
        cv2.waitKey(int(1000 / int(fps)))
        videoWriter.write(im)
    videoWriter.release()


def getImg(imgpath):  # 得到所有图片
    imgs = glob.glob(imgpath + '*.jpg')
    # print(len(imgs))
    # print(sortImg(imgs))
    return sortImg(imgs)


def sortImg(imgs):  # 对图片按照文件名排序
    imglist = []
    for img in imgs:
        imglist.append(int(os.path.basename(img).split('.')[0]))
    imglist.sort()
    return imglist


def getImgType(img):
    return


def getDirFile(imgpath, img):
    return imgpath + str(img[0]) + '.jpg'


if __name__ == '__main__':
    # mov = '/Users/yycx/VScode/python/xm/overwatch.avi'
    mov = '/Users/yycx/VScode/python/Python-test/xm/mov.avi'
    # imgpath = '/Users/yycx/VScode/python/xm/overwatch/'
    imgpath = '/Users/yycx/VScode/python/Python-test/xm/img/'
    # dirfile = '/Users/yycx/VScode/python/xm/overwatch/1.jpg'
    # print(getDirFile(imgpath, getImg(imgpath)))
    dirfile = getDirFile(imgpath, getImg(imgpath))
    wirteToMovie(getImg(imgpath), mov, imgpath, dirfile)
