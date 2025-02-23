import os
import tkinter as tk
from tkinter import messagebox

# Get the current user's Videos\NVIDIA path dynamically
user_videos_path = os.path.join(os.path.expanduser("~"), "Videos", "NVIDIA")

# Define file types for pictures and videos
PICTURE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')
VIDEO_EXTENSIONS = ('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv')

def get_subfolders(folder):
    subfolders = []
    if os.path.exists(folder):
        for root, dirs, _ in os.walk(folder):
            for dir_name in dirs:
                subfolders.append(os.path.join(root, dir_name))  # Add full path of subfolders
    return subfolders

def clean_folder(folder_path, file_types):
    if os.path.exists(folder_path):
        deleted_files = 0
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path) and file.endswith(file_types):
                os.remove(file_path)
                deleted_files += 1
        if deleted_files > 0:
            return f"Clean completed in {folder_path}. {deleted_files} files deleted."
        else:
            return f"Clean failed in {folder_path}. No matching files found."
    else:
        return f"Folder {folder_path} does not exist."

def clean_pictures():
    result = ""
    nvidia_folders = get_subfolders(user_videos_path)
    for folder in nvidia_folders:
        result += clean_folder(folder, PICTURE_EXTENSIONS) + "\n"
    return result

def clean_videos():
    result = ""
    nvidia_folders = get_subfolders(user_videos_path)
    for folder in nvidia_folders:
        result += clean_folder(folder, VIDEO_EXTENSIONS) + "\n"
    return result

def clean_both():
    result = ""
    nvidia_folders = get_subfolders(user_videos_path)
    for folder in nvidia_folders:
        result += clean_folder(folder, PICTURE_EXTENSIONS) + "\n"
        result += clean_folder(folder, VIDEO_EXTENSIONS) + "\n"
    return result

def show_result(result):
    messagebox.showinfo("Clean Operation Complete", result)

def on_clean_pictures():
    result = clean_pictures()
    show_result(result)

def on_clean_videos():
    result = clean_videos()
    show_result(result)

def on_clean_both():
    result = clean_both()
    show_result(result)

def count_files():
    picture_count = 0
    video_count = 0
    nvidia_folders = get_subfolders(user_videos_path)
    for folder in nvidia_folders:
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                if file.endswith(PICTURE_EXTENSIONS):
                    picture_count += 1
                elif file.endswith(VIDEO_EXTENSIONS):
                    video_count += 1
    messagebox.showinfo("File Count", f"Total Pictures: {picture_count}\nTotal Videos: {video_count}")

def create_gui():
    window = tk.Tk()
    window.title("NHC")
    window.geometry("300x440")  # Adjusted width for a better look
    window.configure(bg="#2e2e2e")  # Dark background color

    # Title Label
    title_label = tk.Label(window, text="Welcome to the", font=("Arial", 18, "bold"), fg="#ffffff", bg="#2e2e2e")
    title_label.pack(pady=10)

    # Instructions Label
    instructions_label = tk.Label(window, text="Nvidia Highlights Cleaner", font=("Arial", 12), fg="#a1a1a1", bg="#2e2e2e")
    instructions_label.pack(pady=5)

    # Button Style
    button_style = {
        "bg": "#444444",  # Dark gray background
        "fg": "#ffffff",  # White text
        "font": ("Arial", 12, "bold"),
        "relief": "flat",
        "width": 25,
        "height": 2,
        "activebackground": "#666666",  # Slightly lighter gray for active state
        "activeforeground": "#ffffff"  # White text on hover
    }

    # Buttons
    clean_pictures_button = tk.Button(window, text="Clean Only Pictures", command=on_clean_pictures, **button_style)
    clean_pictures_button.pack(pady=10)

    clean_videos_button = tk.Button(window, text="Clean Only Videos", command=on_clean_videos, **button_style)
    clean_videos_button.pack(pady=10)

    clean_both_button = tk.Button(window, text="Clean Both", command=on_clean_both, **button_style)
    clean_both_button.pack(pady=10)

    count_files_button = tk.Button(window, text="Count Pictures & Videos", command=count_files, **button_style)
    count_files_button.pack(pady=10)

    exit_button = tk.Button(window, text="Exit", command=window.quit, **button_style)
    exit_button.pack(pady=10)

    window.mainloop()

create_gui()
