from PyQt5.QtWidgets import QMainWindow
from cadastro import Ui_Cadastro
import sqlite3


class anunciar(QMainWindow):
    try:
        def __init__(self, *args, **kwargs):
            super(anunciar, self).__init__(*args, **kwargs)
            self.tela1 = Ui_Cadastro()
            self.tela1.setupUi(self)
            self.tela1.pushButton.clicked.connect(self._salvar)
            self.tela1.pushButton_2.clicked.connect(self._buscar)
            self.tela1.pushButton_3.clicked.connect(self._excluir)
            self.tela1.pushButton_4.clicked.connect(self._limpar1)
            _ini = self.tela1.lineEdit.setText("0001")

        @staticmethod
        def _buscar():
            ide = input(print("Informe a identificação do imóvel: "))
            try:

                banco = sqlite3.connect('imovel.db')
                cursor = banco.cursor()
                check = cursor.execute("SELECT ident FROM imovel WHERE ident = '"+ide+"' ")

                banco.commit()
                banco.close()
            except Exception as e:
                print("Imóvel não encontrado", e)

        @staticmethod
        def _excluir():
            print("Função EXCLUIR em desenvolvimento")
            banco = sqlite3.connect('imovel.db')
            cursor = banco.cursor()
            cursor.execute("DROP imovel1.db")
            banco.commit()
            banco.close()

        @staticmethod
        def _limpar1():
            print("Função LIMPAR em desenvolvimento")

        def _salvar(self):
            ide = self.tela1.lineEdit.text()
            Ide = int(ide)
            end = self.tela1.lineEdit_2.text()
            num = self.tela1.lineEdit_3.text()
            comp = self.tela1.lineEdit_4.text()
            cep = self.tela1.lineEdit_5.text()
            bar = self.tela1.lineEdit_6.text()
            desc = self.tela1.lineEdit_7.text()
            neg = self.tela1.comboBox_24.currentText()
            tip = self.tela1.comboBox_2.currentText()
            est = self.tela1.comboBox.currentText()
            sta = self.tela1.comboBox_3.currentText()
            prec = self.tela1.comboBox_4.currentText()
            quar = self.tela1.comboBox_5.currentText()
            ban = self.tela1.comboBox_6.currentText()
            suite = self.tela1.comboBox_7.currentText()
            saest = self.tela1.comboBox_8.currentText()
            saljan = self.tela1.comboBox_9.currentText()
            pisc = self.tela1.comboBox_10.currentText()
            arser = self.tela1.comboBox_21.currentText()
            arlaz = self.tela1.comboBox_22.currentText()
            gar = self.tela1.comboBox_23.currentText()
            obs = self.tela1.plainTextEdit.toPlainText()
            cond = self.tela1.plainTextEdit_2.toPlainText()

            try:
                banco = sqlite3.connect('imovel.db')
                cursor = banco.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS imovel (ident text, ender text, numer text, complem text, "
                               "cep text, bairro text, descric text, negocia text, tipo text, estado text, status text,"
                               "preco text, quarto text, banho text, suite text, salaestar text, salajanta text, "
                               "piscina text, arserv text, arlazer text, garag text, observ text, condic text)")
                cursor.execute("INSERT INTO imovel VALUES ('"+ide+"', '"+end+"', '"+num+"', '"+comp+"', '"+cep+"', "
                                "'"+bar+"','"+desc+"','"+neg+"','"+tip+"','"+est+"','"+sta+"','"+prec+"','"+quar+"',"
                                "'"+ban+"','"+suite+"','"+saest+"','"+saljan+"','"+pisc+"','"+arser+"','"+arlaz+"',"
                                "'"+gar+"','"+obs+"','"+cond+"')")

                banco.commit()
                banco.close()

                self.tela1.lineEdit.setText("")
                self.tela1.lineEdit_2.setText("")
                self.tela1.lineEdit_3.setText("")
                self.tela1.lineEdit_4.setText("")
                self.tela1.lineEdit_5.setText("")
                self.tela1.lineEdit_6.setText("")
                self.tela1.lineEdit_7.setText("")
                self.tela1.comboBox_24.clearEditText()
                self.tela1.comboBox_2.clearEditText()
                self.tela1.comboBox.clearEditText()
                self.tela1.comboBox_3.clearEditText()
                self.tela1.comboBox_4.clearEditText()
                self.tela1.comboBox_5.clearEditText()
                self.tela1.comboBox_6.clearEditText()
                self.tela1.comboBox_7.clearEditText()
                self.tela1.comboBox_8.clearEditText()
                self.tela1.comboBox_9.clearEditText()
                self.tela1.comboBox_10.clearEditText()
                self.tela1.comboBox_21.clearEditText()
                self.tela1.comboBox_22.clearEditText()
                self.tela1.comboBox_23.clearEditText()
                self.tela1.plainTextEdit.setPlainText("")
                self.tela1.plainTextEdit_2.setPlainText("")
                Ide += 1
                ide = str(Ide)
                self.tela1.lineEdit.setText("000"+ide)
            except sqlite3.Error as e:
                print("Erro ao inserir dados: ", e)
    except Exception as e:
        print("Erro de:", e)
