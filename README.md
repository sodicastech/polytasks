# Polytasks: a polybar TaskManager for multiple monitors*.
<sub> *(also works for single monitor).</sub>

inpired by the work of [uniquepointer](https://github.com/uniquepointer) on his [polywins](https://github.com/uniquepointer/polywins) script written in bash.

## Requirements
| Library | How to install |
| --- | --- |
| gi | pip install PyGObject |
| ewmh | pip install ewmh |
| pyxdg | p install pyxdg |


## Configuration

polytasks requires a configuration file called polytasks_config.py in the same folder as the polytasks.py script.

| Setting | Description |
| --- | --- |
| `use_styling = True` | Set False to disable window name styling |
| `use_active_underline = True` |  Set to False to disable underlining the active window name. |
| `use_inactive_underline = False` | Set to True to enable underlining inactive window names. |
| `add_icon = True` | If True prepends a nerd fonts icon char to the front of the window names if icon provided on icon_list (see icon_list for more information) |
| `max_windows = 10` | Maximum number of window names to display |
| `char_limit = 20` | Maximum number of characters to display per window name |
| `separator = "."` | Separator between window names |
| `name_option = "application_name"` | Default: Choose from "window_title", "window_class", "application_name". see name options table bellow for more information |
| `forbidden_classes = ["polybar"]` | List of forbidden classes, add the classes of windows to be ignored by the script.
| `text_case_option = "normal"` | Default: Choose from "normal", "uppercase", "lowercase", "capitalized". see text case options table for more information. |

| Name Options | Description | 
| --- | --- | 
| `window_title` | Display current window title. | 
| `window_class` | Display the windows class. | 
| `application_name` | Display application name, tries to get the application name from its *.desktop file if can't find displays the window class. |
