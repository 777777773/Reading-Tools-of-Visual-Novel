import pyautogui
import subprocess
import time
import tkinter as tk

def capture_and_open(x, y, width, height):
    # 等待几秒以便你有时间切换到你想截图的窗口
    time.sleep(0)
    
    # 捕获屏幕特定区域的截图
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    
    # 保存截图
    screenshot_path = "screenshot.png"
    screenshot.save(screenshot_path)
    
    #对图片进行黑白化取字
    subprocess.Popen(['python', 'otsu.py'])
    

    # time.sleep(0.1)
    # subprocess.Popen(['python', 'api.py', '1.png'])

    #利用windows.py生成字幕弹窗，通过引用api.py中的参数直接同步调用
    time.sleep(0.1)
    subprocess.Popen(['python', 'windows.py', '1.png'])



# 调整两次截图的图片分辨率以捕获屏幕上的不同区域
x = 592  #第一次截图的第一个坐标
y = 1282  #第一次截图的第二个坐标
x1 = 2038  #第二次截图的第一个坐标
y1 = 1474  #第二次截图的第二个坐标
width = x1-x  # 区域的宽度
height = y1-y  # 区域的高度


capture_and_open(x, y, width, height)
