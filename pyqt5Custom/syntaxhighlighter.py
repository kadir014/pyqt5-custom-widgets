#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #
#                                                     #
#  DISCLAIMER: This class uses the JSON files in the  #
#              syntax and themes folders which has    #
#              pre-defined syntax rules and themes.   #
#              Don't forget to include them in your   #
#              package's folder if you're installing  #
#              this project manually.                 #


import json
import pathlib

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter



class SyntaxHighlighter(QSyntaxHighlighter):

    AVAILABLE_LANGS = {
            "plain"  : "plain",
            "py"     : "python",
            "python" : "python",
            "cpp"    : "cpp",
            "c++"    : "cpp"
        }

    def __init__(self, document, lang="python", theme="default"):
        super().__init__(document)

        self.setLang(lang)
        self.setTheme(theme)
        self.setRules()

    def formatThemeKey(self, color, style="", returnColor=False):
        _color = QColor()
        if type(color) is not str:
            _color.setRgb(color[0], color[1], color[2])

        elif color.startswith("#"):
            hexc = color.lstrip('#')
            hexc = tuple(int(hexc[i:i+2], 16) for i in (0, 2, 4))
            _color.setRgb(*hexc)

        else:
            _color.setNamedColor(color)

        if returnColor: return _color

        _format = QTextCharFormat()
        _format.setForeground(_color)
        if "bold"   in style: _format.setFontWeight(QFont.Bold)
        if "italic" in style: _format.setFontItalic(True)

        return _format

    def setTheme(self, theme):
        if isinstance(theme, dict):
            pass

        else:
            path = pathlib.Path(__file__).parents[0] / "themes" / f"{theme}.json"
            with open(path, "r", encoding="utf-8") as f:
                s = json.loads(f.read())

                self.theme = dict()

                for k in s:
                    p = s[k].split("-")
                    if len(p) == 2: self.theme[k] = self.formatThemeKey(s[k], p[1])
                    else: self.theme[k] = self.formatThemeKey(s[k])

                self.theme["background"] = self.formatThemeKey(s["background"], returnColor=True)
                self.theme["lines-background"] = self.formatThemeKey(s["lines-background"], returnColor=True)
                self.theme["lines"] = self.formatThemeKey(s["lines"], returnColor=True)
                self.theme["identifier"] = self.formatThemeKey(s["identifier"], returnColor=True)

    def setLang(self, lang):
        lang = lang.lower()

        if lang in SyntaxHighlighter.AVAILABLE_LANGS:
            self.lang = SyntaxHighlighter.AVAILABLE_LANGS[lang]

            if self.lang == "plain": return

            path = pathlib.Path(__file__).parents[0] / "syntax" / f"{self.lang}.json"
            with open(path, "r", encoding="utf-8") as f:
                rr = json.loads(f.read())

                self.keywords = rr["keywords"]
                self.this = rr["this"]
                self.comment = rr["comment"]

            self.operators = operators = (
                    "=",
                    "==", "!=", "<", "<=", ">", ">=",
                    "\+", "-", "\*", "/", "//", "\%", "\*\*",
                    "\+=", "-=", "\*=", "/=", "\%=",
                    "\^", "\|", "\&", "\~", ">>", "<<",
                    "\+\+", "--", "\&\&", "\|\|"
                )

            self.braces = (
                    "\{", "\}", "\(", "\)", "\[", "\]",
                )

        else:
            raise ValueError(f"Language '{lang}' is not supported.")

    def setRules(self):
        self.tri_single = (QRegExp("'''"), 1, self.theme["string"])
        self.tri_double = (QRegExp('"""'), 2, self.theme["string"])

        if self.lang == "plain":
            self.rules = list()
            return

        rules = list()

        rules += [(r'\b%s\b' % w, 0, self.theme["keyword"])  for w in self.keywords]

        rules += [(r'%s' % o,     0, self.theme["operator"]) for o in self.operators]

        rules += [(r'%s' % b,     0, self.theme["brace"])    for b in self.braces]

        if self.lang in ("cpp", "c"):
            rules.append( (r'\#[^\n]*', 0, self.theme["preprocessor"]) )

        rules += [
            (r"\b[A-Za-z0-9_]+(?=\()",  0, self.theme["function"]),

            (r'\b%s\b' % self.this,     0, self.theme["this"]),

            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, self.theme["string"]),

            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, self.theme["string"]),

            (r'%s[^\n]*' % self.comment, 0, self.theme["comment"]),

            (r'\b[+-]?[0-9]+[lL]?\b',                             0, self.theme["numeric"]),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b',                  0, self.theme["numeric"]),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, self.theme["numeric"])
        ]

        self.rules = [(QRegExp(pat), index, fmt) for (pat, index, fmt) in rules]

    def highlightBlock(self, text):
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)

            while index >= 0:
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.tri_double)

    def match_multiline(self, text, delimiter, in_state, style):
        if self.previousBlockState() == in_state:
            start = 0
            add = 0

        else:
            start = delimiter.indexIn(text)
            add = delimiter.matchedLength()

        while start >= 0:
            end = delimiter.indexIn(text, start + add)

            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)

            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add

            self.setFormat(start, length, style)
            start = delimiter.indexIn(text, start + length)


        if self.currentBlockState() == in_state: return True
        else: return False
