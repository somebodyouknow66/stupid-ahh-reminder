import tkinter as tkinter

root = tkinter.Tk()

root.title("stupid-ahh-reminder")
root.attributes("-topmost", True)
root.resizable(False, False)

window_width, window_height = 320, 140

label = tkinter.Label(root, text="Did you bring the keys?", font=("Segoe UI", 13))
label.pack(pady=20)

button_frame = tkinter.Frame(root)
button_frame.pack()

yes_btn = tkinter.Button(button_frame, text="Affirmative", width=10)
yes_btn.pack(side="left", padx=10)

no_button = tkinter.Button(button_frame, text="yes", width="10")
no_button.pack(side="left")

root.mainloop()