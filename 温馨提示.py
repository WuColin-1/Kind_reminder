import tkinter as tk
import random 
import math

root = tk.Tk()

screem_w=root.winfo_screenwidth()
screem_v=root.winfo_screenheight()


root.geometry(f"300x150+{math.floor(screem_w/2)}+{math.floor(screem_v/2)}")
root.title("退出提示")
root.config(bg="skyblue")
label=tk.Label(
    root,
    text="按esc结束程序",
    font=("Arial", 30), 
    fg="black",
    bg="skyblue"

)
label.pack(expand=True)
messages = [
    "累了吗？休息一下",
    "深呼吸，让自己放松",
    "今天也要保持微笑",
    "喝杯热茶，让自己暖和",
    "不要太逼自己，慢慢来",
    "小小休息也很重要",
    "记得抬头看看窗外",
    "好好吃午餐哦",
    "给自己一点奖励吧",
    "天气冷了，多穿点衣服",
    "晚上早点睡，明天更精神",
    "保持好心情，事情会更顺利",
    "你很棒，不要忘记赞美自己",
    "照顾好自己，也照顾心情",
    "别忘了喝水，多补充能量",
    "适当放空，让自己轻松",

]
color = [
    # 经典暖色系
    "#FFE4E1",  # MistyRose
    "#FFDAB9",  # PeachPuff
    "#FFA07A",  # LightSalmon
    "#FFFACD",  # LemonChiffon
    "#FFE4B5",  # Moccasin
    "#F5DEB3",  # Wheat

    # 淡暖中性色
    "#FFEBCD",  # BlanchedAlmond
    "#FFEFD5",  # PapayaWhip
    "#FFE4C4",  # Bisque
    "#FFDEAD",  # NavajoWhite
    "#FAFAD2",  # LightGoldenrod

    # 梦幻暖粉系
    "#FFB6C1",  # LightPink
    "#D8BFD8",  # Thistle
    "#DDA0DD",  # Plum
    "#FFF0F5",  # LavenderBlush

    # 活力暖橙系
    "#FF7F50",  # Coral
    "#FA8072",  # Salmon
    "#F4A460",  # SandyBrown
    "#DEB887",  # BurlyWood
    "#F08080",  # LightCoral
]

def on_key_press(event):
    if event.keysym=="Escape":
        root.destroy()
root.bind("<Key>",on_key_press)

def show_window(index=0):
    win = tk.Toplevel()                 # 创建新窗口
    win.title(f"温馨提示")
    win.geometry(f"300x150+{random.randint(0,screem_w)}+{random.randint(0,screem_v)}")  # 让窗口错位显示
    color_code=random.randint(0,len(color)-1)
    text_code=random.randint(0,len(messages)-1)
    win.config(bg=f"{color[color_code]}")
    win.bind("<Key>",lambda event: root.destroy() if event.keysym=="Escape" else None)
    label = tk.Label(win, text=messages[text_code], font=("Arial", 25), fg="black", bg=f"{color[color_code]}")
    label.pack(expand=True)
    
    # 2秒后显示下一个窗口
    root.after(500, show_window, index + 1)

# 开始显示第一个窗口
show_window()
root.mainloop()