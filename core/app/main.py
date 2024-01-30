import json
import os
import sys
import re
import qdarkstyle
from app.trans_core import get
from PySide6.QtCore import *
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import *
from app.ui_browser import Ui_browser
from app.ui_gui import Ui_gui


class Browser(QMainWindow, Ui_browser):
    def __init__(self, txt):
        super().__init__()
        self.setupUi(self)
        self.input = txt

        self.browser = QWebEngineView()
        self.web_layout.addWidget(self.browser)

        self.baidu.clicked.connect(self.reload)
        self.youdao.clicked.connect(self.reload)
        self.bing.clicked.connect(self.reload)
        self.google.clicked.connect(self.reload)
        self.ciba.clicked.connect(self.reload)
        self.oxford.clicked.connect(self.reload)
        self.tencent.clicked.connect(self.reload)
        self.reload()

    def reload(self):
        if self.baidu.isChecked():
            self.browser.load(
                QUrl(f'https://fanyi.baidu.com/#en/zh/{self.input.text()}'))
        elif self.youdao.isChecked():
            self.browser.load(
                QUrl(f'https://www.youdao.com/result?word={self.input.text()}&lang=en'))
        elif self.bing.isChecked():
            self.browser.load(
                QUrl(f'https://cn.bing.com/dict/search?q={self.input.text()}'))
        elif self.google.isChecked():
            self.browser.load(QUrl(
                f'https://translate.google.cn/?sl=en&tl=zh-CN&text={self.input.text()}&op=translate'))
        elif self.ciba.isChecked():
            self.browser.load(
                QUrl(f'http://www.iciba.com/word?w={self.input.text()}'))
        elif self.oxford.isChecked():
            self.browser.load(
                QUrl(f'https://www.oxfordlearnersdictionaries.com/definition/english/{self.input.text()}'))
        elif self.tencent.isChecked():
            self.browser.load(QUrl('https://fanyi.qq.com/'))

    def closeEvent(self, event):
        global window
        window.browser.pop(window.browser.index(self))
        # event.accept()
        print(
            f'delete a browser, now {len(window.browser)} browser(s) remained')


class Main(QMainWindow, Ui_gui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = self.windowFlags()
        self.browser = []
        self.top_convert()
        self.topmost.clicked.connect(self.top_convert)
        self.file_select.clicked.connect(self.file_translate)
        self.web.clicked.connect(self.open_web)
        self.input.textChanged.connect(self.reload)
        self.show()

    def top_convert(self):
        temp = self.browser+[self]
        if self.topmost.isChecked():
            for i in temp:
                i.setWindowFlags(self.flag | Qt.WindowStaysOnTopHint)
                i.show()
        else:
            for i in temp:
                i.setWindowFlags(self.flag)
                i.show()

    def open_web(self):
        self.browser.append(Browser(self.input))
        self.top_convert()
        self.browser[-1].show()
        print(f'create a browser, now {len(self.browser)} browser(s) existed')

    def reload(self):
        if self.browser:
            for i in self.browser:
                if i.auto_update.isChecked():
                    i.reload()

    def translate(self, lis):
        try:
            temp = self.split_list(lis)
            # 翻译结果[ ['',''] ] map后再多一层[]
            temp = list(map(get, temp))[0]
            if self.hide_char.isChecked():
                temp = [re.sub(r'\.+|。+|!+|！+', '', i)
                        for i in temp]  # 这里更改要屏蔽的字符 "<char> +|" +代表>=1个结果
            return temp
        except:
            QMessageBox.warning(self, '警告', f'爬取翻译时发生未知错误，请检查网络连接')
            return ''

    def file_translate(self):
        path, mode = QFileDialog.getOpenFileName(
            self, caption='选择文件和模式', filter='json文件翻译(*.json);;lang文件翻译(*.lang);;文本翻译(*)')
        if path:
            try:
                with open(path, 'r', encoding='utf-8')as file:
                    if mode == 'json文件翻译(*.json)':
                        data = json.load(file)
                        temp = self.translate(list(data.values()))
                        data = dict(zip(data.keys(), temp))
                    elif mode == 'lang文件翻译(*.lang)':
                        data = file.read().split('\n')
                        data = dict([temp.split('=')
                                    for temp in data if '=' in temp])
                        temp = self.translate(list(data.values()))
                        data = '\n'.join(
                            [f'{list(data.keys())[i]}={temp[i]}'for i in range(len(data))])
                    else:
                        data = file.read().split('\n')
                        data = '\n'.join((self.translate(data)))

                    if QMessageBox.question(self, '翻译结果', f'{data}\n是否保存？') == QMessageBox.Yes:
                        path, mode = QFileDialog.getSaveFileName(
                            self, caption='选择路径', filter=mode)
                        if path:
                            with open(path, 'w', encoding='utf-8')as file:
                                file.write(str(data))  # json保存会以非中文保存
                        else:
                            QMessageBox.warning(self, '警告', '路径不存在')
            except Exception as e:
                QMessageBox.warning(self, '警告', f'操作文件时发生未知错误\n{e}')

        else:
            QMessageBox.warning(self, '警告', '路径不存在')

    def split_list(self, lis):
        length, result, temp = 5000, [], ''  # 这里更改列表切分步长
        for i in lis:
            if len(i) > length:
                if temp:
                    result.append(temp)
                    temp = ''
                if ' ' in i:
                    result += self.split_list(i.split(' '))
                else:
                    result.append(i)
            else:
                if len(temp+i) < length:
                    temp = temp+i+'\n'
                else:
                    result.append(temp)
                    temp = i+'\n'
        result.append(temp)
        return result

    def finder(self, en, cn):
        with open('word.txt', 'r', encoding='utf-8')as file:
            if en[0].lower() not in 'abcdefghijklmnopqrstuvwxyz':
                en, cn = cn, en
            data = file.read()
            if data:
                text = data.split('\n')[:-1]
                a, b, c = [], [], []
                for temp in text:
                    if en.lower() == temp.split(' --- ')[0].lower():
                        a.append((text.index(temp), temp))
                    elif en.lower() in temp.split(' --- ')[0].lower():
                        b.append((text.index(temp), temp))
                    elif cn in temp.split(' --- ')[1] or temp.split(' --- ')[1] in cn:
                        c.append((text.index(temp), temp))
                if not a:
                    a = [(-1, '未找到结果')]
                if not b:
                    b = [(-1, '未找到结果')]
                if not c:
                    c = [(-1, '未找到结果')]
                return (a, b, c)
            else:
                return ([(-1, '未找到结果')], [(-1, '未找到结果')], [(-1, '未找到结果')])

    def check_save(self, en, cn):
        try:
            if not os.path.isfile('word.txt'):
                with open('word.txt', 'w', encoding='utf-8')as file:
                    self.browser.browser.load(QUrl(''))

            with open('word.txt', 'a', encoding='utf-8')as file:  # last
                lis = self.finder(en, cn)
                save = QMessageBox.question(self, '保存', '> 找到完全相同结果：\n{}\n> 包含关键字的结果：\n{}\n> 类似结果：\n{}\n仍然保存？'.format(
                    '\n'.join([f'第{temp[0]+1}项：{temp[1]}' for temp in lis[0]]),
                    '\n'.join([f'第{temp[0]+1}项：{temp[1]}' for temp in lis[1]]),
                    '\n'.join([f'第{temp[0]+1}项：{temp[1]}' for temp in lis[2]]))) == QMessageBox.Yes
                if save:
                    if en[0].lower() in 'abcdefghijklmnopqrstuvwxyz':
                        file.write(en+' --- '+cn+'\n')
                    else:
                        file.write(cn+' --- '+en+'\n')
        except:
            QMessageBox.warning(self, '警告', '单词本 word.txt\n格式有误或无修改权限')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            word = self.input.text()
            output = self.translate([word])[0]
            self.output.setText(output)
            self.check_save(word, output)

        elif event.key() == Qt.Key_F1:
            lis = self.finder(self.input.text(), self.output.text())
            QMessageBox.information(self, '查找', '> 找到完全相同结果：\n{}\n> 包含关键字的结果：\n{}\n> 类似结果：\n{}'.format(
                '\n'.join([f'第{temp[0]+1}项：{temp[1]}' for temp in lis[0]]),
                '\n'.join([f'第{temp[0]+1}项：{temp[1]}' for temp in lis[1]]),
                '\n'.join([f'第{temp[0]+1}项：{temp[1]}' for temp in lis[2]])))

        elif event.key() == Qt.Key_F2:
            self.check_save(self.input.text(), self.output.text())

    def closeEvent(self, event):
        if self.browser:
            for i in self.browser:
                i.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
    window = Main()
    sys.exit(app.exec())
