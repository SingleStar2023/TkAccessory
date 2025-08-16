from TkAccessory import TkCircularProgress , CustomTkCircularProgress
import customtkinter as tk #use customtkinter

value = 0

def change(value):
    if value >= 100:
        value = 0

    value += 0.5

    progress1.set(value,str(int(value)))
    progress2.set(value,str(int(value)))
    progress3.set(value,str(int(value)))
    progress4.set(value,str(int(value)))
    progress5.set(value,str(int(value)))
    progress6.set(value,str(int(value)))

    window.after(3,lambda : change(value=value))

window = tk.CTk()
window.title('TkTools')
window.configure(fg_color="black")
window.resizable(False,False)
window.geometry('500x500')

canvas = tk.CTkCanvas(window,width=400,height=400,bg="black",highlightthickness=0)
canvas.place(x=250,y=250,anchor="center")

progress1 = TkCircularProgress(canvas,1,(80,80),100,8,value,text_angle=25,text_font=("Aria",20,"bold"),text="0/0",progress_color="red",head_color_start="red",head_color_end="red",bg_color="darkred",fg_color="white",text_color="black")
progress2 = TkCircularProgress(canvas,2,(200,80),100,8,value,text_angle=25,text_font=("Aria",20,"bold"),text="0/0",progress_color="blue",head_color_start="blue",head_color_end="blue",bg_color="darkblue",fg_color="lightblue",text_color="white")
progress3 = TkCircularProgress(canvas,3,(320,80),100,8,value,text_angle=25,text_font=("Aria",20,"bold"),text="0/0",progress_color="green",head_color_start="green",head_color_end="green",bg_color="darkgreen",fg_color="lightgreen",text_color="black")

progress4 = TkCircularProgress(canvas,4,(140,200),100,8,value,text_angle=25,text_font=("Aria",20,"bold"),text="0/0",progress_color="pink",head_color_start="pink",head_color_end="pink",bg_color="purple",fg_color="white",text_color="black")
progress5 = TkCircularProgress(canvas,5,(260,200),100,8,value,text_angle=25,text_font=("Aria",20,"bold"),text="0/0",progress_color="darkgray",head_color_start="darkgray",head_color_end="darkgray",bg_color="gray",fg_color="white",text_color="black")

#The custom one
progress6 = CustomTkCircularProgress(canvas,6,(200,320),100,8,value,text_angle=25,text_font=("Aria",20,"bold"),text="0/0",fg_color="black",text_color="white")

window.after(50,lambda : change(value))

tk.CTkLabel(window,text="TkAccessory",text_color="white",font=("Aria",15,"bold"),justify="left").place(x=10,y=430,anchor="nw")
tk.CTkLabel(window,text="Make your UI more interesting",text_color="white",font=("Aria",10,"italic"),justify="left").place(x=10,y=450,anchor="nw")
tk.CTkLabel(window,text="pip install TkAccessory",text_color="white",font=("Aria",10,"italic"),justify="left").place(x=10,y=470,anchor="nw")

window.mainloop()