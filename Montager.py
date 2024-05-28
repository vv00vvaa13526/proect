#Перед использованием установите библиотеки moviepy, pyautogui

import os
import pyautogui
from moviepy.editor import *





vid_or_img = pyautogui.confirm(title="ВОПРОС", text="Что надо смонтировать?", buttons=["Видео","Видео"])

if vid_or_img == "Видео":
    vid = "NotRickRollVideo.mp4"
    a = 0
    b = 0
    y = 0
    x = 0
    speed = 0
    g = 0
    
    vid = pyautogui.prompt(title="ВОПРОС", text="Укажите видео и его формат", default="NotRickRollVideo.mp4")
    a = pyautogui.prompt(title="ВОПРОС", text="С какой секунды начать видео?", default= "10" )
    b = pyautogui.prompt(title="ВОПРОС", text="На какой секунде закончить видео?", default= "30" )
    y = pyautogui.prompt(title="ВОПРОС", text="Какой размер видео по высоте?", default= "720" )
    x = pyautogui.prompt(title="ВОПРОС", text="Какой размер видео по ширине?", default= "1280" )
    speed = pyautogui.prompt(title="ВОПРОС", text="Во сколько раз ускорить видео?", default= "2" )
    g = pyautogui.prompt(title="ВОПРОС", text="На сколько градусов повернуть видео?", default= "0" )
    
    new_clip = VideoFileClip(str(vid)).subclip(int(a),int(b)).rotate(int(g))

    new_clip = new_clip.resize((int(x), int(y)))

    new_clip = new_clip.speedx(int(speed))

    new_clip.write_videofile("new_video.mp4")

    os.startfile("new_video.mp4")
