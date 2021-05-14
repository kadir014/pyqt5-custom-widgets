# Welcome to PyQt5 Custom Widgets Documentation
You can check out `showcase.py` in the [Examples](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/) to see a clear demonstration of all widgets. \
Here is the list of currently implemented widgets
- [ToggleSwitch](#ToggleSwitch)
- [StyledButton](#StyledButton)
- [ImageBox](#ImageBox)
- [ColorPicker](#ColorPicker)
- [DragDropFile](#DragDropFile)
- [EmbedWindow](#DEmbedWindow)
- [CodeTextEdit](#CodeTextEdit)
- [TitleBar](#TitleBar)
- [Spinner](#Spinner)
- [Toast](#Toast)

## Other stuff
Other stuff that the the library provides but are not mainly widgets. Some are tools, data classes, etc...
- [RequestHandler](#RequestHandler)
- [FileDetails](#FileDetails)
- [Animation](#Animation)
- [AnimationHandler](#AnimationHandler)
- [ColorPreview](#ColorPreview)
- [SyntaxHighlighter](#SyntaxHighlighter)


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

#### Methods
- `setIcon(filepath)` : Changes button's icon


## ColorPicker
`ColorPicker` is not completed yet
\
![ColorPicker](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/colorpicker.png)



## DragDropFile
`DragDropFile` is an area to let user simply drop files onto it instead of browsing it on file dialog \
\
![DragDropFile](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/dropfileshowcase.gif)

#### Signals
- `fileDropped(file)` FileDetails : This signal is emitted when a file is dropped on widget

## EmbedWindow
`EmbedWindow` is a dialog window which is not a popup, it is embedded onto the parent widget \
\
![EmbedWindow](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/embedwindowshowcase.gif)

#### Parameters
- `parent` (QWidget) : Parent widget of the window

#### Attributes
- `content` (QLayout) : Window's layout where you can add your own widgets

#### Methods
- `setTitle(title)` : Change title of the window
- `setControlsVisible(bool)` : Change visibility of control buttons

## CodeTextEdit
`CodeTextEdit` is simply a code editor. It's a multiline text area with syntax highlighting, it only supports few languages for now. For details see [SyntaxHighlighter](#SyntaxHighlighter) \
\
![CodeTextEdit](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/codetextshowcase.gif)

#### Methods
- `setTheme(theme)` : Change syntax coloring theme
- `setLang(lang)` : Change language syntax
- `loadFile(filepath)` : Load file content into editor

## TitleBar
`TitleBar` lets the developer use a custom window title bar, this widget also provides window resizing controls (WIP) \
\
![TitleBar](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/data/titlebarshowcase.png)

#### Parameters
- `parent` (QWidget) : Parent widget of the window
- `title` (str) : Title of the window (Optional)

#### Attributes
- `close_btn` (StyledButton) : Close button
- `max_btn` (StyledButton) : Maximize button
- `min_btn` (StyledButton) : Minimize button

#### Methods
- `setTitle(title)` : Change title
- `title()` (str) : Get title


# Other stuff
Other stuff that the the library provides but are not mainly widgets. Some are tools, data classes, etc...

## RequestHandler
`RequestHandler` is a thread (QThread) that can be used to handle HTTP requests while avoiding blocking Qt's event loop. You can see [Examples](https://github.com/kadir014/pyqt5-custom-widgets/blob/main/examples/) to see usage of this class.

#### Methods
- `newRequest(method, url, headers, data)`
  - `method` (str) : Request method
  - `url` (str) : Address where request will be sent at
  - `headers` (dict) : Request headers
  - `data` (dict) : Request data

#### Signals
- `requestResponded` : Emitted when a requeest in the current pool gets responded. Response is a [requests.Response](https://docs.python-requests.org/en/latest/api/#requests.Response) object

## FileDetails
`FileDetails` object is a data class which is meant to be used by `DragDropFile` for `fileDropped` signal

#### Attributes
- `path` (str) : File's path
- `content` (str) : Content of the file
- `name` (str) : File's name
- `pureName` (str) : File's name without the extension
- `extension` (str) : File's extension

## Animation
`Animation` is just a static class holding easing animation functions. This class is most likely going to be deprecated when I rework animations.

## AnimationHandler
`AnimationHandler` animates widget's properties using `Animation` class's functions. This class is most likely going to be deprecated when I rework animations.

## ColorPreview
`ColorPreview` is a widget to display some color. It can bee seen used next to ColorPicker example. But this widget is most likely going to be deprecated

## SyntaxHighlighter
`SyntaxHighlighter` inherits `QSyntaxHighlighter`, it's only purpose is to serve `CodeTextEdit` widget. `pyqt5Custom` module currently supports only Python and C++ syntax highlighting.
