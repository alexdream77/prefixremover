import os
import tkinter as tk
from tkinter import filedialog

def remove_prefix(prefix, folder_path):
    for filename in os.listdir(folder_path):
        if filename.startswith(prefix):
            new_filename = filename[len(prefix):]
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

def remove_prefix_gui():
    prefix = prefix_entry.get()
    folder_path = folder_entry.get()

    if not prefix or not folder_path:
        result_label.config(text="Please enter both prefix and folder path.")
        return

    try:
        remove_prefix(prefix, folder_path)
        result_label.config(text="Prefix removed successfully.")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("Remove Prefix from File Names")
root.geometry("400x200")

prefix_label = tk.Label(root, text="Prefix to Remove:")
prefix_label.pack()

prefix_entry = tk.Entry(root)
prefix_entry.pack()

folder_label = tk.Label(root, text="Folder Path:")
folder_label.pack()

folder_entry = tk.Entry(root)
folder_entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.pack()

remove_button = tk.Button(root, text="Remove Prefix", command=remove_prefix_gui)
remove_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
