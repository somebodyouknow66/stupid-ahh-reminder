import customtkinter as ctk
import json
from datetime import datetime
import os 

LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keys_log.json")

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
    root.destroy()

root = ctk.CTk()
root.geometry("300x200")

root.title("stupid-ahh-reminder")
root.attributes("-topmost", True)
root.resizable(False, False)

window_width, window_height = 320, 140


label = ctk.CTkLabel(root, text="Did you bring the keys?", font=("Dubai", 25))
label.pack(pady=20)


yes_btn = ctk.CTkButton(master=root, text="Affirmative", corner_radius=15, hover_color="#2980b9", text_color="white", border_width=2, border_color="#2c3e50", command=on_yes, font=("Dubai", 15)) 
yes_btn.pack(side="left", padx=10)

yes_btn = ctk.CTkButton(master=root, text="Negative", corner_radius=15, hover_color="#630C0C", text_color="white", border_width=2, border_color="#2c3e50", fg_color="#8B0000", command=on_no, font=("Dubai", 15))
yes_btn.pack(side="left", padx=10)

root.mainloop()