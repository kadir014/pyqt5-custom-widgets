# PyQt5 Custom Widgets <img src="https://seeklogo.com/images/Q/qt-logo-1631E0218A-seeklogo.com.png" alt="drawing" width="43"/>
<p>
  <img src="https://img.shields.io/badge/python-3.6%2B-green">
  <img src="https://img.shields.io/badge/license-GPL%203.0-blue.svg">
  <img src="https://img.shields.io/badge/version-1.0.1-orange">
</p>
More useful and stylish widgets for PyQt5 such as toggle switches, animated buttons, etc..
<br>
<img src="https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/showcase.gif" width="500">

## Table of Contents
- [Installing](#Installing)
- [Usage](#Usage)
- [Widgets](#Widgets)
- [Examples](#References)
- [Documentation](#References)
- [Styling Reference](#References)
- [Dependencies](#Dependencies)
- [TODO](#Todo)
- [License](#License)

## Installing
Install using PIP (it might be `pip3` or `python3` depending on your platform)
```
pip install pyqt5Custom
```
or
```
python -m pip install pyqt5Custom
```
Also you can also use PySide2 instead of PyQt5 with just litte changes.

## Usage
Just import `pyqt5Custom` and you're ready to go. You can check out [Examples](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/), one little example for StyledButton widget:
```py
from pyqt5Custom import StyledButton

...

btn = StyledButton(text="Hello!")
btn.setStyleDict({
    "border-radius" : 20,
    "font-family" : "Helvetica",
    "font-size" : 17
  })

@btn.clicked.connect
def slot():
  print("Quitting!")
  app.exit()

layout.addWidget(btn)

...
```

## Widgets
| ![ToggleSwitch](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/toggleswitch.gif) <br> ToggleSwitch <br> [Documentation](documentation.md) | ![StyledButton](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/styledbutton.gif) <br> StyledButton <br> [Documentation](documentation.md) |
| :---: | :---: |
| ![ImageBox](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/imagebox.png) <br> **ImageBox** <br> [Documentation](documentation.md) | ![ColorPicker](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/colorpicker.png) <br> **ColorPicker** <br> [Documentation](documentation.md) |
| ![DragDropFile](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/dropfileshowcase.gif) <br> **DragDropFile** <br> [Documentation](documentation.md) | ![EmbedWindow](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/embedwindowshowcase.gif) <br> **EmbedWindow** <br> [Documentation](documentation.md) |
| ![CodeTextEdit](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/codetextshowcase.gif) <br> **CodeTextEdit** <br> [Documentation](documentation.md) | ![TitleBar](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/titlebarshowcase.gif) <br> **TitleBar** <br> [Documentation](documentation.md) |
| ![Spinner](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/spinnershowcase.gif) <br> **Spinner** <br> [Documentation](documentation.md) | ![Toast](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/toastshowcase.gif) <br> **Toast** <br> [Documentation](documentation.md) |

## References
- See [Examples](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/) page for examples
- See [Documentation](documentation.md) page for documentation and detailed widget references
- See [styling reference](stylingref.md) page for styling instructions on custom widget

## Dependencies
 - [PyQt5](https://pypi.org/project/PyQt5/)
 - [requests](https://pypi.org/project/requests/)

## TODO
  - [ ] Better styling and QSS support
  - [ ] Rework animations using [Qt's animation framework](https://doc.qt.io/qtforpython/overviews/animation-overview.html)
  - [ ] Optimize and complete ColorPicker widget

## License
[GPL v3](LICENSE) © Kadir Aksoy
