import tkinter as tk
from api import chinese_content  


# 创建一个顶级窗口
window = tk.Tk()
# 要求创建无边框窗口
window.overrideredirect(True)
# 设置窗口大小和位置
window.geometry("1280x30+0+0")  # 宽x高+水平偏移量+垂直偏移量
window.title("视觉小说阅读器")

# 设置窗口置于顶层
window.attributes("-topmost", True)

# 在窗口中添加一个标签来显示中文内容，使用黑体字体和20号大小
label = tk.Label(window, text=chinese_content, font=("黑体", 20), padx=10, pady=10)
label.pack()

# 定时器函数，关闭窗口
def close_window():
    window.destroy()

# 30秒后执行关闭窗口的函数，以释放内存
window.after(30000, close_window)

# 开始主循环
window.mainloop()
