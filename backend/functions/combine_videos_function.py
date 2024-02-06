import os
import random
from moviepy.editor import *


def combine_videos(timestamp):

    video2_folder = f"{timestamp}/image_videos"
    video2_files = sorted(os.listdir(video2_folder),
                          key=lambda x: int(x.split(".")[0]))

    clips = []
    for i in range(len(video2_files)):
        video2 = VideoFileClip(os.path.join(video2_folder, video2_files[i]))

        clips.append(video2)

    final_clip = concatenate_videoclips(clips, method='compose')
    final_clip.write_videofile(
        f"{timestamp}/final_video.mp4", codec="libx264", fps=25)
