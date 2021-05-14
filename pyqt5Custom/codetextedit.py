#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #


from PyQt5.QtCore    import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPlainTextEdit
from PyQt5.QtGui     import QColor, QPainter, QPen, QBrush

from .syntaxhighlighter import SyntaxHighlighter



class CodeTextEdit(QWidget):

    LANG_DISPLAY = {
            "plain"  : "Plain text",
            "python" : "Python",
            "py"     : "Python",
            "cpp"    : "C++",
            "c++"    : "C++"
        }

    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.layout.addSpacing(37)

        self.editorlyt = QVBoxLayout()
        self.editorlyt.setSpacing(0)
        self.editorlyt.setContentsMargins(0, 0, 0, 0)
        self.layout.addLayout(self.editorlyt)

        self.editor = QPlainTextEdit()
        self.editor.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.editorlyt.addWidget(self.editor)

        self.setStyleSheet("QPlainTextEdit {font-family:Consolas; font-size:14px; color:#222222;}")

        self.highlighter = SyntaxHighlighter(self.editor.document())

        self.sliderVal = 0
        self.lastdigit = 2
        vs = self.editor.verticalScrollBar()

        @vs.rangeChanged.connect
        def slot(v):
            self.sliderVal = self.editor.verticalScrollBar().value()

            if len(str(vs.maximum()+15)) > self.lastdigit:
                self.lastdigit = len(str(vs.maximum()+15))
                self.layout.insertSpacing(0, 10)

            self.update()

        @vs.valueChanged.connect
        def slot(v):
            self.sliderVal = v

            self.update()

        self.statusbar = QWidget()
        self.statusbar.setFixedHeight(26)
        self.statusbarlyt = QHBoxLayout()
        self.statusbarlyt.setContentsMargins(10, 0, 30, 0)
        self.statusbar.setLayout(self.statusbarlyt)
        self.editorlyt.addWidget(self.statusbar)

        self.cursor_lbl = QLabel("0:0")
        self.cursor_lbl.setStyleSheet("font-size:16px;")
        self.statusbarlyt.addWidget(self.cursor_lbl, alignment=Qt.AlignLeft|Qt.AlignVCenter)

        self.lang_lbl = QLabel("Plain text")
        self.lang_lbl.setStyleSheet("font-size:16px;")
        self.statusbarlyt.addWidget(self.lang_lbl, alignment=Qt.AlignRight|Qt.AlignVCenter)

        @self.editor.cursorPositionChanged.connect
        def slot():
            self.cursor_lbl.setText(f"{self.editor.textCursor().blockNumber()}:{self.editor.textCursor().positionInBlock()}")

    def __repr__(self):
        return f"<pyqt5Custom.CodeTextEdit({CodeTextEdit.LANG_DISPLAY(self.lang)})>"

    def setTheme(self, theme):
        self.highlighter.setTheme(theme)
        self.highlighter.setRules()

        c = self.highlighter.theme["background"]
        rgb = f"rgb({c.red()}, {c.green()}, {c.blue()})"

        cc = self.highlighter.theme["identifier"]
        crgb = f"rgb({cc.red()}, {cc.green()}, {cc.blue()})"

        self.editor.setStyleSheet(f"QPlainTextEdit {{background-color: {rgb}; color: {crgb};}}")

        self.cursor_lbl.setStyleSheet(f"color: {crgb}; font-size:16px;")
        self.lang_lbl.setStyleSheet(f"color: {crgb}; font-size:16px;")

        self.highlighter.rehighlight()
        self.update()

    def setLang(self, lang):
        self.lang_lbl.setText(CodeTextEdit.LANG_DISPLAY[lang])

        self.highlighter.setLang(lang)
        self.highlighter.setRules()
        self.highlighter.rehighlight()
        self.update()

    def loadFile(self, filepath, encoding="utf-8"):

        if filepath.endswith(".py"): lang = "python"
        elif filepath.endswith(".cpp"): lang = "cpp"
        else: lang = "plain"

        with open(filepath, "r", encoding=encoding) as f:
            self.editor.setPlainText(f.read())

        self.setLang(lang)

    def paintEvent(self, event):
        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing)

        pt.setBrush(QBrush(self.highlighter.theme["lines-background"]))

        pt.drawRect(0, 0, self.width(), self.height())

        font = self.editor.font()
        pt.setFont(font)

        gap = font.pixelSize() + 3

        for i in range((self.height()//gap)):
            font = pt.font()
            pt.setFont(font)
            pt.setPen(QPen(self.highlighter.theme["lines"]))

            pt.drawText(13, i*gap, str(i+self.sliderVal))

        pt.setBrush(QBrush(self.highlighter.theme["background"]))
        pt.setPen(QPen(QColor(0, 0, 0, 0)))
        pt.drawRect(3, self.height()-self.statusbar.height(), 40, self.statusbar.height()-6)

        pt.end()
