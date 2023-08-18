#!/usr/bin/env python3

import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck
import sys
import os
import xdg.DesktopEntry
from ewmh import EWMH
import glob

# Import variables from polytasks_config.py
from polytasks_config import *

def get_icon_for_window(window):
    global name_option
    window_class = None
    
    if name_option == "window_title":
        window_class = window.get_class_group_name().lower()
    elif name_option == "window_class":
        window_class = window.get_class_group_name().lower()
    elif name_option == "application_name":
        pid = window.get_application().get_pid()
        desktop_file = find_desktop_file_by_exec(get_executable_name_from_pid(pid))
        if desktop_file:
            app_name = xdg.DesktopEntry.DesktopEntry(desktop_file).getName()
            window_class = app_name.lower()
        else:
            window_class = window.get_class_group_name().lower()

    #print(window_class) # Uncomment this line to findout the class of the window you want to add to the icon_list dictionary

    if window_class is None:
        return None
    
    if window_class in icon_list:
        return icon_list[window_class]

def find_desktop_file_by_exec(executable_name):
    desktop_files = glob.glob("/usr/share/applications/*.desktop")
    
    for desktop_file in desktop_files:
        try:
            with open(desktop_file, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith("Exec="):
                        exec_command = line.strip()[len("Exec="):].split()[0]
                        if os.path.basename(exec_command) == executable_name:
                            return desktop_file
        except:
            pass
    
    return None

def get_executable_name_from_pid(pid):
    try:
        exe_path = os.readlink(f"/proc/{pid}/exe")
        executable_name = os.path.basename(exe_path)
        return executable_name
    except Exception as e:
        #0print(f"Error: {e}")
        return None

def get_window_name(window):
    global name_option, text_case_option
    if name_option == "window_title":
        window_name = window.get_name()
    elif name_option == "window_class":
        window_name = window.get_class_instance_name()
    elif name_option == "application_name":
        pid = window.get_pid()
        desktop_file = find_desktop_file_by_exec(get_executable_name_from_pid(pid))
        if desktop_file:
            app_name = xdg.DesktopEntry.DesktopEntry(desktop_file).getName()
            window_name = app_name
        else:
            window_name = window.get_application().get_name()

    # Apply text case transformation
    if text_case_option == "uppercase":
        window_name = window_name.upper()
    elif text_case_option == "lowercase":
        window_name = window_name.lower()
    elif text_case_option == "capitalized":
        window_name = window_name.capitalize()
        
    # Add icon if enabled
    if add_icon:
        icon = get_icon_for_window(window)
        if icon:
            window_name = f"{icon} {window_name}"
            
    return window_name
    
def generate_window_list(monitor_id):
    global char_limit, name_option, separator, forbidden_classes, use_styling, max_windows

    # Create Wnck Screen instance
    screen = Wnck.Screen.get_default()
    screen.force_update()

    # Create a list to store formatted window names
    formatted_window_names = []

    # Loop through windows and add their formatted names to the list
    window_count = 0
    for window in screen.get_windows():
        desktop_name = str(window.get_workspace().get_number())
        if desktop_name == monitor_id:
            window_class = window.get_class_group_name()
            
            # Check if the window class is not in the list of forbidden classes
            if window_class.lower() not in [cls.lower() for cls in forbidden_classes]:
                window_name = get_window_name(window)
                if window_name is not None:
                    window_name = window_name[:char_limit]  # Truncate to char_limit characters
                    
                    if use_styling:
                        if window.is_active():
                            if use_active_underline:
                                window_name = f"%{{F{active_text_color}}}%{{B{active_bg}}}%{{U{active_underline}}}%{{+u}}{window_name}%{{-u}}%{{U-}}%{{B-}}%{{F-}}"

                            else:
                                window_name = f"%{{F{active_text_color}}}%{{B{active_bg}}}{window_name}%{{B-}}%{{F-}}"
                        else:
                            if use_inactive_underline:
                                window_name = f"%{{F{inactive_text_color}}}%{{B{inactive_bg}}}%{{U{inactive_underline}}}%{{+u}}{window_name}%{{-u}}%{{U-}}%{{B-}}%{{F-}}"
                            else:
                                window_name = f"%{{F{inactive_text_color}}}%{{B{inactive_bg}}}{window_name}%{{B-}}%{{F-}}"
                            
                    if window_count < max_windows:
                        formatted_window_names.append(window_name)
                    window_count += 1

    # Add a blank space to each side of the separator
    formatted_separator = f" {separator} "

    # Join the formatted window names with the separator
    window_string = formatted_separator.join(formatted_window_names)

    return window_string

if __name__ == "__main__":

    if len(sys.argv) > 1:
        monitor_id = sys.argv[1]

    window_string = generate_window_list(monitor_id)

    print(window_string)
