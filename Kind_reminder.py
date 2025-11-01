import tkinter as tk
import random 

root = tk.Tk()
# get the size of the screem
screem_w=root.winfo_screenwidth()
screem_v=root.winfo_screenheight()

# define main window
root.geometry(f"500x150+{int(screem_w/2)}+{int(screem_v/2)}")
root.title("quit tips")
root.config(bg="skyblue")
label=tk.Label(
    root,
    text="press Esc to quit the programm", # way to quit the progamm
    font=("Arial", 30), 
    fg="black",
    bg="skyblue"

)
label.pack(expand=True)
# messages and colors lists
messages = [
    "Tired? Have a rest",
    "Take a deep breath and relax",
    "Keep smiling today",
    "Have a cup of warm tea to feel cozy",
    "Don't push yourself too hard, take it easy",
    "Even a short break is important",
    "Remember to look up and enjoy the view outside",
    "Have a good lunch",
    "Give yourself a small reward",
    "It's cold, wear some extra clothes",
    "Go to bed early tonight to feel refreshed tomorrow",
    "Maintain a good mood, things will go smoother",
    "You are great, don't forget to praise yourself",
    "Take care of yourself and your mood",
    "Don't forget to drink water and stay hydrated",
    "Take some time to relax and unwind",
]
color = [
    # Classic warm colors
    "#FFE4E1",  # MistyRose
    "#FFDAB9",  # PeachPuff
    "#FFA07A",  # LightSalmon
    "#FFFACD",  # LemonChiffon
    "#FFE4B5",  # Moccasin
    "#F5DEB3",  # Wheat

    # Light warm neutral colors
    "#FFEBCD",  # BlanchedAlmond
    "#FFEFD5",  # PapayaWhip
    "#FFE4C4",  # Bisque
    "#FFDEAD",  # NavajoWhite
    "#FAFAD2",  # LightGoldenrod

    # Dreamy warm pink colors
    "#FFB6C1",  # LightPink
    "#D8BFD8",  # Thistle
    "#DDA0DD",  # Plum
    "#FFF0F5",  # LavenderBlush

    # Energetic warm orange colors
    "#FF7F50",  # Coral
    "#FA8072",  # Salmon
    "#F4A460",  # SandyBrown
    "#DEB887",  # BurlyWood
    "#F08080",  # LightCoral
]

# captrue the event from keyboard
def on_key_press(event):
    if event.keysym=="Escape":
        root.destroy()
root.bind("<Key>",on_key_press)
 

# Create a new window
def show_window(index=0):
    win = tk.Toplevel() 
    win.title(f"Tip")
    win.geometry(f"600x200+{random.randint(0,screem_w)}+{random.randint(0,screem_v)}")  # Offset window display
    color_code=random.randint(0,len(color)-1)
    text_code=random.randint(0,len(messages)-1)
    win.config(bg=f"{color[color_code]}")
    win.bind("<Key>",lambda event: root.destroy() if event.keysym=="Escape" else None)
    label = tk.Label(win, text=messages[text_code], font=("Arial", 25), fg="black", bg=f"{color[color_code]}")
    label.pack(expand=True)
    
    # Show the next window after 0.5 seconds
    root.after(500, show_window, index + 1)

# show the first window
show_window()
root.mainloop()