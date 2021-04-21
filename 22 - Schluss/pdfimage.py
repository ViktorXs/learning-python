import os

class PdfImage():
    def __init__(self, src, width=1):
        self.src = src
        self.width = width

    # Der Bild-Einbindungscode für die Anzeige in Jupyter
    def _repr_html_(self):
        return '<img src={0} style="width: {1}%;"/></iframe>'.format(self.src, self.width * 100)

    # Der Bild-Einbindungscode für das PDF
    def _repr_latex_(self):
        src = os.path.abspath(os.getcwd()) + "/" + self.src
        return r'\Oldincludegraphics[width={1}\textwidth]{{{0}}}'.format(src, self.width)