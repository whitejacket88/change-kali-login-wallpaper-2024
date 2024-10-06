import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk

# Directory and file paths
login_wallpaper_dir = "/usr/share/backgrounds/kali/"
login_file = os.path.join(login_wallpaper_dir, "login")
login_blurred_file = os.path.join(login_wallpaper_dir, "login-blurred")
login_backup_file = os.path.join(login_wallpaper_dir, "login-backup")
login_blurred_backup_file = os.path.join(login_wallpaper_dir, "login-blurred-backup")

def prompt_for_sudo_password():
    """Prompt the user for the sudo password."""
    password = simpledialog.askstring("Sudo Password", "Enter your sudo password:", show='*')
    return password

def change_wallpaper(image_path, sudo_password):
    """Automate the process of changing login screen wallpaper."""
    try:
        # Backup existing files
        if os.path.exists(login_file):
            subprocess.run(["sudo", "-S", "mv", login_file, login_backup_file], input=sudo_password.encode(), check=True)
        if os.path.exists(login_blurred_file):
            subprocess.run(["sudo", "-S", "mv", login_blurred_file, login_blurred_backup_file], input=sudo_password.encode(), check=True)
        
        # Copy the selected image as login and login-blurred
        subprocess.run(["sudo", "-S", "cp", image_path, login_file], input=sudo_password.encode(), check=True)
        subprocess.run(["sudo", "-S", "cp", image_path, login_blurred_file], input=sudo_password.encode(), check=True)
        
        messagebox.showinfo("Success", "Login screen wallpaper updated successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred while updating the wallpaper: {e}")

def undo_changes(sudo_password):
    """Revert login wallpaper changes by restoring backup files."""
    try:
        if os.path.exists(login_backup_file):
            subprocess.run(["sudo", "-S", "mv", login_backup_file, login_file], input=sudo_password.encode(), check=True)
        if os.path.exists(login_blurred_backup_file):
            subprocess.run(["sudo", "-S", "mv", login_blurred_backup_file, login_blurred_file], input=sudo_password.encode(), check=True)
        messagebox.showinfo("Success", "Login screen wallpaper reverted to the backup successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred while reverting the wallpaper: {e}")

def select_image():
    """Open a file dialog to select an image starting from the current user's home directory."""
    # Get the current user's home directory (not root)
    home_dir = os.path.expanduser("~")
    
    # Open file dialog starting at the user's home directory
    image_path = filedialog.askopenfilename(
        title="Select Wallpaper Image", 
        initialdir=home_dir,  # Open in user's home directory
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    if image_path:
        # Ask for the sudo password
        sudo_password = prompt_for_sudo_password()
        if sudo_password:
            # Proceed to change the wallpaper
            change_wallpaper(image_path, sudo_password)
        else:
            messagebox.showwarning("Cancelled", "Sudo password is required to proceed.")

def undo_wallpaper_change():
    """Prompt for sudo password and undo the wallpaper change."""
    sudo_password = prompt_for_sudo_password()
    if sudo_password:
        undo_changes(sudo_password)
    else:
        messagebox.showwarning("Cancelled", "Sudo password is required to proceed.")

def show_about():
    """Display an About dialog box."""
    messagebox.showinfo("About", "Login Wallpaper Changer\nVersion 1.0\nAuthor: Tom White")

# Setup the GUI
root = tk.Tk()
root.title("Login Wallpaper Changer")
root.geometry("400x250")

# Add a menu bar with "About" option
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

about_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=about_menu)
about_menu.add_command(label="About", command=show_about)

# Title Label
title_label = ttk.Label(root, text="Login Screen Wallpaper Changer", font=("Helvetica", 16))
title_label.pack(pady=10)

# Instruction Label
instruction_label = ttk.Label(root, text="Select an image to update the login screen wallpaper:", font=("Helvetica", 10))
instruction_label.pack(pady=5)

# Create a frame for the buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=20)

# Button to select image
select_button = ttk.Button(button_frame, text="Select Wallpaper Image", command=select_image)
select_button.grid(row=0, column=0, padx=10)

# Button to undo changes
undo_button = ttk.Button(button_frame, text="Undo Wallpaper Change", command=undo_wallpaper_change)
undo_button.grid(row=0, column=1, padx=10)

# Start the GUI event loop
root.mainloop()
