# Welcome to PyQt5 Custom Widgets Documentation
You can check out `showcase.py` in the [Examples](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/) to see a clear demonstration of all widgets. \
Here is the list of currently implemented widgets
- [ToggleSwitch](#ToggleSwitch)
- [StyledButton](#StyledButton)
- [ImageBox](#ImageBox)
- [ColorPicker](#ColorPicker)
- [DragDropFile](#DragDropFile)



## ToggleSwitch
`ToggleSwitch` is simply a modern looking checkbox. It has 3 styles named win10, ios and android. \
\
![ToggleSwitch](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/toggleswitch.gif)

#### Parameters
- `text` (str) : Text that is shown next to the switch
- `style` (str) : Style of the widget. "win10", "ios" or "android"
- `on` (bool) : Whether the switch is toggled or not

#### Methods
- `isToggled()` (bool) : Returns switch's state

#### Signals
- `toggled` : This signal is emitted when switch's state gets changed



## StyledButton
`StyledButton` is an animated push button. It has two styles named flat and hyper. \
\
![StyledButton](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/styledbutton.gif)

#### Parameters
- `text` (str) : Text that is shown inside the button
- `style` (str) : Style of the widget. "flat" or "hyper"
- `icon` (str) : Filepath for the icon. This parameter is optional
- `fixedBottom` (bool) : Is hyper styled button's bottom fixed or not. This parameter is optional

#### Methods
- `setIcon(filepath)` : Changes button's icon
- `setDropShadow(bool)` : Enables or disables button's drop shadow effect



## ImageBox
`ImageBox` is a container for images or animated GIFs \
\
![ImageBox](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/imagebox.png)

#### Parameters
- `source` (str) : Filepath or URL of the source image/gif
- `keepAspectRatio` (bool) : Protect aspect ratio. This parameter is optional
- `smoothScale` (bool) : Transform the image smoothly. This parameter is optional



## ColorPicker
`ColorPicker` is not completed yet
\
![ColorPicker](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/colorpicker.png)



## DragDropFile
`DragDropFile` is an area to let user simply drop files onto it instead of browsing it on file dialog \
\
![DragDropFile](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/dropfileshowcase.gif)

#### Signals
- `fileDropped` : This signal is emitted when a file is dropped on widget
