import socket
import threading
import sys
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox


HOST = "127.0.0.1"
PORT = 1234

DARK_GREY = "#121212"
MEDIUM_GREY = "#1F1B24"
OCEAN_BLUE = "#464EB8"
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def add_message(message):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, f"{message}\n")
    message_box.config(state=tk.DISABLED)


def connect():
    try:
        client.connect((HOST, PORT))
    except:
        messagebox.showerror(
            "Unable to connect to server", f"Unable to connect to server {HOST} {PORT}"
        )
        sys.exit()
    else:
        add_message("[SERVER] Successfully connected to the server")
        username = username_textbox.get()
        if username != "":
            client.sendall(username.encode())
            username_textbox.config(state=tk.DISABLED)
            username_button.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Invalid Username", "Username cannot empty")
            sys.exit()
        threading.Thread(target=listen_for_messages_from_server, args=(client,)).start()


def send_message():
    msg = message_textbox.get()
    if msg != "":
        client.sendall(msg.encode())
        message_textbox.delete(0, len(msg))
    else:
        messagebox.showerror("Empty Message", f"Message cannot be empty")


root = tk.Tk()
root.geometry("600x600")
root.title("VMessenger")
root.resizable(False, False)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_rowconfigure(2, weight=1)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        exit()


root.protocol("WM_DELETE_WINDOW", on_closing)

top_frame = tk.Frame(root, width=600, height=100, bg=DARK_GREY)
top_frame.grid(row=0, column=0, sticky=tk.NSEW)

mid_frame = tk.Frame(root, width=600, height=400, bg=MEDIUM_GREY)
mid_frame.grid(row=1, column=0, sticky=tk.NSEW)

bot_frame = tk.Frame(root, width=600, height=100, bg=DARK_GREY)
bot_frame.grid(row=2, column=0, sticky=tk.NSEW)

username_label = tk.Label(
    top_frame, text="Enter Username: ", font=FONT, bg=DARK_GREY, fg=WHITE
)
username_label.pack(side=tk.LEFT, padx=10)

username_textbox = tk.Entry(top_frame, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=23)
username_textbox.pack(side=tk.LEFT)

username_button = tk.Button(
    top_frame, text="Join", font=FONT, bg=OCEAN_BLUE, fg=WHITE, command=connect
)
username_button.pack(side=tk.LEFT)

message_textbox = tk.Entry(bot_frame, bg=MEDIUM_GREY, fg=WHITE, font=FONT, width=38)
message_textbox.pack(side=tk.LEFT, padx=10)

message_button = tk.Button(
    bot_frame,
    text="Send",
    bg=OCEAN_BLUE,
    fg=WHITE,
    font=BUTTON_FONT,
    command=send_message,
)
message_button.pack(side=tk.LEFT, padx=10)

message_box = scrolledtext.ScrolledText(
    mid_frame, font=SMALL_FONT, bg=MEDIUM_GREY, fg=WHITE, width=67, height=26.5
)
message_box.config(state=tk.DISABLED)
message_box.pack(side=tk.TOP)


def main():
    root.mainloop()


def listen_for_messages_from_server(client):
    while True:
        message = client.recv(2048).decode("utf-8")
        if message != "":
            username, messg, date = message.split("~")
            add_message(f"[{username}] {messg} send at {date}")
        else:
            messagebox.showerror(
                "Empty Message", f"Message received from {client} is empty"
            )


if __name__ == "__main__":
    main()
