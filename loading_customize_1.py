from TkAccessory import TkAtomicLoading
import customtkinter as tk


radiuses1 = [1,4,6,8,10,12]
colors1 = ["blue" for _ in range(6)]

radiuses2 = [3 for _ in range(6)]
colors2 = ["blue" for _ in range(6)]

radiuses3 = [10 for _ in range(7)]
colors3 = ["#96bcfa","#87b3fa","#72a5f7","#5897fc","#3983fa","#126cfc","#0061fc"]

radiuses4 = [10 for _ in range(6)]
colors4 = ["white" for _ in range(6)]

radiuses5 = [10 for _ in range(6)]
colors5 = ["blue" for _ in range(6)]


def change_loading1(radiuses : list[int],colors : list[str],count : int = 0):
    change_radiuses = radiuses.copy()
    change_colors = colors.copy()

    change_radiuses[int(count % len(radiuses))] += 3
    change_colors[int(count % len(radiuses))] = "white"

    loading1.move(loading_radiuses=change_radiuses,loading_colors=change_colors)

    count += 0.25
    window.after(50, lambda : change_loading1(radiuses=radiuses,colors=colors,count=count))


def change_loading2(radiuses : list[int],count : int = 0):
    change_radiuses = radiuses.copy()

    change_radiuses[int(count % len(radiuses))] += 4

    loading2.move(loading_radiuses=change_radiuses)

    count += 0.25
    window.after(50, lambda : change_loading2(radiuses=radiuses,count=count))


def change_loading3(radiuses : list[int],count : int = 0,count_up : bool = True):
    count += 0.25 if count_up else -0.25
    text = "Hi" if (count > -1) else ""

    if count_up:
        if count > 3:
            count_up = False
            count = 0
    else:
        if count < -3:
            count_up = True
            count = 0

    radiuses = list(map(lambda x : x + count , radiuses))
    loading3.move(text=text,loading_radiuses=radiuses)

    window.after(50, lambda : change_loading3(radiuses=radiuses,count=count,count_up=count_up))


def change_loading4(loading : TkAtomicLoading,radiuses : list[int],count : int = 0,count_up : bool = True):
    count += 0.25 if count_up else -0.25

    if count_up:
        if count > 3:
            count_up = False
            count = 0
    else:
        if count < -3:
            count_up = True
            count = 0

    radiuses = list(map(lambda x : x + count , radiuses))
    loading.move(loading_radiuses=radiuses)

    window.after(50, lambda : change_loading4(loading=loading,radiuses=radiuses,count=count,count_up=count_up))


window = tk.CTk()
window.title("TkAccessory")
window.configure(fg_color="black")
window.geometry("500x500")
window.resizable(False,False)

canvas = tk.CTkCanvas(window,width=500,height=500,bg="black")
canvas.place(x=250,y=250,anchor="center")

loading1 = TkAtomicLoading(canvas,0,(180,180),80,bg_color="black",text="Loading ...",loading_radiuses=radiuses1,loading_colors=colors1)
loading2 = TkAtomicLoading(canvas,1,(320,180),80,bg_color="black",text="Loading ...",loading_radiuses=radiuses2,loading_colors=colors2)

loading3 = TkAtomicLoading(canvas,2,(100,320),50,bg_color="black",text="",text_font=("Robot",15,"bold"),text_color="white",loading_radiuses=radiuses3,loading_colors=colors3)
loading4 = TkAtomicLoading(canvas,3,(250,320),50,bg_color="black",text="Hi",text_font=("Robot",15,"bold"),text_color="black",loading_radiuses=radiuses4,loading_colors=colors4)
loading5 = TkAtomicLoading(canvas,4,(400,320),50,bg_color="black",text="Hi",text_font=("Robot",15,"bold"),text_color="blue",loading_radiuses=radiuses5,loading_colors=colors5)

window.after(1, lambda : change_loading1(radiuses=radiuses1,colors=colors1))
window.after(1, lambda : change_loading2(radiuses=radiuses2))
window.after(1, lambda : change_loading3(radiuses=radiuses3))

window.after(1, lambda : change_loading4(loading=loading4,radiuses=radiuses4))
window.after(1, lambda : change_loading4(loading=loading5,radiuses=radiuses5))

tk.CTkLabel(window,text="TkAccessory",text_color="white",font=("Aria",15,"bold"),justify="left").place(x=10,y=430,anchor="nw")
tk.CTkLabel(window,text="Make your UI more interesting",text_color="white",font=("Aria",10,"italic"),justify="left").place(x=10,y=450,anchor="nw")
tk.CTkLabel(window,text="pip install TkAccessory",text_color="white",font=("Aria",10,"italic"),justify="left").place(x=10,y=470,anchor="nw")

window.mainloop()