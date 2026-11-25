import sys
import customtkinter as ctk
import json
from datetime import datetime
import os 

if getattr(sys, 'frozen', False):
    app_dir = os.path.dirname(sys.executable)
else: 
    app_dir = os.path.dirname(os.path.abspath(__file__))

LOG_FILE = os.path.join(app_dir, "keys_log.json")



def log_answer(answer: str) -> None:
    """Today's answer"""
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "answer": answer,
    }
    if os.path.exists(LOG_FILE): 
        with open(LOG_FILE, "r") as f: 
            try: 
                    data = json.load(f)
            except json.JSONDecodeError:
                    data = []
    else: 
        data = []
        data.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)

def on_yes():
    log_answer("affirmative")
    root.destroy() 


def on_no():
    log_answer("negative")
    label = ctk.CTkLabel(root, text="ahhh, go back you dumb goose", font=("Dubai", 16))
    label.pack(pady=5)

root = ctk.CTk()
root.geometry("600x400")

root.title("stupid-ahh-reminder")
root.attributes("-topmost", True)
root.resizable(False, False)

window_width, window_height = 320, 140


label = ctk.CTkLabel(root, text="Did you bring the keys?", font=("Dubai", 25))
label.pack(pady=20)

button_frame = ctk.CTkFrame(root, fg_color="transparent")
button_frame.pack(pady=100)


yes_btn = ctk.CTkButton(master=button_frame, text="Affirmative", corner_radius=15, hover_color="#2980b9", text_color="white", border_width=2, border_color="#2c3e50", command=on_yes, font=("Dubai", 15)) 
yes_btn.pack(side="left", padx=1)

yes_btn = ctk.CTkButton(master=button_frame, text="Negative", corner_radius=15, hover_color="#630C0C", text_color="white", border_width=2, border_color="#2c3e50", fg_color="#8B0000", command=on_no, font=("Dubai", 15))
yes_btn.pack(side="left", padx=10)

root.mainloop()