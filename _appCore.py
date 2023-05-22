# Favor atentar que os somente o botão "Anunciar" contém as funções pedidas na atividade MAPA
# Os outros botões foram somente apresentados como parte do desenvolvimento da interace
# Apesar de ser um protótipo, os outros botões tem função somente demonstrativa com impressão de mensagem.

import sys
from PyQt5.QtWidgets import QDialog, QApplication
import appFunc
from main import Ui_MainWindow

app = QApplication(sys.argv)
if QDialog.Accepted:
    tela = appFunc._telaP()
    tela.show()
sys.exit(app.exec_())


