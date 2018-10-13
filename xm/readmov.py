import cv2
videoCapture = cv2.VideoCapture()
videoCapture.open('/Users/yycx/VScode/python/xm/1.mp4')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
#fps是帧率，意思是每一秒刷新图片的数量，frames是一整段视频中总的图片数量。
print("fps=", fps, "frames=", frames)
# i = 0
for i in range(int(frames)):
    # print(i)
    success, frame = videoCapture.read()
    if success:
        cv2.imshow("Oto Video", frame)
        cv2.waitKey(int(1000 / fps))
        # cv2.destroyAllWindows()
        cv2.imwrite("/Users/yycx/VScode/python/xm/overwatch/%d.jpg" % i, frame)
        # success, frame = videoCapture.read()
        # i += 1
