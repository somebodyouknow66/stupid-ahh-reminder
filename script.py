import customtkinter as ctk

root = ctk.CTk()
root.geometry("300x200")

root.title("stupid-ahh-reminder")
root.attributes("-topmost", True)
root.resizable(False, False)

window_width, window_height = 320, 140

def on_yes():
    root.destroy() 


def on_no():
    root.destroy()

label = ctk.CTkLabel(root, text="Did you bring the keys?", font=("Segoe UI", 13))
label.pack(pady=20)


yes_btn = ctk.CTkButton(master=root, text="Affirmative", corner_radius=15, hover_color="#2980b9", text_color="white", border_width=2, border_color="#2c3e50", command=on_yes)
yes_btn.pack(side="left", padx=10)

yes_btn = ctk.CTkButton(master=root, text="Negative", corner_radius=15, hover_color="#8B0000", text_color="white", border_width=2, border_color="#2c3e50", fg_color="#8B0000", command=on_no)
yes_btn.pack(side="left", padx=10)

root.mainloop()