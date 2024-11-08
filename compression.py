import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def compress_image(image_path, output_path, quality, include_jpg):
    try:
        with Image.open(image_path) as img:
            if img.format in ['JPEG', 'JPG'] and not include_jpg:
                img.save(output_path, optimize=True, quality=100)
                print(f"Copied {image_path} without compression as {output_path}")
            else:
                img.convert('RGB').save(output_path, format='JPEG', optimize=True, quality=quality)
                print(f"Compressed {image_path} and saved as {output_path} with quality={quality}")
    except Exception as e:
        print(f"Error compressing {image_path}: {e}")

def compress_images_in_directory(directory, output_directory, quality, include_jpg):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png', 'gif')):
                image_path = os.path.join(root, file)
                output_path = os.path.join(output_directory, os.path.relpath(image_path, directory))
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                compress_image(image_path, output_path, quality, include_jpg)

def select_input_directory():
    folder_path = filedialog.askdirectory()
    input_dir_var.set(folder_path)

def select_output_directory():
    folder_path = filedialog.askdirectory()
    output_dir_var.set(folder_path)

def start_compression():
    input_dir = input_dir_var.get()
    output_dir = output_dir_var.get()
    quality = int(quality_var.get())
    include_jpg = include_jpg_var.get()

    if not input_dir or not output_dir:
        messagebox.showerror("Error", "Please select both input and output directories.")
        return

    compress_images_in_directory(input_dir, output_dir, quality, include_jpg)
    messagebox.showinfo("Success", "Images compressed successfully.")

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Image Compressor")
root.geometry("400x400")
root.configure(bg="#f0f0f5")

input_dir_var = tk.StringVar()
output_dir_var = tk.StringVar()
quality_var = tk.StringVar(value="85")
include_jpg_var = tk.BooleanVar(value=False)

# Styling configurations
label_font = ("Helvetica", 10, "bold")
entry_font = ("Helvetica", 10)
button_font = ("Helvetica", 10, "bold")
button_style = {"bg": "#4CAF50", "fg": "white", "font": button_font, "bd": 0, "highlightthickness": 0}

# Configure grid layout weights for responsiveness
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Input Directory
tk.Label(root, text="Select Input Directory:", font=label_font, bg="#f0f0f5").grid(row=0, column=0, sticky="w", padx=20, pady=(20, 5), columnspan=2)
tk.Entry(root, textvariable=input_dir_var, font=entry_font).grid(row=1, column=0, sticky="ew", padx=20, columnspan=1)
tk.Button(root, text="Browse", command=select_input_directory, **button_style).grid(row=1, column=1, padx=20, pady=5, sticky="ew")

# Output Directory
tk.Label(root, text="Select Output Directory:", font=label_font, bg="#f0f0f5").grid(row=2, column=0, sticky="w", padx=20, pady=(20, 5), columnspan=2)
tk.Entry(root, textvariable=output_dir_var, font=entry_font).grid(row=3, column=0, sticky="ew", padx=20, columnspan=1)
tk.Button(root, text="Browse", command=select_output_directory, **button_style).grid(row=3, column=1, padx=20, pady=5, sticky="ew")

# Compression Quality
tk.Label(root, text="Compression Quality (1-100):", font=label_font, bg="#f0f0f5").grid(row=4, column=0, sticky="w", padx=20, pady=(20, 5), columnspan=2)
tk.Entry(root, textvariable=quality_var, font=entry_font, width=10).grid(row=5, column=0, sticky="w", padx=20, columnspan=2)

# Include JPEG Checkbox
tk.Checkbutton(root, text="Include JPEG Files in Compression", variable=include_jpg_var, bg="#f0f0f5", font=label_font).grid(row=6, column=0, columnspan=2, pady=5)

# Start Compression Button
start_button = tk.Button(root, text="Start Compression", command=start_compression, **button_style)
start_button.grid(row=7, column=0, columnspan=2, pady=20, padx=20, sticky="ew")

root.mainloop()
