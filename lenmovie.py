from moviepy.editor import VideoFileClip
import glob
import time
from numba import jit


@jit
def getMoviesTime():
    start = time.time()
    movies = glob.glob(r'/Users/yycx/学习资料/machine-learning-2014/*.mkv')
    all_time = 0
    for movie in movies:
        clip = VideoFileClip(movie)
        all_time += clip.duration
        movie_time = str(int(clip.duration / 60)) + ":" + str(
            int(clip.duration % 60))
        print(movie + "  " + movie_time)
    print(all_time)
    print("总时长：" + str(int(all_time / 3600)) + ":" +
          str(int((all_time % 3600) / 60)) + ":" + str(int(all_time % 60)))
    elapsed = (time.time() - start)
    print("Time used:", elapsed)


getMoviesTime()
