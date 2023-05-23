# Funções dos botões da aplicação.

from PyQt5.QtWidgets import QMainWindow
import _appFuncCad
from main import Ui_MainWindow

class _telaP(QMainWindow):
    try:
        def __init__(self, *args, **kwargs):
            super(_telaP, self).__init__(*args, **kwargs)
            self.tela = Ui_MainWindow()
            self.tela.setupUi(self)
            self.tela.pushButton.clicked.connect(self._iniciar)
            self.tela.pushButton_2.clicked.connect(self._comprar)
            self.tela.pushButton_3.clicked.connect(self._alugar)
            self.tela.pushButton_4.clicked.connect(self._cadastrar)
            self.tela.pushButton_5.clicked.connect(self._avaliar)
            self.tela.pushButton_6.clicked.connect(self._enviar)
            self.tela.pushButton_7.clicked.connect(self._limpar)

        def _iniciar(self):
            print("Função INICIAR em desenvolvimento")

        def _comprar(self):
            print("Função COMPRAR em desenvolvimento")

        def _alugar(self):
            print("Função ALUGAR em desenvolvimento")

        def _cadastrar(self):
            self.ui = _appFuncCad.anunciar()
            self.ui.show()

        def _avaliar(self):
            print("Função AVALIAR em desenvolvimento")

        def _enviar(self):
            print("Função ENVIAR em desenvolvimento")

        def _limpar(self):
            self.tela.textEdit.setText("")

    except Exception as e:
        print("Erro de:", e)
