import cv2
import pygame
import time
from music import play_background_music
from buttons import draw_info_button, draw_info_overlay

def hold_last_frame(video_path, display_time=30):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    last_frame = None

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        last_frame = frame
        cv2.imshow("Last Frame", last_frame)
        key = cv2.waitKey(1) & 0xFF

        if key == 27:  # Check for the "Escape" key (key code 27)
            break  # Exit the loop and end the program

    cap.release()

    if last_frame is not None:
        cv2.imshow("Last Frame", last_frame)
        cv2.waitKey(1)
        time.sleep(display_time)
        cv2.destroyWindow("Last Frame")

    else:
        print("Error: Could not retrieve frames from the video.")

def play_game(cap0, cap1, cap2, button_sound, button_i, frame_rate0, frame_rate1, frame_rate2, music_path, video_path2):
    
    overlay_visible = False
    prev_video = False
    prev_i_pressed = -1
    language = True
    
    play_background_music(music_path)
    #screen from green/muddy to healthy blue
    while True:
        ret0, frame0 = cap0.read()

        if not ret0:
            break

        if overlay_visible:
            draw_info_overlay(frame0, language)

        draw_info_button(frame0, language)
        cv2.imshow('Video Playback', frame0)

        key = cv2.waitKey(1000 // frame_rate0) & 0xFF
        if key == 27:  # Check for the "Escape" key (key code 27)
            button_sound.play()
            time.sleep(1)
            pygame.mixer.music.stop()
            break
        elif key == ord('i'):
            button_i.play()
            #pygame.mixer.music.stop()
            overlay_visible = not overlay_visible
            prev_video = None
            prev_i_pressed *= -1
        elif key == ord('l'):
            if language == True:
                language = False
            else:
                language = True
        if (key == ord('Q')):
            cap0.release()
            cap1.release()
            cap2.release()
            cv2.destroyAllWindows() 

    while True:
        ret1, frame1 = cap1.read()

        if not ret1:
            break

        if overlay_visible:
            draw_info_overlay(frame1, language)

        draw_info_button(frame1, language)
        cv2.imshow('Video Playback', frame1)

        key = cv2.waitKey(1000 // frame_rate1) & 0xFF
        if key == 27:  # Check for the "Escape" key (key code 27
            button_sound.play()
            time.sleep(1)
            pygame.mixer.music.stop()
            break
        elif key == ord('i'):
            button_i.play()
            #pygame.mixer.music.stop()
            overlay_visible = not overlay_visible
            prev_video = None
            prev_i_pressed *= -1
        elif key == ord('l'):
            if language == True:
                language = False
            else:
                language = True
        if (key == ord('Q')):
            cap0.release()
            cap1.release()
            cap2.release()
            cv2.destroyAllWindows() 

    while True:
        ret2, frame2 = cap2.read()

        if not ret2:
            break

        if overlay_visible:
            draw_info_overlay(frame2, language)

        draw_info_button(frame2, language)
        cv2.imshow('Video Playback', frame2)

        key = cv2.waitKey(1000 // frame_rate2) & 0xFF
        if key == 27:  # Check for the "Escape" key (key code 27)
            button_sound.play()
            time.sleep(1)
            pygame.mixer.music.stop()
            break
        elif key == ord('i'):
            button_i.play()
            # pygame.mixer.music.stop()
            #stf_stl.play()
            #time.sleep(20)
            overlay_visible = not overlay_visible
            #prev_video = video_path2
            #prev_i_pressed *= -1
            #play_background_music(music_path)
        elif key == ord('l'):
            if language == True:
                language = False
            else:
                language = True
    
    hold_last_frame(video_path2)
    
    cap0.release()
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()

def play_sequential_videos(video_intro, video_path0, video_path1, video_path2):
    pygame.init()
    
    # Call the function to play the music
    music_path = '/Users/sam/Desktop/STF_script/assets/background.mp3'

    button_sound = pygame.mixer.Sound('/Users/sam/Desktop/STF_script/assets/bonus.wav')
    button_i = pygame.mixer.Sound('/Users/sam/Desktop/STF_script/assets/pressed_i.wav')
    button_stf = pygame.mixer.Sound('/Users/sam/Desktop/STF_script/assets/save-the-fishes.wav')
    stf_stl = pygame.mixer.Sound('/Users/sam/Desktop/STF_script/assets/stf_stl.wav')
    
    capminus = cv2.VideoCapture(video_intro)
    cap0 = cv2.VideoCapture(video_path0)
    cap1 = cv2.VideoCapture(video_path1)
    cap2 = cv2.VideoCapture(video_path2)
    language = True

    if not cap0.isOpened() or not capminus.isOpened() or not cap1.isOpened() or not cap2.isOpened():
        print("Error: Could not open videos.")
        return
    frame_rateminus = int(capminus.get(cv2.CAP_PROP_FPS))
    frame_rate0 = int(cap0.get(cv2.CAP_PROP_FPS))
    frame_rate1 = int(cap1.get(cv2.CAP_PROP_FPS))
    frame_rate2 = int(cap2.get(cv2.CAP_PROP_FPS))
    
    #CAPMINUS
    
    while True:
    
        retminus, frame_intro = capminus.read()

        if not retminus:
            break

        cv2.imshow('Video Playback', frame_intro)

        key = cv2.waitKey(1000 // frame_rateminus) & 0xFF
        if key == ord(' '):
            if (button_stf.play()):
                time.sleep(2)
                play_game(cap0, cap1, cap2, button_sound, button_i, frame_rate0, frame_rate1, frame_rate2, music_path, video_path2)
