
#merger()

import ffmpeg
import subprocess
import os
from mhmovie.code import *
video=ffmpeg.input(r'C:\Users\sagar\Desktop\ytdownload\Chamak Challo Chel ChabeliL video.mp4')
audio=ffmpeg.input(r'C:\Users\sagar\Desktop\ytdownload\Chamak Challo Chel ChabeliL song.mp4')
#out = ffmpeg.output(video, audio, 'C:\\Users\\sagar\\Desktop\\ytdownload\\ Challo Chel ChabeliL video.mp4', vcodec='copy', acodec='copy', strict='experimental')
#out.run() (2\
print(os.cmd)
print(os.listdir('D:\\New folder (2)\\'))

def merger():
	vid=movie('D:\\New folder (2)\\video.mp4')
	aud=music('D:\\New folder (2)\\audio.mp4')
	final=vid=aud
	final.save('output.mp4')

