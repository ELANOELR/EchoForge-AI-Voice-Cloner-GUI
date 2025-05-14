
import tkinter as tk
import threading
import vf_launcher

def clone_voice():
    status_label.config(text="Cloning voice model...")
    threading.Thread(target=vf_launcher.run).start()
    root.after(3000, lambda: status_label.config(text="Voice model cloned successfully."))

root = tk.Tk()
root.title("VocalForge AI Voice Cloner")
root.geometry("480x220")

tk.Label(root, text="Text-to-Speech Offline Voice Tool", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="Clone Voice", command=clone_voice, font=("Arial", 12)).pack(pady=5)
status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack(pady=10)

root.mainloop()
