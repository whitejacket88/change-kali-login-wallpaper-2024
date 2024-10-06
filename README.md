# login-wallpaper-changer


  			 Login Wallpaper Changer - README

This Python script provides a graphical interface (GUI) to change the login screen wallpaper on a Kali Linux system 2024. It allows you to select an image from your computer, replaces the current login screen wallpaper with the selected image, and creates a backup of the original wallpaper for easy restoration.


1. FEATURES

- **Change Login Wallpaper**: Select a custom image to use as the login screen background.
- **Backup and Restore**: Automatically backs up the current login wallpaper and provides an option to restore it.
- **Undo Changes**: Reverts the login wallpaper to the previously backed-up version.
- **User-friendly GUI**: Simple graphical interface with buttons for easy operation.

2. REQUIREMENTS

- **Python 3.x**: Ensure that you have Python 3 installed.
- **tkinter**: This script uses the `tkinter` library to create the GUI. Most Linux distributions include `tkinter` with Python, but you can install it with the following command if needed:
└─# sudo apt-get install python3-tk


3. HOW TO USE

Follow these steps to use the Login Wallpaper Changer script:

 1. **Run the Script**:
- Run the script with Python 3. You may need to provide executable permissions to the script, or you can run it directly:
└─# sudo chmod +x /path/to/change-login-wallpaper.py
└─# python3 change-login-wallpaper.py

 2. **Select a Wallpaper**:
- Click on the "Select Wallpaper Image" button.
- A file dialog will open, starting in your **home directory**. From here, you can browse and select an image file. The supported formats are PNG, JPG, and JPEG.
- Note: Hidden directories will be shown in the file selection dialog, just ignore them.

 3. **Provide Sudo Password**:
- After selecting an image, the script will prompt you to enter your `sudo` password. This is required because modifying the login screen background requires root privileges.

 4. **Undo Changes**:
- If you wish to revert to the original login wallpaper, click on the "Undo Wallpaper Change" button. The script will restore the backed-up wallpaper files.

 5. **About**:
- The "Help" menu contains an "About" option, which shows information about the script's version and author only not really helpfull I know.

4. IMPORTANT DIRECTORIES TO REMEMBER !!!!!

The script modifies the following directory:

/usr/share/backgrounds/kali/

Here, the script manages the following files:
- **login**: The active login wallpaper.
- **login-blurred**: The blurred version of the login wallpaper.
- **login-backup**: The backup of the original login wallpaper.
- **login-blurred-backup**: The backup of the original blurred wallpaper.


5. DISCLAIMER

This script modifies system files that require root privileges. Please proceed with caution. By using this script, you agree to the following terms:

- **Backup Your Data**: The author is not responsible for any damage or data loss that may occur from the use of this script. Ensure that you back up important files before using this tool.
- **For Educational Purposes**: This tool is provided for educational purposes and is intended to automate the login wallpaper changing process in a secure and responsible manner.
- **Use at Your Own Risk**: The author of this script assumes no liability for any issues that arise from its use, including but not limited to system crashes or boot failures.


6. AUTHOR

- **Version**: 1.0
- **Author** 
- **whitejacket88-tom white**
- **10/05/24**
