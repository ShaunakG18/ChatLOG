import customtkinter as ctk
import requests

BASE_URL = "https://fastapi-chat-c9ge.onrender.com"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Messenger")
app.geometry("700x600")
app.minsize(500, 500)


main_frame = ctk.CTkFrame(app)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

input_frame = ctk.CTkFrame(main_frame)
input_frame.pack(pady=(0, 10), fill="x")

chat_frame = ctk.CTkScrollableFrame(main_frame, width=600, height=400)
chat_frame.pack(pady=10, fill="both", expand=True)

status_label = ctk.CTkLabel(main_frame, text="", font=("Arial", 14))
status_label.pack(pady=(5, 0))

chat_labels = []  

def update_chat_log():
    try:
        res = requests.get(f"{BASE_URL}/get_messages")
        data = res.json()
        for widget in chat_frame.winfo_children():
            widget.destroy()
        chat_labels.clear()

        for msg in data["chat"]:
            text = f"{msg['name']}: {msg['message']}"
            label = ctk.CTkLabel(chat_frame, text=text, anchor="w", justify="left", wraplength=550)
            label.pack(anchor="w", pady=2, padx=5)
            chat_labels.append(label)

        chat_frame._parent_canvas.yview_moveto(1.0)
    except Exception as e:
        status_label.configure(text=f"❌ Could not load chat: {str(e)}")

def update_chat_loop():
    update_chat_log()
    app.after(3000, update_chat_loop)


def send():
    uname = name_entry.get()
    msg = message_entry.get()
    if not uname or not msg:
        status_label.configure(text="Please enter both username and message.")
        return
    try:
        res = requests.post(f"{BASE_URL}/send_message", json={
            "name": uname,
            "message": msg
        })
        message_entry.delete(0, "end")
        update_chat_log()
        status_label.configure(text=res.json().get("message", "Sent!"))
    except Exception as e:
        status_label.configure(text=f"❌ API error: {str(e)}")


name_entry = ctk.CTkEntry(input_frame, placeholder_text="Username")
name_entry.pack(side="left", fill="x", expand=True, padx=(0, 10), pady=10)

message_entry = ctk.CTkEntry(input_frame, placeholder_text="Message")
message_entry.pack(side="left", fill="x", expand=True, padx=(0, 10), pady=10)

send_button = ctk.CTkButton(input_frame, text="Send", command=send)
send_button.pack(side="left", pady=10)


update_chat_loop()
app.mainloop()
