import keyboard
import subprocess
import os

def capture_and_open(x, y, width, height):
    subprocess.run(["python", "jietu.py", str(x), str(y), str(width), str(height)])

def main():
    # 获取当前脚本所在的目录
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # 监听键盘输入
    keyboard.add_hotkey('q', lambda: capture_and_open(0, 0, 100, 100))

    print("按下 'q' 键来执行截图和打开截图的功能，按下 'Esc' 键退出程序。")
    #这里选择不冲突按键为热键，可以通过修改代码选择enter为热键，便可实现同步翻页和翻译的功能
    #但由于文字出现缓慢，过场动画等原因，效果没有分别控制好
    

    try:
        # 持续监听键盘输入，直到按下 'Esc' 键退出程序
        keyboard.wait('esc')
    except KeyboardInterrupt:
        pass

    # 程序结束时移除监听
    keyboard.unhook_all()

if __name__ == "__main__":
    main()
