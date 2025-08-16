from TkAccessory import TkAtomicLoading
import customtkinter as tk #use customtkinter

loading_text = "Loading"
loading_pattern = "."

def change():
    global loading_pattern , loading_text

    if loading_text[-3:] != "...":
        loading_text += loading_pattern
    else:
        loading_text = loading_text[:-3]

    progress1.move(loading_text)
    progress2.move(loading_text)
    progress3.move(loading_text)
    progress4.move(loading_text)
    progress5.move(loading_text)
    progress6.move(loading_text)
    progress7.move()
    progress8.move()
    progress9.move()

    window.after(70,lambda : change())

window = tk.CTk()
window.title('TkTools')
window.configure(fg_color="black")
window.resizable(False,False)
window.geometry('500x500')

canvas = tk.CTkCanvas(window,width=400,height=400,bg="black",highlightthickness=0)
canvas.place(x=250,y=250,anchor="center")

progress1 = TkAtomicLoading(canvas,1,(80,80),100,10,bg_color="black",text=loading_text,text_font=("Aria",10,"bold"),text_angle=10,text_color="white",speed=10)
progress2 = TkAtomicLoading(canvas,2,(200,80),100,10,bg_color="black",text=loading_text,text_font=("Aria",10,"bold"),text_angle=10,text_color="white",speed=10,loading_colors=["#ff0000","#ff0000","#fa4646","#fa4646","#ff7a7a","#ff7a7a"])
progress3 = TkAtomicLoading(canvas,3,(320,80),100,10,bg_color="black",text=loading_text,text_font=("Aria",10,"bold"),text_angle=10,text_color="white",speed=10,loading_colors=["#00ff08","#00ff08","#42ff49","#42ff49","#81f785","#81f785"])

progress4 = TkAtomicLoading(canvas,4,(80,200),100,10,bg_color="blue",text=loading_text,text_font=("Aria",10,"bold"),text_angle=10,text_color="white",speed=10)
progress5 = TkAtomicLoading(canvas,5,(200,200),100,10,bg_color="red",text=loading_text,text_font=("Aria",10,"bold"),text_angle=10,text_color="white",speed=10,loading_colors=["#ff0000","#ff0000","#fa4646","#fa4646","#ff7a7a","#ff7a7a"])
progress6 = TkAtomicLoading(canvas,6,(320,200),100,10,bg_color="green",text=loading_text,text_font=("Aria",10,"bold"),text_angle=10,text_color="white",speed=10,loading_colors=["#00ff08","#00ff08","#42ff49","#42ff49","#81f785","#81f785"])

progress7 = TkAtomicLoading(canvas,7,(80,320),50,20,bg_color="white",text="",speed=10)
progress8 = TkAtomicLoading(canvas,8,(200,320),50,20,bg_color="white",text="",speed=10,loading_colors=["#ff0000","#ff0000","#fa4646","#fa4646","#ff7a7a","#ff7a7a"])
progress9 = TkAtomicLoading(canvas,9,(320,320),50,20,bg_color="white",text="",speed=10,loading_colors=["#00ff08","#00ff08","#42ff49","#42ff49","#81f785","#81f785"])

window.after(50,lambda : change())

tk.CTkLabel(window,text="TkAccessory",text_color="white",font=("Aria",15,"bold"),justify="left").place(x=10,y=430,anchor="nw")
tk.CTkLabel(window,text="Make your UI more interesting",text_color="white",font=("Aria",10,"italic"),justify="left").place(x=10,y=450,anchor="nw")
tk.CTkLabel(window,text="pip install TkAccessory",text_color="white",font=("Aria",10,"italic"),justify="left").place(x=10,y=470,anchor="nw")

window.mainloop()