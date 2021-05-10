# PyQt5 Custom Widgets <img src="https://seeklogo.com/images/Q/qt-logo-1631E0218A-seeklogo.com.png" alt="drawing" width="43"/>
<p>
  <img src="https://img.shields.io/badge/python-3.6%2B-green">
  <img src="https://img.shields.io/badge/license-GPL%203.0-blue.svg">
  <img src="https://img.shields.io/badge/version-0.0.4-orange">
</p>
More useful and stylish widgets for PyQt5 such as toggle switches, animated buttons, etc.. \
\
![showcase](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/showcase.gif) \
\
**DISCLAIMER:** \
Currently most widgets can't use style sheets properly so you have to use attributes to stylize them. I'm planning to remove this inconvenience and make their usage as close as to base Qt widgets in the next update.

## Table of Contents
- [Installing](#Installing)
- [Usage](#Usage)
- [Widgets](#Widgets)
- [Examples](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/)
- [Documentation](documentation.md)
- [Dependencies](#Dependencies)
- [TODO](#Todo)
- [License](#License)

## Installing
The module (version 0.0.4) is not on PyPi yet, so you have to manually download `pyqt5Custom` folder. Version 0.0.5 will be on PyPi. \
You can also use PySide2 instead of PyQt5 with just litte changes.

## Usage
Just import `pyqt5Custom` and you're ready to go. You can check out [Examples](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/), one little example for ToggleSwitch widget:
```py
from pyqt5Custom import ToggleSwitch

...

togglesw = ToggleSwitch("Turn on/off the lights", style="ios")
togglesw.setStyleSheet("font-size:15px; color: #444444;")
layout.addWidget(togglesw)

...
```

## Widgets
| ![ToggleSwitch](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/toggleswitch.gif) <br> ToggleSwitch <br> [Documentation](documentation.md) | ![StyledButton](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/styledbutton.gif) <br> StyledButton <br> [Documentation](documentation.md) |
| :---: | :---: |
| ![ImageBox](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/imagebox.png) <br> **ImageBox** <br> [Documentation](documentation.md) | ![ColorPicker](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/colorpicker.png) <br> **ColorPicker** <br> [Documentation](documentation.md) |
| ![DragDropFile](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/dropfileshowcase.gif) <br> **DragDropFile** <br> [Documentation](documentation.md) | ![EmbedWindow](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/embedwindowshowcase.gif) <br> **EmbedWindow** <br> [Documentation](documentation.md) |
| ![CodeTextEdit](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/codetextshowcase.gif) <br> **CodeTextEdit** <br> [Documentation](documentation.md) | ![TitleBar](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/titlebarshowcase.png) <br> **TitleBar** <br> [Documentation](documentation.md) |


## Dependencies
 - [PyQt5](https://pypi.org/project/PyQt5/)
 - [requests](https://pypi.org/project/requests/)

## TODO
  - [ ] Better styling and QSS support
  - [ ] Rework animations using [Qt's animation framework](https://doc.qt.io/qtforpython/overviews/animation-overview.html)
  - [ ] Optimize and complete ColorPicker widget

## License
[GPL v3](LICENSE) © Kadir Aksoy
