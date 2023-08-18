# Polytasks: a polybar TaskManager for multiple monitors*.
<sub> *(also works for single monitor).</sub>

inpired by the work of [uniquepointer](https://github.com/uniquepointer) on his [polywins](https://github.com/uniquepointer/polywins) script written in bash.

## Requirements
##### Packages
| Package | How to install (Fedora) | How to install (Ubuntu) | 
| --- | --- | --- |
| pip | sudo dnf install python3-pip | sudo apt install python3-pip |
| xprop | sudo dnf install xprop | I'll check and update here since I don't user ubuntu |

##### Python Libraries

| Library | How to install |
| --- | --- |
| gi | pip install PyGObject |
| ewmh | pip install ewmh |
| pyxdg | p install pyxdg |


## Configuration

polytasks requires a configuration file called polytasks_config.py in the same folder as the polytasks.py script.

| Setting | Description |
| --- | --- |
| `use_styling = True` | Set False to disable window name styling. |
| `use_active_underline = True` |  Set to False to disable underlining the active window name. |
| `use_inactive_underline = False` | Set to True to enable underlining inactive window names. |
| `add_icon = True` | If True prepends a nerd fonts icon char to the front of the window names if icon provided on icon_list (see icon_list for more information) |
| `max_windows = 10` | Maximum number of window names to display |
| `char_limit = 20` | Maximum number of characters to display per window name |
| `separator = "."` | Separator between window names |
| `name_option = "application_name"` | Default: Choose from "window_title", "window_class", "application_name". see name options table bellow for more information |
| `forbidden_classes = ["polybar"]` | List of forbidden classes, add the classes of windows to be ignored by the script.
| `text_case_option = "normal"` | Default: Choose from "normal", "uppercase", "lowercase", "capitalized". see text case options table for more information. |

| Styling variables | Description |
| --- | --- |
| `active_text_color = "#88c0d0"` | Active window name foregound color. |
| `active_bg = "#282a36"` | Active window name background color. |
| `active_underline = "#88c0d0"` | Active window name underline color |
| `inactive_text_color = "#44475a"` | Inactive window name foreground color. |
| `inactive_bg = "#282a36"` | Inactive window name background color. |
| `inactive_underline = "#44475a"` | Inactive windows name underline color. |

| Name options | Description | 
| --- | --- | 
| window_title | Display current window title. | 
| window_class | Display the windows class. | 
| application_name | Display application name, tries to get the application name from its *.desktop file if can't find displays the window class. |

| Text case options | Description | 
| --- | --- | 
| normal | Display all windows name as it comes from the system. | 
| uppercase | Display all windows name in uppercase. | 
| lowercase | Display all windows name in lowercase. | 
| capitalized | Display all windows name capitalized, only the first letter of the window name with multiple words will be capitalized. |

## Installing

* Save `polytasks.py`, for example to `~/.config/polybar/scripts`
* Save `polytasks_config.py` to the same folder as `polytaks.py`
* Make the script and config executable with `chmod +x ~/.config/polybar/scripts/polytasks*`
* Change any setting you wish from polytasks_config.py

## Configuring Polybar (single monitor)

* Open terminal and type `xprop -spy' and press enter, it will ask you to target any open window, once a window is target it will display information on your terminal. look for _NET_WM_DESKTOP(CARDINAL), this will be your $Desktop_ID
* Add the following module to your polybar config replacing the $Desktop_ID with your own:

```ini
[module/polytasks]
type = custom/script
exec = ~/.config/polybar/scripts/polywins.sh $Desktop_ID 2>/dev/null
format = <label>
label = %output%
label-padding = 1
tail = true
```
* Add the module to one of your bars, and don't forget to set a line-size if you intend to use underline, for example like so:
```ini
[bar/your_bar_name]
modules-center = polytasks
line-size = 2
```
