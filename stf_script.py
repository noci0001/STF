import cv2
import pygame
import time
from video_functions import play_game, play_sequential_videos

video_intro = '/Users/sam/Desktop/STF_script/assets/intro-STF.mp4'
video_path0 = '/Users/sam/Desktop/STF_script/assets/From_green_to_healthy.mp4'
video_path1 = '/Users/sam/Desktop/STF_script/assets/new_main_animation.mp4'  # Replace with the correct absolute path for the first video
video_path2 = '/Users/sam/Desktop/STF_script/assets/From_healthy_to_green.mp4'  # Replace with the correct absolute path for the second video

if __name__ == "__main__":
    while (1):
        play_sequential_videos(video_intro, video_path0,video_path1, video_path2)
                          