# PyQt5 Custom Widgets 🧱
More useful and stylish widgets for PyQt5 such as toggle switches, animated buttons, etc.. \
\
![showcase](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/showcase.gif) \
\
**DISCLAIMER:** \
Currently most widgets can't use style sheets properly so you have to use attributes to stylize them. I'm planning to remove this inconvenience and make their usage as close as to base Qt widgets in the next update.

## Usage
Just import `customwidgets.py` and you're ready to go. You can check out examples folder for examples. Here are the list of current widgets:
```py
from customwidgets import ToggleSwitch, StyledButton, ...

...

togglesw = ToggleSwitch("Toggle lights", style="ios")
togglesw.setStyleSheet("font-size:15px; color: #444444;")
layout.addWidget(togglesw)

...
```

## Widgets
| ![ToggleSwitch](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/toggleswitch.gif) <br> ToggleSwitch <br> [Documentation](documentation.md) | ![StyledButton](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/styledbutton.gif) <br> StyledButton <br> [Documentation](documentation.md) |
| :---: | :---: |
| ![ImageBox](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/imagebox.png) <br> **ImageBox** <br> [Documentation](documentation.md) | ![ColorPicker](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/colorpicker.png) <br> **ColorPicker** <br> [Documentation](documentation.md) |
| ![DragDropFile](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/dropfileshowcase.gif) <br> **DragDropFile** <br> [Documentation](documentation.md) | |

## Todo
 - [ ] Make styling options more suitable for Qt
 - [ ] QSS support
 - [ ] Rework animations using [Qt's animation framework](https://doc.qt.io/qtforpython/overviews/animation-overview.html)
 - [ ] Optimize and complete color picker widget

 ## License
 [GPL v3](LICENSE) © Kadir Aksoy
