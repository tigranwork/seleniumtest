import tkinter as tk
from tkinter import messagebox


def on_button_click():
    messagebox.showinfo("Greeting", "Hello World")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hello App")

    btn = tk.Button(root, text="Click Me", command=on_button_click)
    btn.pack(padx=20, pady=20)

    root.mainloop()
