# Polytasks: a polybar TaskManager

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
| `use_styling = True` | Set to False to disable styling |
| `use_active_underline = True` | Set to False to disable styling |
| `use_inactive_underline = True` | Set to False to disable styling |
| `add_icon = True` | Set to True to add icons to window names |
| `max_windows = 10` | Maximum number of windows to display |
| `char_limit = 20` | Maximum number of characters to display |
| `separator = "."` | Separator between window names |
| `name_option = "application_name"` | Default: Choose from "window_title", "window_class", "application_name" |
| `forbidden_classes = ["polybar"]` | List of forbidden classes
| `text_case_option = "normal"` | Default: Choose from "normal", "uppercase", "lowercase", "capitalized" |
